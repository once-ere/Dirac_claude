//! Minimal JSON reader and deterministic writer (no external crates).
//!
//! Writer conventions (byte-identical repeat runs): objects keep insertion
//! order, 2-space indentation, LF, trailing newline; floats are written with
//! 16 significant digits (`{:.15e}`), non-finite floats as `null`.

#[derive(Clone, Debug)]
pub enum Json {
    Null,
    Bool(bool),
    Num(f64),
    Int(i64),
    Str(String),
    Arr(Vec<Json>),
    Obj(Vec<(String, Json)>),
}

impl Json {
    pub fn get(&self, key: &str) -> Option<&Json> {
        match self {
            Json::Obj(v) => v.iter().find(|(k, _)| k == key).map(|(_, x)| x),
            _ => None,
        }
    }
    pub fn path(&self, keys: &[&str]) -> Option<&Json> {
        let mut cur = self;
        for k in keys {
            cur = cur.get(k)?;
        }
        Some(cur)
    }
    pub fn as_arr(&self) -> Option<&Vec<Json>> {
        match self {
            Json::Arr(v) => Some(v),
            _ => None,
        }
    }
    pub fn as_str(&self) -> Option<&str> {
        match self {
            Json::Str(s) => Some(s),
            _ => None,
        }
    }
    pub fn as_f64(&self) -> Option<f64> {
        match self {
            Json::Num(x) => Some(*x),
            Json::Int(i) => Some(*i as f64),
            _ => None,
        }
    }
}

impl From<f64> for Json {
    fn from(x: f64) -> Json {
        Json::Num(x)
    }
}
impl From<i64> for Json {
    fn from(x: i64) -> Json {
        Json::Int(x)
    }
}
impl From<i32> for Json {
    fn from(x: i32) -> Json {
        Json::Int(x as i64)
    }
}
impl From<usize> for Json {
    fn from(x: usize) -> Json {
        Json::Int(x as i64)
    }
}
impl From<u32> for Json {
    fn from(x: u32) -> Json {
        Json::Int(x as i64)
    }
}
impl From<bool> for Json {
    fn from(x: bool) -> Json {
        Json::Bool(x)
    }
}
impl From<&str> for Json {
    fn from(x: &str) -> Json {
        Json::Str(x.to_string())
    }
}
impl From<String> for Json {
    fn from(x: String) -> Json {
        Json::Str(x)
    }
}
impl From<Vec<Json>> for Json {
    fn from(x: Vec<Json>) -> Json {
        Json::Arr(x)
    }
}
impl From<Vec<f64>> for Json {
    fn from(x: Vec<f64>) -> Json {
        Json::Arr(x.into_iter().map(Json::Num).collect())
    }
}

/// Build an object from (key, value) pairs, keeping the order.
pub fn obj(items: Vec<(&str, Json)>) -> Json {
    Json::Obj(items.into_iter().map(|(k, v)| (k.to_string(), v)).collect())
}

/// Deterministic float format: 16 significant digits.
pub fn fmt_f(x: f64) -> String {
    if x.is_finite() {
        format!("{:.15e}", x)
    } else {
        "null".to_string()
    }
}

fn esc(s: &str, out: &mut String) {
    out.push('"');
    for c in s.chars() {
        match c {
            '"' => out.push_str("\\\""),
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\t' => out.push_str("\\t"),
            '\r' => out.push_str("\\r"),
            c if (c as u32) < 0x20 => out.push_str(&format!("\\u{:04x}", c as u32)),
            c => out.push(c),
        }
    }
    out.push('"');
}

fn is_scalar(j: &Json) -> bool {
    !matches!(j, Json::Arr(_) | Json::Obj(_))
}

fn write(j: &Json, ind: usize, out: &mut String) {
    match j {
        Json::Null => out.push_str("null"),
        Json::Bool(b) => out.push_str(if *b { "true" } else { "false" }),
        Json::Num(x) => out.push_str(&fmt_f(*x)),
        Json::Int(i) => out.push_str(&i.to_string()),
        Json::Str(s) => esc(s, out),
        Json::Arr(v) => {
            if v.is_empty() {
                out.push_str("[]");
            } else if v.iter().all(is_scalar) && v.len() <= 64 {
                out.push('[');
                for (i, x) in v.iter().enumerate() {
                    if i > 0 {
                        out.push_str(", ");
                    }
                    write(x, ind, out);
                }
                out.push(']');
            } else {
                out.push_str("[\n");
                for (i, x) in v.iter().enumerate() {
                    out.push_str(&" ".repeat(ind + 2));
                    write(x, ind + 2, out);
                    if i + 1 < v.len() {
                        out.push(',');
                    }
                    out.push('\n');
                }
                out.push_str(&" ".repeat(ind));
                out.push(']');
            }
        }
        Json::Obj(v) => {
            if v.is_empty() {
                out.push_str("{}");
            } else {
                out.push_str("{\n");
                for (i, (k, x)) in v.iter().enumerate() {
                    out.push_str(&" ".repeat(ind + 2));
                    esc(k, out);
                    out.push_str(": ");
                    write(x, ind + 2, out);
                    if i + 1 < v.len() {
                        out.push(',');
                    }
                    out.push('\n');
                }
                out.push_str(&" ".repeat(ind));
                out.push('}');
            }
        }
    }
}

pub fn to_pretty(j: &Json) -> String {
    let mut s = String::new();
    write(j, 0, &mut s);
    s.push('\n');
    s
}

struct Parser<'a> {
    b: &'a [u8],
    i: usize,
}

impl<'a> Parser<'a> {
    fn ws(&mut self) {
        while self.i < self.b.len() && matches!(self.b[self.i], b' ' | b'\n' | b'\r' | b'\t') {
            self.i += 1;
        }
    }
    fn err<T>(&self, m: &str) -> Result<T, String> {
        Err(format!("json: {} at byte {}", m, self.i))
    }
    fn value(&mut self) -> Result<Json, String> {
        self.ws();
        if self.i >= self.b.len() {
            return self.err("unexpected end");
        }
        match self.b[self.i] {
            b'{' => {
                self.i += 1;
                let mut v = Vec::new();
                self.ws();
                if self.i < self.b.len() && self.b[self.i] == b'}' {
                    self.i += 1;
                    return Ok(Json::Obj(v));
                }
                loop {
                    self.ws();
                    let k = match self.value()? {
                        Json::Str(s) => s,
                        _ => return self.err("object key"),
                    };
                    self.ws();
                    if self.i >= self.b.len() || self.b[self.i] != b':' {
                        return self.err("expected :");
                    }
                    self.i += 1;
                    let x = self.value()?;
                    v.push((k, x));
                    self.ws();
                    if self.i < self.b.len() && self.b[self.i] == b',' {
                        self.i += 1;
                        continue;
                    }
                    if self.i < self.b.len() && self.b[self.i] == b'}' {
                        self.i += 1;
                        return Ok(Json::Obj(v));
                    }
                    return self.err("expected , or }");
                }
            }
            b'[' => {
                self.i += 1;
                let mut v = Vec::new();
                self.ws();
                if self.i < self.b.len() && self.b[self.i] == b']' {
                    self.i += 1;
                    return Ok(Json::Arr(v));
                }
                loop {
                    v.push(self.value()?);
                    self.ws();
                    if self.i < self.b.len() && self.b[self.i] == b',' {
                        self.i += 1;
                        continue;
                    }
                    if self.i < self.b.len() && self.b[self.i] == b']' {
                        self.i += 1;
                        return Ok(Json::Arr(v));
                    }
                    return self.err("expected , or ]");
                }
            }
            b'"' => {
                self.i += 1;
                let mut s = String::new();
                loop {
                    if self.i >= self.b.len() {
                        return self.err("unterminated string");
                    }
                    let c = self.b[self.i];
                    if c == b'"' {
                        self.i += 1;
                        return Ok(Json::Str(s));
                    }
                    if c == b'\\' {
                        self.i += 1;
                        let e = self.b[self.i];
                        self.i += 1;
                        match e {
                            b'"' => s.push('"'),
                            b'\\' => s.push('\\'),
                            b'/' => s.push('/'),
                            b'n' => s.push('\n'),
                            b't' => s.push('\t'),
                            b'r' => s.push('\r'),
                            b'b' => s.push('\u{8}'),
                            b'f' => s.push('\u{c}'),
                            b'u' => {
                                let h = std::str::from_utf8(&self.b[self.i..self.i + 4]).map_err(|e| e.to_string())?;
                                let cp = u32::from_str_radix(h, 16).map_err(|e| e.to_string())?;
                                self.i += 4;
                                s.push(char::from_u32(cp).unwrap_or('?'));
                            }
                            _ => return self.err("bad escape"),
                        }
                    } else {
                        // copy one UTF-8 character
                        let start = self.i;
                        let len = if c < 0x80 {
                            1
                        } else if c >> 5 == 0b110 {
                            2
                        } else if c >> 4 == 0b1110 {
                            3
                        } else {
                            4
                        };
                        self.i += len;
                        s.push_str(std::str::from_utf8(&self.b[start..self.i]).map_err(|e| e.to_string())?);
                    }
                }
            }
            b't' if self.b[self.i..].starts_with(b"true") => {
                self.i += 4;
                Ok(Json::Bool(true))
            }
            b'f' if self.b[self.i..].starts_with(b"false") => {
                self.i += 5;
                Ok(Json::Bool(false))
            }
            b'n' if self.b[self.i..].starts_with(b"null") => {
                self.i += 4;
                Ok(Json::Null)
            }
            _ => {
                let start = self.i;
                while self.i < self.b.len() && matches!(self.b[self.i], b'-' | b'+' | b'.' | b'e' | b'E' | b'0'..=b'9') {
                    self.i += 1;
                }
                let t = std::str::from_utf8(&self.b[start..self.i]).map_err(|e| e.to_string())?;
                if t.is_empty() {
                    return self.err("unexpected character");
                }
                if !t.contains(['.', 'e', 'E']) {
                    if let Ok(i) = t.parse::<i64>() {
                        return Ok(Json::Int(i));
                    }
                }
                t.parse::<f64>().map(Json::Num).map_err(|e| format!("json number {}: {}", t, e))
            }
        }
    }
}

pub fn parse(s: &str) -> Result<Json, String> {
    let mut p = Parser { b: s.as_bytes(), i: 0 };
    let v = p.value()?;
    p.ws();
    if p.i != p.b.len() {
        return p.err("trailing characters");
    }
    Ok(v)
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn roundtrip() {
        let j = obj(vec![("a", 1.5.into()), ("b", Json::Arr(vec![1i64.into(), "x\"y".into()])), ("c", Json::Null)]);
        let s = to_pretty(&j);
        let k = parse(&s).unwrap();
        assert_eq!(k.get("a").unwrap().as_f64().unwrap(), 1.5);
        assert_eq!(k.get("b").unwrap().as_arr().unwrap()[1].as_str().unwrap(), "x\"y");
        assert_eq!(to_pretty(&k), s);
    }
}
