import os

DOCS_ROOT = "docs"

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    in_code_block = False

    for i, line in enumerate(lines):
        stripped = line.rstrip()

        # Detect code block start/end
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue

        # Don't modify lines inside code blocks
        if in_code_block:
            new_lines.append(line)
            continue

        # Preserve list items (starting with - , *, or numbers)
        if stripped.startswith(("-", "*")) or stripped[:2].isdigit() and stripped[2] == ".":
            new_lines.append(line)
            continue

        # Add an empty line after a non-empty line
        if stripped != "":
            new_lines.append(line)
            # Only add a blank line if the next line isn't already blank
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                new_lines.append("\n")
        else:
            # Already a blank line
            new_lines.append(line)

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"Processed: {path}")

# Walk all Markdown files
for root, _, files in os.walk(DOCS_ROOT):
    for file in files:
        if file.endswith(".md"):
            process_file(os.path.join(root, file))

print("All Markdown files processed. Empty lines added between paragraphs.")
