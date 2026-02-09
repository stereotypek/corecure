import os
import re

ROOT = "docs"

for subdir, _, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(subdir, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            def repl(match):
                target = match.group(1).replace(" ", "-").lower()  # sanitize path
                display = match.group(2) if match.group(2) else os.path.basename(target)
                # compute relative path
                rel = os.path.relpath(os.path.join(ROOT, target + ".md"), start=subdir)
                return f"[{display}]({rel.replace(os.sep, '/')})"

            text = re.sub(r"\[([^\]]*?)\]\(/(.*?)(?:\.md)?\)", repl, text)
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)

