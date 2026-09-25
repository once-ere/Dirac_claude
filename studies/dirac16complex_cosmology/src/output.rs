//! Deterministic writers shared by all experiments.
//!
//! * Numbers are always formatted with the engine's C-style
//!   `sundials_core::sundials_utils::fmt_e(v, 17)` (C `%.17e`), never Rust's
//!   `{:e}`; a negative zero is normalised to `0.0` first (`v + 0.0`), so
//!   a structurally zero column never prints as `-0.000...e+00`.
//! * CSV: one header row, comma separated, LF line endings, trailing newline.
//! * JSON: [`Json`] keeps object keys in insertion order; the serializer
//!   uses a 2-space indent, `": "` after keys, LF, trailing newline; floats
//!   via `fmt17`, non-finite floats as `null`; strings are escaped per
//!   RFC 8259 (ASCII output).
//! * Nothing written here may contain absolute paths or timings: the repeat
//!   run writes into another directory and must be byte-identical.

use std::fs;
use std::path::Path;

use sundials_core::sundials_utils::fmt_e;

use crate::{ExperimentSummary, RunContext, Tolerances};

/// `fmt_e(v + 0.0, 17)`.
pub fn fmt17(value: f64) -> String {
    fmt_e(value + 0.0, 17)
}

/// Write a CSV table (header + rows of floats).
pub fn write_csv(path: &Path, header: &[String], rows: &[Vec<f64>]) -> Result<(), String> {
    let mut text = String::with_capacity(rows.len() * header.len() * 25 + 256);
    text.push_str(&header.join(","));
    text.push('\n');
    for (index, row) in rows.iter().enumerate() {
        if row.len() != header.len() {
            return Err(format!(
                "{}: row {index} has {} values, header has {}",
                path.display(),
                row.len(),
                header.len()
            ));
        }
        for (column, value) in row.iter().enumerate() {
            if column > 0 {
                text.push(',');
            }
            text.push_str(&fmt17(*value));
        }
        text.push('\n');
    }
    fs::write(path, text).map_err(|error| format!("write {} failed: {error}", path.display()))
}

/// Ordered JSON value.
#[derive(Clone, Debug, PartialEq)]
pub enum Json {
    Null,
    Bool(bool),
    Int(i64),
    Float(f64),
    Str(String),
    Array(Vec<Json>),
    Object(Vec<(String, Json)>),
}

impl Json {
    pub fn str(value: &str) -> Json {
        Json::Str(value.to_string())
    }

    pub fn floats(values: &[f64]) -> Json {
        Json::Array(values.iter().map(|v| Json::Float(*v)).collect())
    }

    /// Build an object from (key, value) pairs, keeping their order.
    pub fn object(pairs: Vec<(&str, Json)>) -> Json {
        Json::Object(pairs.into_iter().map(|(k, v)| (k.to_string(), v)).collect())
    }

    /// Serialize with a 2-space indent and a trailing newline.
    pub fn to_text(&self) -> String {
        let mut out = String::new();
        self.write_into(&mut out, 0);
        out.push('\n');
        out
    }

    fn write_into(&self, out: &mut String, depth: usize) {
        match self {
            Json::Null => out.push_str("null"),
            Json::Bool(value) => out.push_str(if *value { "true" } else { "false" }),
            Json::Int(value) => out.push_str(&value.to_string()),
            Json::Float(value) => {
                if value.is_finite() {
                    out.push_str(&fmt17(*value));
                } else {
                    out.push_str("null");
                }
            }
            Json::Str(value) => escape_into(out, value),
            Json::Array(items) => {
                if items.is_empty() {
                    out.push_str("[]");
                    return;
                }
                out.push_str("[\n");
                for (index, item) in items.iter().enumerate() {
                    indent(out, depth + 1);
                    item.write_into(out, depth + 1);
                    if index + 1 < items.len() {
                        out.push(',');
                    }
                    out.push('\n');
                }
                indent(out, depth);
                out.push(']');
            }
            Json::Object(pairs) => {
                if pairs.is_empty() {
                    out.push_str("{}");
                    return;
                }
                out.push_str("{\n");
                for (index, (key, value)) in pairs.iter().enumerate() {
                    indent(out, depth + 1);
                    escape_into(out, key);
                    out.push_str(": ");
                    value.write_into(out, depth + 1);
                    if index + 1 < pairs.len() {
                        out.push(',');
                    }
                    out.push('\n');
                }
                indent(out, depth);
                out.push('}');
            }
        }
    }
}

fn indent(out: &mut String, depth: usize) {
    for _ in 0..depth {
        out.push_str("  ");
    }
}

fn escape_into(out: &mut String, value: &str) {
    out.push('"');
    for ch in value.chars() {
        match ch {
            '"' => out.push_str("\\\""),
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if (c as u32) < 0x20 || (c as u32) > 0x7e => {
                let mut buffer = [0u16; 2];
                for unit in c.encode_utf16(&mut buffer) {
                    out.push_str(&format!("\\u{:04x}", unit));
                }
            }
            c => out.push(c),
        }
    }
    out.push('"');
}

/// Write a JSON document.
pub fn write_json(path: &Path, value: &Json) -> Result<(), String> {
    fs::write(path, value.to_text())
        .map_err(|error| format!("write {} failed: {error}", path.display()))
}

/// The fixed-order summary.json document shared by all experiments:
/// schemaVersion, study, experiment, fixture{path, sha256, source}, engine,
/// solver, refined, tolerances{rtol, atol, maxStep}, <extra fields in the
/// given order>, files, solverTotals{steps, rhsEvaluations}, checks{name:
/// bool}, verdict.  `summary.files` should already list every data file;
/// "summary.json" is appended here.
pub fn standard_summary(
    ctx: &RunContext,
    summary: &ExperimentSummary,
    tolerances: &Tolerances,
    solver: &str,
    extra: Vec<(&str, Json)>,
) -> Json {
    let mut files: Vec<Json> = summary.files.iter().map(|f| Json::str(f)).collect();
    files.push(Json::str("summary.json"));
    let mut pairs: Vec<(String, Json)> = vec![
        (
            "schemaVersion".to_string(),
            Json::Int(crate::SCHEMA_VERSION),
        ),
        ("study".to_string(), Json::str(crate::STUDY)),
        ("experiment".to_string(), Json::str(&summary.experiment)),
        (
            "fixture".to_string(),
            Json::object(vec![
                ("path", Json::str(crate::FIXTURE_PATH)),
                ("sha256", Json::str(crate::FIXTURE_SHA256)),
                ("source", Json::str(crate::FIXTURE_SOURCE)),
            ]),
        ),
        ("engine".to_string(), Json::str(crate::ENGINE)),
        ("solver".to_string(), Json::str(solver)),
        ("refined".to_string(), Json::Bool(ctx.refined)),
        (
            "tolerances".to_string(),
            Json::object(vec![
                ("rtol", Json::Float(tolerances.rtol)),
                ("atol", Json::Float(tolerances.atol)),
                ("maxStep", Json::Float(tolerances.max_step)),
            ]),
        ),
    ];
    for (key, value) in extra {
        pairs.push((key.to_string(), value));
    }
    pairs.push(("files".to_string(), Json::Array(files)));
    pairs.push((
        "solverTotals".to_string(),
        Json::object(vec![
            ("steps", Json::Int(summary.solver_steps)),
            ("rhsEvaluations", Json::Int(summary.rhs_evaluations)),
        ]),
    ));
    pairs.push((
        "checks".to_string(),
        Json::Object(
            summary
                .checks
                .iter()
                .map(|check| (check.name.clone(), Json::Bool(check.passed)))
                .collect(),
        ),
    ));
    pairs.push(("verdict".to_string(), Json::str(summary.verdict())));
    Json::Object(pairs)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn json_layout_is_fixed() {
        let doc = Json::object(vec![
            ("a", Json::Int(1)),
            ("b", Json::floats(&[0.5, -0.0])),
            (
                "c",
                Json::object(vec![("d", Json::str("x\"y")), ("e", Json::Null)]),
            ),
            ("f", Json::Array(vec![])),
            ("g", Json::Float(f64::NAN)),
        ]);
        let expected = "{\n  \"a\": 1,\n  \"b\": [\n    5.00000000000000000e-01,\n    \
                        0.00000000000000000e+00\n  ],\n  \"c\": {\n    \"d\": \"x\\\"y\",\n    \
                        \"e\": null\n  },\n  \"f\": [],\n  \"g\": null\n}\n";
        assert_eq!(doc.to_text(), expected);
    }

    #[test]
    fn fmt17_normalises_negative_zero() {
        assert_eq!(fmt17(-0.0), "0.00000000000000000e+00");
        assert_eq!(fmt17(-1.5), "-1.50000000000000000e+00");
        assert_eq!(fmt17(0.1), "1.00000000000000006e-01");
    }
}
