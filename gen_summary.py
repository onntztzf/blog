import re
from pathlib import Path
import subprocess


def format_directory_heading(directory):
    """
    Format the directory heading by converting it to a string.
    If the directory is the current directory ('.'), return an empty string.
    """
    return str(directory) if directory != "." else ""


def format_file_link(file_path):
    """
    Format the file link and return a Markdown-formatted file link.
    If the file path starts with './', remove the leading './'.
    """
    formatted_path = (
        str(file_path)[2:] if file_path.name.startswith("./") else str(file_path)
    )
    return formatted_path


def get_file_commits(file_path):
    """
    Retrieve the commit history for a given file path using git log.
    Return a list of commit timestamps.
    """
    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "--format=%cd",
                "--date=format-local:%Y-%m-%d %H:%M:%S",
                str(file_path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip().splitlines()
    except subprocess.CalledProcessError:
        return []


def group_files_by_directory(folder_path: str):
    """
    Split the files in the specified folder by directory.
    Return a dictionary with directory names as keys and corresponding file lists as values.
    """
    files_by_directory = {}

    for file_path in Path(folder_path).rglob("*.md"):
        directory = file_path.parent.relative_to(folder_path).as_posix()
        files_by_directory.setdefault(directory, []).append(file_path)

    return files_by_directory


folder_path = "."


files_by_directory = group_files_by_directory(folder_path)


formatted_files = []
for directory, files in files_by_directory.items():
    for file_path in files:
        commits = get_file_commits(file_path)
        first_commit_time = commits[-1] if commits else ""
        last_commit_time = commits[0] if commits else ""
        formatted_files.append(
            [directory, file_path, first_commit_time, last_commit_time]
        )


sorted_files = sorted(
    formatted_files, key=lambda x: (x[0] == ".", x[0].lower(), x[2]), reverse=True
)

output = "# SUMMARY\n\n"

excluded_files = ["SUMMARY.md"]

directories = []
directory2Files = {}
for directory, file_path, first_commit_time, last_commit_time in sorted_files:
    # Skip output for excluded files
    if str(file_path) in excluded_files:
        continue

    if directory not in directory2Files:
        directories.append(directory)

    file_link = format_file_link(file_path)
    title = ""
    try:
        with file_path.open() as f:
            content = f.read()
            title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
    except IOError:
        pass
    directory2Files.setdefault(directory, []).append(
        {
            "file_link": format_file_link(file_path),
            "title": title,
        }
    )

for directory, files in directory2Files.items():
    heading_text = format_directory_heading(directory)
    if heading_text:
        output += f"- [{heading_text}]({directory})\n"
        for file in files:
            output += f"  - [{file['title']}]({file['file_link']})\n"
        output += "\n"
    else:
        for file in files:
            output += f"[{file['title']}]({file['file_link']})\n\n"

print(output.strip())
