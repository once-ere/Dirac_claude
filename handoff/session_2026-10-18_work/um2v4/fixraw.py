"""Convert non-raw string literals to raw literals with the intended text (single backslashes kept literally,
an escaped backslash becomes one backslash, an escaped quote becomes the quote)."""
import io, sys, tokenize

def intended(body):
    out, i = [], 0
    while i < len(body):
        c = body[i]
        if c == '\\' and i + 1 < len(body):
            n = body[i + 1]
            if n == '\\':
                out.append('\\'); i += 2; continue
            if n in "'\"":
                out.append(n); i += 2; continue
            out.append('\\' + n); i += 2; continue
        out.append(c); i += 1
    return ''.join(out)

def convert(src):
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    lines = src.split('\n')
    edits = []
    for t in toks:
        if t.type != tokenize.STRING:
            continue
        s = t.string
        prefix = ''
        while s[0] in 'rRbBuUfF':
            prefix += s[0]; s = s[1:]
        if 'r' in prefix.lower() or s.startswith(('"""', "'''")):
            continue
        q = s[0]
        body = intended(s[1:-1])
        if '\\' not in body:
            new = prefix + q + body.replace(q, '\\' + q) + q if q in body else None
            if new is None:
                continue
        else:
            nq = q
            if q in body:
                nq = '"' if q == "'" else "'"
                if nq in body:
                    raise SystemExit('both quotes in ' + s[:60])
            if body.endswith('\\'):
                raise SystemExit('trailing backslash in ' + s[:60])
            new = 'r' + prefix + nq + body + nq
        edits.append((t.start, t.end, new))
    for (sr, sc), (er, ec), new in reversed(edits):
        assert sr == er
        ln = lines[sr - 1]
        lines[sr - 1] = ln[:sc] + new + ln[ec:]
    return '\n'.join(lines)

for f in sys.argv[1:]:
    src = open(f).read()
    try:
        compile(src, f, 'exec')
    except SyntaxError as e:
        print('syntax error before conversion (expected for bad escapes):', f, e.msg)
    new = convert(src)
    compile(new, f, 'exec')
    open(f, 'w').write(new)
    print('converted', f)
