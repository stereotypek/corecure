
import os
import re

DOCS_ROOT = "docs"

def fix_link(current_file, target_path):
    # Remove vault prefix
    target_path = target_path.replace("/", "")

    # Build absolute target path
    absolute_target = os.path.join(DOCS_ROOT, target_path)

    # Compute relative path from current file's folder
    relative = os.path.relpath(absolute_target, start=os.path.dirname(current_file))

    return relative.replace(os.sep, "/")

for subdir, _, files in os.walk(DOCS_ROOT):
    for file in files:
        if file.endswith(".md"):
            current_path = os.path.join(subdir, file)

            with open(current_path, "r", encoding="utf-8") as f:
                content = f.read()

            def replacer(match):
                text = match.group(1)
                target = match.group(2)
                new_path = fix_link(current_path, target)
                return f"[{text}]({new_path})"

            new_content = re.sub(
                r"\[([^\]]+)\]\((/[^)]+)\)",
                replacer,
                content
            )

            with open(current_path, "w", encoding="utf-8") as f:
                f.write(new_content)

print("All links fixed.")
