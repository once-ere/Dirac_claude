//! Deterministic JSON and Markdown writers (no external crates).

use crate::geometry::{COORD, DIM};
use crate::poly::Poly;
use std::fmt::Write as _;

pub fn json_str(s: &str) -> String {
    let mut o = String::with_capacity(s.len() + 2);
    o.push('"');
    for ch in s.chars() {
        match ch {
            '"' => o.push_str("\\\""),
            '\\' => o.push_str("\\\\"),
            '\n' => o.push_str("\\n"),
            c if (c as u32) < 0x20 => write!(o, "\\u{:04x}", c as u32).unwrap(),
            c => o.push(c),
        }
    }
    o.push('"');
    o
}

/// All 64 components of a rank-2 object as a JSON object
/// {"x1,x1": {"mathematica": ..., "latex": ...}, ...} in the index order [row][col].
pub fn tensor_json(t: &[Vec<Poly>], indent: &str) -> String {
    let mut o = String::from("{\n");
    let mut first = true;
    for r in 0..DIM {
        for c in 0..DIM {
            if !first {
                o.push_str(",\n");
            }
            first = false;
            write!(
                o,
                "{indent}  {}: {{\"mathematica\": {}, \"latex\": {}, \"monomials\": {}}}",
                json_str(&format!("{},{}", COORD[r], COORD[c])),
                json_str(&t[r][c].to_mathematica()),
                json_str(&t[r][c].to_latex()),
                monomials_json(&t[r][c])
            )
            .unwrap();
        }
    }
    write!(o, "\n{indent}}}").unwrap();
    o
}

/// Exact machine-readable form: [[numerator, denominator, [e_H, e_a4', e_a4'', e_a4''',
/// e_a4'''', e_E, e_S, e_C]], ...] (symbols as in poly.rs), so that an independent
/// program can rebuild every term without parsing text.
pub fn monomials_json(p: &Poly) -> String {
    let items: Vec<String> = p
        .terms()
        .iter()
        .map(|(m, c)| format!("[{}, {}, [{}]]", c.num(), c.den(), m.iter().map(|e| e.to_string()).collect::<Vec<_>>().join(", ")))
        .collect();
    format!("[{}]", items.join(", "))
}

/// A Markdown list of all 64 components (zeros written out).
pub fn tensor_markdown(name: &str, t: &[Vec<Poly>], row_up: bool, col_up: bool) -> String {
    let mut o = String::new();
    for r in 0..DIM {
        for c in 0..DIM {
            let idx = |i: usize, up: bool| if up { format!("^{{{}}}", COORD[i]) } else { format!("_{{{}}}", COORD[i]) };
            writeln!(o, "- ${}{}{}= {}$", name, idx(r, row_up), idx(c, col_up), t[r][c].to_latex()).unwrap();
        }
    }
    o
}
