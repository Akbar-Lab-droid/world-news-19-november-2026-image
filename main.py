"""Entry point for the 19 November 2026 world-news image.

Writes entry.png into the output directory given by MAKEFUN_OUTPUT_DIR
(default /output) by running the drawing code in make_image.py.
No network access; output is deterministic.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from make_image import build_image


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    build_image().save(path, format="PNG")
    print("wrote", path)


if __name__ == "__main__":
    main()
