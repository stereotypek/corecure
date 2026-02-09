import os
import re

DOCS_ROOT = "docs"

for subdir, _, files in os.walk(DOCS_ROOT):
    for file in files:
        if file.endswith(".md"):
            current_path = os.path.join(subdir, file)
            with open(current_path, "r", encoding="utf-8") as f:
                content = f.read()

            def repl(match):
                target_path = match.group(1).lstrip("/")  # remove leading slash
                abs_target = os.path.join(DOCS_ROOT, target_path)
                rel_target = os.path.relpath(abs_target, start=subdir)
                return f"({rel_target.replace(os.sep,'/')})"

            content = re.sub(r"\((/[^)]+)\)", repl, content)
            
            with open(current_path, "w", encoding="utf-8") as f:
                f.write(content)
