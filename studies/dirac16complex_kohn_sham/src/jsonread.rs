//! Minimal JSON reader (RFC 8259 subset sufficient for the theory files of
//! this repository): objects (insertion order kept), arrays, strings with
//! escapes, numbers as f64, true/false/null.  No dependencies.

#[derive(Clone, Debug, PartialEq)]
pub enum Value {
    Null,
    Bool(bool),
    Number(f64),
    Str(String),
    Array(Vec<Value>),
    Object(Vec<(String, Value)>),
}

impl Value {
    pub fn get(&self, key: &str) -> Option<&Value> {
        match self {
            Value::Object(pairs) => pairs.iter().find(|(k, _)| k == key).map(|(_, v)| v),
            _ => None,
        }
    }

    /// Follow a path of keys / indices ("a", "b", "3").
    pub fn path(&self, keys: &[&str]) -> Option<&Value> {
        let mut current = self;
        for key in keys {
            current = match current {
                Value::Object(_) => current.get(key)?,
                Value::Array(items) => items.get(key.parse::<usize>().ok()?)?,
                _ => return None,
            };
        }
        Some(current)
    }

    pub fn as_str(&self) -> Option<&str> {
        match self {
            Value::Str(s) => Some(s),
            _ => None,
        }
    }

    pub fn as_array(&self) -> Option<&Vec<Value>> {
        match self {
            Value::Array(items) => Some(items),
            _ => None,
        }
    }

    /// A number given either as a JSON number or as a rational string "n" / "n/d".
    pub fn as_rational(&self) -> Option<f64> {
        match self {
            Value::Number(x) => Some(*x),
            Value::Str(s) => parse_rational(s),
            _ => None,
        }
    }
}

/// "n", "-n", "n/d" (also a plain decimal) to f64.
pub fn parse_rational(text: &str) -> Option<f64> {
    let text = text.trim();
    if let Some((num, den)) = text.split_once('/') {
        let n: f64 = num.trim().parse().ok()?;
        let d: f64 = den.trim().parse().ok()?;
        if d == 0.0 {
            return None;
        }
        Some(n / d)
    } else {
        text.parse().ok()
    }
}

struct Parser<'a> {
    bytes: &'a [u8],
    pos: usize,
}

impl<'a> Parser<'a> {
    fn skip_ws(&mut self) {
        while self.pos < self.bytes.len()
            && matches!(self.bytes[self.pos], b' ' | b'\t' | b'\n' | b'\r')
        {
            self.pos += 1;
        }
    }

    fn expect(&mut self, ch: u8) -> Result<(), String> {
        self.skip_ws();
        if self.pos < self.bytes.len() && self.bytes[self.pos] == ch {
            self.pos += 1;
            Ok(())
        } else {
            Err(format!(
                "json: expected '{}' at byte {}",
                ch as char, self.pos
            ))
        }
    }

    fn value(&mut self) -> Result<Value, String> {
        self.skip_ws();
        let Some(&c) = self.bytes.get(self.pos) else {
            return Err("json: unexpected end".to_string());
        };
        match c {
            b'{' => {
                self.pos += 1;
                let mut pairs = Vec::new();
                self.skip_ws();
                if self.bytes.get(self.pos) == Some(&b'}') {
                    self.pos += 1;
                    return Ok(Value::Object(pairs));
                }
                loop {
                    self.skip_ws();
                    let key = self.string()?;
                    self.expect(b':')?;
                    let value = self.value()?;
                    pairs.push((key, value));
                    self.skip_ws();
                    match self.bytes.get(self.pos) {
                        Some(b',') => self.pos += 1,
                        Some(b'}') => {
                            self.pos += 1;
                            return Ok(Value::Object(pairs));
                        }
                        _ => return Err(format!("json: bad object at byte {}", self.pos)),
                    }
                }
            }
            b'[' => {
                self.pos += 1;
                let mut items = Vec::new();
                self.skip_ws();
                if self.bytes.get(self.pos) == Some(&b']') {
                    self.pos += 1;
                    return Ok(Value::Array(items));
                }
                loop {
                    items.push(self.value()?);
                    self.skip_ws();
                    match self.bytes.get(self.pos) {
                        Some(b',') => self.pos += 1,
                        Some(b']') => {
                            self.pos += 1;
                            return Ok(Value::Array(items));
                        }
                        _ => return Err(format!("json: bad array at byte {}", self.pos)),
                    }
                }
            }
            b'"' => Ok(Value::Str(self.string()?)),
            b't' => self.literal("true", Value::Bool(true)),
            b'f' => self.literal("false", Value::Bool(false)),
            b'n' => self.literal("null", Value::Null),
            _ => self.number(),
        }
    }

    fn literal(&mut self, word: &str, value: Value) -> Result<Value, String> {
        if self.bytes[self.pos..].starts_with(word.as_bytes()) {
            self.pos += word.len();
            Ok(value)
        } else {
            Err(format!("json: bad literal at byte {}", self.pos))
        }
    }

    fn number(&mut self) -> Result<Value, String> {
        let start = self.pos;
        while self.pos < self.bytes.len()
            && matches!(
                self.bytes[self.pos],
                b'-' | b'+' | b'.' | b'e' | b'E' | b'0'..=b'9'
            )
        {
            self.pos += 1;
        }
        let text = std::str::from_utf8(&self.bytes[start..self.pos]).map_err(|e| e.to_string())?;
        text.parse::<f64>()
            .map(Value::Number)
            .map_err(|_| format!("json: bad number '{text}' at byte {start}"))
    }

    fn string(&mut self) -> Result<String, String> {
        if self.bytes.get(self.pos) != Some(&b'"') {
            return Err(format!("json: expected string at byte {}", self.pos));
        }
        self.pos += 1;
        let mut out: Vec<u8> = Vec::new();
        while self.pos < self.bytes.len() {
            let c = self.bytes[self.pos];
            self.pos += 1;
            match c {
                b'"' => return String::from_utf8(out).map_err(|e| e.to_string()),
                b'\\' => {
                    let e = *self.bytes.get(self.pos).ok_or("json: bad escape")?;
                    self.pos += 1;
                    match e {
                        b'"' => out.push(b'"'),
                        b'\\' => out.push(b'\\'),
                        b'/' => out.push(b'/'),
                        b'b' => out.push(8),
                        b'f' => out.push(12),
                        b'n' => out.push(b'\n'),
                        b'r' => out.push(b'\r'),
                        b't' => out.push(b'\t'),
                        b'u' => {
                            let hex = std::str::from_utf8(
                                self.bytes
                                    .get(self.pos..self.pos + 4)
                                    .ok_or("json: bad \\u")?,
                            )
                            .map_err(|e| e.to_string())?;
                            let code = u32::from_str_radix(hex, 16).map_err(|e| e.to_string())?;
                            self.pos += 4;
                            let ch = char::from_u32(code).unwrap_or('\u{fffd}');
                            let mut buffer = [0u8; 4];
                            out.extend_from_slice(ch.encode_utf8(&mut buffer).as_bytes());
                        }
                        _ => return Err(format!("json: bad escape at byte {}", self.pos)),
                    }
                }
                _ => out.push(c),
            }
        }
        Err("json: unterminated string".to_string())
    }
}

/// Parse a JSON document.
pub fn parse(text: &str) -> Result<Value, String> {
    let mut parser = Parser {
        bytes: text.as_bytes(),
        pos: 0,
    };
    let value = parser.value()?;
    parser.skip_ws();
    if parser.pos != parser.bytes.len() {
        return Err(format!("json: trailing data at byte {}", parser.pos));
    }
    Ok(value)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parses_nested_documents_and_rationals() {
        let doc =
            parse(r#"{"a": [1, -2.5e1, "3/4", {"b": true, "c": null}], "s": "x\"yé"}"#).unwrap();
        assert_eq!(doc.path(&["a", "1"]).unwrap().as_rational(), Some(-25.0));
        assert_eq!(doc.path(&["a", "2"]).unwrap().as_rational(), Some(0.75));
        assert_eq!(doc.path(&["a", "3", "b"]), Some(&Value::Bool(true)));
        assert_eq!(doc.get("s").unwrap().as_str(), Some("x\"y\u{e9}"));
        assert!(parse("[1,").is_err());
        assert_eq!(parse_rational("-7/2"), Some(-3.5));
    }
}
