import os
import re

DOCS_ROOT = "docs"

# Pattern to detect any Markdown image link ![alt](path)
image_pattern = re.compile(r'!\[.*?\]\(.*?\)')

# Pattern to detect the dg-publish JSON metadata
dg_publish_pattern = re.compile(r'\{"dg-publish".*?\}')

for root, _, files in os.walk(DOCS_ROOT):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                stripped = line.strip()
                # Remove line if it contains an image link
                if image_pattern.search(stripped):
                    continue
                # Remove line if it contains dg-publish metadata
                if dg_publish_pattern.search(stripped):
                    continue
                new_lines.append(line)

            with open(path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

print("All Markdown image lines and dg-publish metadata removed.")
