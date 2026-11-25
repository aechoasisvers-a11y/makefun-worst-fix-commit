import os

ENTRY = "fix: patch the leak by deleting memory; app now forgets everything, including the fix"


def _check(line):
    if not (1 <= len(line) <= 100):
        raise SystemExit("gate FAIL: length %d not in 1-100" % len(line))
    if not line.strip():
        raise SystemExit("gate FAIL: line is only whitespace")


def main():
    _check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    _check(ENTRY)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit("gate FAIL: read-back bytes differ from entry")
    if back.endswith(b"\n"):
        raise SystemExit("gate FAIL: trailing newline present")
    if back.decode("utf-8") != ENTRY:
        raise SystemExit("gate FAIL: read-back text differs from entry")
    print("verified: %r" % ENTRY)
    print("gate PASS: %d chars written to %s" % (len(ENTRY), path))


if __name__ == "__main__":
    main()
