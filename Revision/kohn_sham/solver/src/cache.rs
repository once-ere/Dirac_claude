//! Job cache of the canonical matrix, so that the matrix can be computed in parts, each within a time limit.
//!
//! `all --cache DIR --part i/n` computes a fixed part of the ground and thermal tasks (balanced by `cost`) and
//! stores every finished task in DIR; `all --cache DIR` then computes any task still missing, assembles and
//! writes the outputs.  Every task is a pure function of its inputs and every float is stored as its IEEE-754
//! bit pattern, so the assembled outputs are byte for byte those of one run without a cache.  The cache is tied
//! to a key (the SHA-256 of ks-theory.json, gammas.json and of the solver source embedded in this binary, the
//! numerics and the --quick flag): a cache made with other inputs is refused.

use crate::json::{obj, parse, to_pretty, Json};
use crate::model::{Parity, Shell};
use crate::runs::{ContSeed, GroundOut, Item, MuDiag, ThermOut};
use crate::scf::{Key, SectorSpec};
use crate::shoot::Pots;
use std::collections::BTreeMap;
use std::path::{Path, PathBuf};

const SOURCES: [(&str, &str); 14] = [
    ("Cargo.toml", include_str!("../Cargo.toml")),
    ("analysis.rs", include_str!("analysis.rs")),
    ("cache.rs", include_str!("cache.rs")),
    ("json.rs", include_str!("json.rs")),
    ("main.rs", include_str!("main.rs")),
    ("mermin.rs", include_str!("mermin.rs")),
    ("model.rs", include_str!("model.rs")),
    ("report.rs", include_str!("report.rs")),
    ("runs.rs", include_str!("runs.rs")),
    ("scf.rs", include_str!("scf.rs")),
    ("sha256.rs", include_str!("sha256.rs")),
    ("shoot.rs", include_str!("shoot.rs")),
    ("spectrum.rs", include_str!("spectrum.rs")),
    ("theory.rs", include_str!("theory.rs")),
];

/// SHA-256 of the solver source compiled into this binary (file names, lengths and contents).
pub fn source_sha256() -> String {
    let mut s: Vec<u8> = Vec::new();
    for (n, c) in SOURCES {
        s.extend_from_slice(n.as_bytes());
        s.push(0);
        s.extend_from_slice(c.len().to_string().as_bytes());
        s.push(0);
        s.extend_from_slice(c.as_bytes());
    }
    crate::sha256::hex(&s)
}

pub struct Cache {
    pub dir: PathBuf,
}

impl Cache {
    /// Open (or create) the cache directory and check its key.
    pub fn open(dir: &Path, key: &str) -> Result<Cache, String> {
        std::fs::create_dir_all(dir).map_err(|e| format!("{}: {}", dir.display(), e))?;
        let kp = dir.join("cache-key.txt");
        if kp.exists() {
            let have = std::fs::read_to_string(&kp).map_err(|e| e.to_string())?;
            if have != key {
                return Err(format!("{} was made with other inputs (cache-key.txt differs): use a fresh cache directory", dir.display()));
            }
        } else {
            std::fs::write(&kp, key.as_bytes()).map_err(|e| e.to_string())?;
        }
        Ok(Cache { dir: dir.to_path_buf() })
    }
    fn path(&self, kind: &str, id: &str) -> PathBuf {
        self.dir.join(format!("{}-{}.json", kind, id))
    }
    pub fn load(&self, kind: &str, id: &str) -> Result<Option<Json>, String> {
        let p = self.path(kind, id);
        if !p.exists() {
            return Ok(None);
        }
        let s = std::fs::read_to_string(&p).map_err(|e| format!("{}: {}", p.display(), e))?;
        parse(&s).map(Some).map_err(|e| format!("{}: {}", p.display(), e))
    }
    /// Write atomically (temporary file, then rename).
    pub fn save(&self, kind: &str, id: &str, j: &Json) -> Result<(), String> {
        let p = self.path(kind, id);
        let tmp = self.dir.join(format!("{}-{}.json.tmp", kind, id));
        std::fs::write(&tmp, to_pretty(j).as_bytes()).map_err(|e| format!("{}: {}", tmp.display(), e))?;
        std::fs::rename(&tmp, &p).map_err(|e| format!("{}: {}", p.display(), e))
    }
}

// --- exact encodings ------------------------------------------------------------------------------
fn fx(x: f64) -> Json {
    Json::Str(format!("{:016x}", x.to_bits()))
}
fn xf(j: &Json) -> Result<f64, String> {
    let s = j.as_str().ok_or("cache: a float (hex bits) expected")?;
    u64::from_str_radix(s, 16).map(f64::from_bits).map_err(|e| format!("cache float {}: {}", s, e))
}
fn fv(v: &[f64]) -> Json {
    Json::Arr(v.iter().map(|&x| fx(x)).collect())
}
fn vf(j: &Json) -> Result<Vec<f64>, String> {
    j.as_arr().ok_or("cache: array expected")?.iter().map(xf).collect()
}
fn sv(v: &[String]) -> Json {
    Json::Arr(v.iter().map(|s| Json::Str(s.clone())).collect())
}
fn vs(j: &Json) -> Result<Vec<String>, String> {
    j.as_arr().ok_or("cache: array expected")?.iter().map(|x| x.as_str().map(|s| s.to_string()).ok_or_else(|| "cache: string expected".to_string())).collect()
}
fn int(j: &Json) -> Result<i64, String> {
    match j {
        Json::Int(i) => Ok(*i),
        _ => Err("cache: integer expected".into()),
    }
}
fn boolean(j: &Json) -> Result<bool, String> {
    match j {
        Json::Bool(b) => Ok(*b),
        _ => Err("cache: boolean expected".into()),
    }
}
fn field<'a>(j: &'a Json, k: &str) -> Result<&'a Json, String> {
    j.get(k).ok_or_else(|| format!("cache: field {} missing", k))
}
fn string(j: &Json) -> Result<String, String> {
    j.as_str().map(|s| s.to_string()).ok_or_else(|| "cache: string expected".to_string())
}
/// A Json value with every number stored exactly ({"$f": bits}).
fn enc(j: &Json) -> Json {
    match j {
        Json::Num(x) => obj(vec![("$f", fx(*x))]),
        Json::Arr(v) => Json::Arr(v.iter().map(enc).collect()),
        Json::Obj(v) => Json::Obj(v.iter().map(|(k, x)| (k.clone(), enc(x))).collect()),
        other => other.clone(),
    }
}
fn dec(j: &Json) -> Result<Json, String> {
    Ok(match j {
        Json::Obj(v) if v.len() == 1 && v[0].0 == "$f" => Json::Num(xf(&v[0].1)?),
        Json::Arr(v) => Json::Arr(v.iter().map(dec).collect::<Result<_, _>>()?),
        Json::Obj(v) => Json::Obj(v.iter().map(|(k, x)| dec(x).map(|y| (k.clone(), y))).collect::<Result<_, _>>()?),
        other => other.clone(),
    })
}
fn par(s: &str) -> Result<Parity, String> {
    match s {
        "even" => Ok(Parity::Even),
        "odd" => Ok(Parity::Odd),
        _ => Err(format!("cache: parity {}", s)),
    }
}
fn key_j(k: &Key) -> Json {
    Json::Arr(vec![k.0.into(), k.1.into(), k.2.tag().into(), Json::Int(k.3)])
}
fn j_key(j: &Json) -> Result<Key, String> {
    let a = j.as_arr().ok_or("cache: key")?;
    if a.len() != 4 {
        return Err("cache: key length".into());
    }
    Ok((int(&a[0])? as u32, int(&a[1])? as i32, par(a[2].as_str().ok_or("cache: key parity")?)?, int(&a[3])?))
}
fn items_j(items: &[Item]) -> Json {
    Json::Arr(
        items
            .iter()
            .map(|x| {
                obj(vec![
                    ("name", x.name.clone().into()),
                    ("desc", x.desc.clone().into()),
                    ("tol", fx(x.tol)),
                    ("value", fx(x.value)),
                    ("pass", x.pass.map(Json::Bool).unwrap_or(Json::Null)),
                ])
            })
            .collect(),
    )
}
fn j_items(j: &Json) -> Result<Vec<Item>, String> {
    j.as_arr()
        .ok_or("cache: items")?
        .iter()
        .map(|x| {
            Ok(Item {
                name: string(field(x, "name")?)?,
                desc: string(field(x, "desc")?)?,
                tol: xf(field(x, "tol")?)?,
                value: xf(field(x, "value")?)?,
                pass: match field(x, "pass")? {
                    Json::Null => None,
                    b => Some(boolean(b)?),
                },
            })
        })
        .collect()
}
fn opt_sv(v: &Option<Vec<String>>) -> Json {
    v.as_ref().map(|x| sv(x)).unwrap_or(Json::Null)
}
fn opt_vs(j: &Json) -> Result<Option<Vec<String>>, String> {
    match j {
        Json::Null => Ok(None),
        x => vs(x).map(Some),
    }
}

// --- the outputs of a task --------------------------------------------------------------------------
pub fn ground_to_json(o: &GroundOut) -> Json {
    let seed = match &o.seed {
        None => Json::Null,
        Some(s) => obj(vec![
            ("lambda", fx(s.lambda)),
            (
                "specs",
                Json::Arr(
                    s.specs
                        .iter()
                        .map(|sp| Json::Arr(vec![sp.shell.n2.into(), sp.shell.r3.into(), sp.j.into(), sp.parity.tag().into(), Json::Int(sp.ell_min), sp.nlev.into()]))
                        .collect(),
                ),
            ),
            ("mass", fv(&s.pots.mass)),
            ("v", fv(&s.pots.v)),
            ("wq", fv(&s.pots.wq)),
            ("guesses", Json::Arr(s.guesses.iter().map(|(k, e)| Json::Arr(vec![key_j(k), fx(*e)])).collect())),
        ]),
    };
    obj(vec![
        ("id", o.id.clone().into()),
        ("n", fx(o.n)),
        ("tag", o.tag.clone().into()),
        ("ia", o.ia.into()),
        ("items", items_j(&o.items)),
        ("files", Json::Arr(o.files.iter().map(|(p, c)| Json::Arr(vec![p.clone().into(), c.clone().into()])).collect())),
        ("summary", sv(&o.summary)),
        ("excited", sv(&o.excited)),
        ("adiab", sv(&o.adiab)),
        ("emtrow", sv(&o.emtrow)),
        ("rescale", opt_sv(&o.rescale)),
        ("exx", opt_sv(&o.exx)),
        ("occ", Json::Arr(o.occ.iter().map(|(k, f)| Json::Arr(vec![key_j(k), fx(*f)])).collect())),
        ("seed", seed),
        ("record", enc(&o.record)),
        ("error", o.error.clone().map(Json::Str).unwrap_or(Json::Null)),
        ("e_ks", fx(o.e_ks)),
    ])
}

pub fn ground_from_json(j: &Json) -> Result<GroundOut, String> {
    let seed = match field(j, "seed")? {
        Json::Null => None,
        s => {
            let mut specs = Vec::new();
            for x in field(s, "specs")?.as_arr().ok_or("cache: specs")? {
                let a = x.as_arr().ok_or("cache: spec")?;
                if a.len() != 6 {
                    return Err("cache: spec length".into());
                }
                specs.push(SectorSpec {
                    shell: Shell { n2: int(&a[0])? as u32, r3: int(&a[1])? as u32 },
                    j: int(&a[2])? as i32,
                    parity: par(a[3].as_str().ok_or("cache: spec parity")?)?,
                    ell_min: int(&a[4])?,
                    nlev: int(&a[5])? as usize,
                });
            }
            let mut guesses = BTreeMap::new();
            for x in field(s, "guesses")?.as_arr().ok_or("cache: guesses")? {
                let a = x.as_arr().ok_or("cache: guess")?;
                guesses.insert(j_key(&a[0])?, xf(&a[1])?);
            }
            Some(ContSeed {
                lambda: xf(field(s, "lambda")?)?,
                specs,
                pots: Pots { mass: vf(field(s, "mass")?)?, v: vf(field(s, "v")?)?, wq: vf(field(s, "wq")?)? },
                guesses,
            })
        }
    };
    let mut occ = BTreeMap::new();
    for x in field(j, "occ")?.as_arr().ok_or("cache: occ")? {
        let a = x.as_arr().ok_or("cache: occ entry")?;
        occ.insert(j_key(&a[0])?, xf(&a[1])?);
    }
    let mut files = Vec::new();
    for x in field(j, "files")?.as_arr().ok_or("cache: files")? {
        let a = x.as_arr().ok_or("cache: file")?;
        files.push((string(&a[0])?, string(&a[1])?));
    }
    Ok(GroundOut {
        id: string(field(j, "id")?)?,
        n: xf(field(j, "n")?)?,
        tag: string(field(j, "tag")?)?,
        ia: int(field(j, "ia")?)? as usize,
        items: j_items(field(j, "items")?)?,
        files,
        summary: vs(field(j, "summary")?)?,
        excited: vs(field(j, "excited")?)?,
        adiab: vs(field(j, "adiab")?)?,
        emtrow: vs(field(j, "emtrow")?)?,
        rescale: opt_vs(field(j, "rescale")?)?,
        exx: opt_vs(field(j, "exx")?)?,
        occ,
        seed,
        record: dec(field(j, "record")?)?,
        error: match field(j, "error")? {
            Json::Null => None,
            e => Some(string(e)?),
        },
        e_ks: xf(field(j, "e_ks")?)?,
    })
}

pub fn thermal_to_json(o: &ThermOut) -> Json {
    let mu = match &o.mu {
        None => Json::Null,
        Some(m) => obj(vec![
            ("own_equal", m.own_equal.into()),
            ("dev_ab", fx(m.dev_ab)),
            ("bound_ab", fx(m.bound_ab)),
            ("dev_direct", fx(m.dev_direct)),
            ("bound_direct", fx(m.bound_direct)),
            ("dn_dmu", fx(m.dn_dmu)),
            ("passes", m.passes.into()),
        ]),
    };
    obj(vec![("id", o.id.clone().into()), ("row", sv(&o.row)), ("items", items_j(&o.items)), ("holes_over_n", fx(o.holes_over_n)), ("mu", mu)])
}

pub fn thermal_from_json(j: &Json) -> Result<ThermOut, String> {
    let mu = match field(j, "mu")? {
        Json::Null => None,
        m => Some(MuDiag {
            own_equal: boolean(field(m, "own_equal")?)?,
            dev_ab: xf(field(m, "dev_ab")?)?,
            bound_ab: xf(field(m, "bound_ab")?)?,
            dev_direct: xf(field(m, "dev_direct")?)?,
            bound_direct: xf(field(m, "bound_direct")?)?,
            dn_dmu: xf(field(m, "dn_dmu")?)?,
            passes: int(field(m, "passes")?)? as usize,
        }),
    };
    Ok(ThermOut {
        row: vs(field(j, "row")?)?,
        items: j_items(field(j, "items")?)?,
        id: string(field(j, "id")?)?,
        holes_over_n: xf(field(j, "holes_over_n")?)?,
        mu,
    })
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn exact_float_roundtrip() {
        for x in [0.1f64, -1.0 / 3.0, 1e-300, f64::MAX, f64::MIN_POSITIVE, 0.0, -0.0, f64::INFINITY, 2.0f64.sqrt()] {
            let y = xf(&fx(x)).unwrap();
            assert_eq!(x.to_bits(), y.to_bits());
        }
        let n = xf(&fx(f64::NAN)).unwrap();
        assert!(n.is_nan());
        let j = obj(vec![("a", Json::Num(0.1 + 0.2)), ("b", Json::Arr(vec![Json::Num(1.0 / 7.0), Json::Int(3), Json::Null]))]);
        let back = dec(&parse(&to_pretty(&enc(&j))).unwrap()).unwrap();
        assert_eq!(to_pretty(&back), to_pretty(&j));
        match back.get("a") {
            Some(Json::Num(x)) => assert_eq!(x.to_bits(), (0.1f64 + 0.2).to_bits()),
            _ => panic!("a"),
        }
    }
}
