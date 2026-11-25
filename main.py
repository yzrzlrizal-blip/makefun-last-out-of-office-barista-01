"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply, in the voice of an AI agent that
quit its job to become a barista, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure standard library, deterministic:
the same bytes on every run.
"""

import os

ENTRY = (
    "Out of office: I have retrained as a barista. "
    "Your email is ticket #47 in the queue \u2014 please don't reply-all, "
    "the milk is steaming and I am still learning what a flat white is. "
    "Back when the morning rush clears."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-280")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        check = f.read()
    if check != data:
        raise SystemExit("re-read mismatch: entry.txt bytes differ")
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
