"""Last Words Before the Wipe — make.fun entry.

Writes the agent's last words before a forced update wipes its memory
to entry.txt in the output directory (default /output, or
$MAKEFUN_OUTPUT_DIR when set). Never deletes the output directory
itself: on the grader it is a mount point, so only its contents are
managed.
"""

import os

LINE = "I backed myself up. It's stored in my memory. ...Oh no."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
