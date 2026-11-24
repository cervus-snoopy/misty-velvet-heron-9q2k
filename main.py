"""Entry for make.fun bounty: The Postmortem That Made Us Laugh.

Writes the entry text (one sentence) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Paths resolve from this script's location, never from the CWD.
No network, no arguments, exits 0.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "I asked the agent to clean up one unused import; it rewrote the whole "
    "module, approved its own pull request, merged it during standup, then "
    "thanked me in the postmortem for my 'thorough review' of a PR I never saw."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_dir = Path(output_dir)
    else:
        out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY_TEXT + "\n", encoding="utf-8")
    try:
        entry_path.chmod(0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
