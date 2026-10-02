//! Check report: every check has a name, a verdict (PASS/FAIL) and a detail.

use crate::json::{obj, Json};

#[derive(Clone, Debug)]
pub struct Check {
    pub name: String,
    pub pass: bool,
    pub detail: String,
}

#[derive(Clone, Debug, Default)]
pub struct Report {
    pub checks: Vec<Check>,
}

impl Report {
    pub fn check(&mut self, name: &str, pass: bool, detail: String) {
        eprintln!("{} - {}: {}", if pass { "PASS" } else { "FAIL" }, name, detail);
        self.checks.push(Check { name: name.to_string(), pass, detail });
    }
    pub fn n_fail(&self) -> usize {
        self.checks.iter().filter(|c| !c.pass).count()
    }
    pub fn to_json(&self) -> Json {
        Json::Arr(
            self.checks
                .iter()
                .map(|c| obj(vec![("name", c.name.clone().into()), ("verdict", (if c.pass { "PASS" } else { "FAIL" }).into()), ("detail", c.detail.clone().into())]))
                .collect(),
        )
    }
}
