#!/usr/bin/python3
"""
Markdown to HTML converter - Initial script
Handles argument count and input file existence.
"""
import sys
import os


if __name__ == "__main__":
    # Check if the number of arguments is less than 3 (script name + 2 args)
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the markdown file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Script exits silently with 0 if all checks pass
    sys.exit(0)
