import json, sys
nb = json.load(open(sys.argv[1], encoding="utf-8"))
for c in nb["cells"]:
    if c["cell_type"] != "code":
        continue
    print(f"=== In [{c.get('execution_count')}]")
    for o in c.get("outputs", []):
        if "text" in o:
            print("".join(o["text"]).rstrip())
        elif "data" in o and "text/plain" in o["data"]:
            print("[data]", "".join(o["data"]["text/plain"])[:200])
