"""The funniest toaster error message.

Writes one line to /output/entry.txt: the error message a kitchen
toaster shows its owner when something goes wrong. The joke lives in
the toaster treating the bagel and the lever as parties in a legal
dispute, in the flat voice of an appliance error code.
"""

from pathlib import Path

TEXT = "ERROR: This bagel has a restraining order against the lever."


# The competition accepts texts of 1 to 120 characters.
MIN_CHARS = 1
MAX_CHARS = 120


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
