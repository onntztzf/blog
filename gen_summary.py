import re
from collections import OrderedDict
from pathlib import Path


def format_directory_heading(directory):
    """
    Format the directory heading by adding the Markdown format prefix '### '.
    If the directory is the current directory ('.'), return an empty string.
    """
    return f"{directory}" if directory != "." else ""


def format_file_links(title, file_path):
    """
    Format the file link and return a Markdown-formatted file link.
    If the file path starts with './', remove the leading './'.
    """
    formatted_path = (
        str(file_path)[2:] if str(file_path).startswith("./") else str(file_path)
    )
    return f"[{title}]({formatted_path})"


def split_files_by_directory(folder_path):
    """
    Split the files by directory.
    Return a dictionary with directory names as keys and corresponding file lists as values.
    """
    files_by_directory = {}

    for file_path in Path(folder_path).rglob("*.md"):
        directory = file_path.parent.relative_to(folder_path).as_posix()
        with file_path.open() as f:
            content = f.read()
            title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
                link_text = format_file_links(title, file_path)
                files_by_directory.setdefault(directory, []).append(link_text)

    return files_by_directory


# Specify the folder path
folder_path = "."

# Split the files by directory
files_by_directory = split_files_by_directory(folder_path)

# Place the '.' directory at the beginning, and sort other directories in reverse alphabetical order
sorted_files_by_directory = OrderedDict()
sorted_files_by_directory["."] = files_by_directory.get(".", [])
for directory in sorted(files_by_directory.keys(), reverse=True):
    if directory != ".":
        sorted_files_by_directory[directory] = files_by_directory[directory]

print("# SUMMARY\n")

# Print the split files
for i, (directory, files) in enumerate(sorted_files_by_directory.items()):
    heading_text = format_directory_heading(directory)
    if heading_text:
        print(f"- [{heading_text}]({directory})")
        for file_link in files:
            print(f"  - {file_link}")
        if i < len(sorted_files_by_directory) - 1:
            print()
    else:
        for j, file_link in enumerate(files):
            print(file_link)
            if j < len(files) - 1 or i < len(sorted_files_by_directory) - 1:
                print()
