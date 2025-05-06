#!/usr/bin/python3
import sys
import os


# Check if the correct number of arguments is provided
if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input Markdown file exists
if not os.path.exists(input_file):
    sys.stderr.write(f"Missing {input_file}\n")
    sys.exit(1)

# Read markdown content
with open(input_file, "r", encoding="utf-8") as md_file:
    markdown_content = md_file.read()

# Convert Markdown to HTML (basic conversion)
html_content = f"<html>\n<body>\n{markdown_content}\n</body>\n</html>"

# Write to the output HTML file
with open(output_file, "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

sys.exit(0)
