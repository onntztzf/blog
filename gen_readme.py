import re
from collections import OrderedDict
from pathlib import Path
import subprocess


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
        str(file_path)[2:] if file_path.name.startswith("./") else str(file_path)
    )
    return f"[{title}]({formatted_path})"


def get_file_last_commit_time(file_path):
    """
    Get the last commit time of a file using Git.
    Return the last commit time in the format "YYYY-MM-DD HH:MM:SS".
    If there's an error or the file is not under version control, return an empty string.
    """
    try:
        output = subprocess.check_output(
            [
                "git",
                "log",
                "-1",
                "--format=%cd",
                "--date=format-local:%Y-%m-%d %H:%M:%S",
                str(file_path),
            ]
        )
        last_commit_time = output.decode("utf-8").strip()
        return last_commit_time
    except subprocess.CalledProcessError:
        return ""


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
                last_commit_time = get_file_last_commit_time(file_path)
                files_by_directory.setdefault(directory, []).append(
                    (link_text, last_commit_time)
                )

    return files_by_directory


# Specify the folder path
folder_path = "."

# Split the files by directory
files_by_directory = split_files_by_directory(folder_path)

# Place the '.' directory at the beginning, and sort other directories in reverse alphabetical order
sorted_files_by_directory = OrderedDict()
sorted_files_by_directory["."] = files_by_directory.pop(".", [])
sorted_files_by_directory.update(
    sorted(files_by_directory.items(), key=lambda x: x[0], reverse=True)
)

# Print the README header
print("# README\n")
print("Just a repository for blogs. :)\n")
print("## Table of Contents\n")

print("| Directory | File | Last Updated |")
print("| --- | --- | --- |")

# Print the split files
for directory, files in sorted_files_by_directory.items():
    heading_text = format_directory_heading(directory)
    for file_link, last_commit_time in files:
        print(f"| {heading_text} | {file_link} | {last_commit_time} |")

print()
print("如果觉得文章不错，可以关注公众号哟！\n")
print("![干货输出机](https://img.zhangpeng.site/wechat/qrcode.jpg)")
