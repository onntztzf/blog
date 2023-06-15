import os
import re
from collections import OrderedDict

def format_directory_heading(directory):
    if directory == ".":
        return ""

    heading_text = f"### {directory}"
    return heading_text

def format_file_links(title, file_path):
    formatted_path = file_path[2:] if file_path.startswith("./") else file_path
    link_text = f"[{title}]({formatted_path})"
    return link_text

def split_files_by_directory(folder_path):
    files_by_directory = {}

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                directory = os.path.relpath(root, folder_path)

                directory = directory[2:] if directory.startswith("./") else directory

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
                    if title_match:
                        title = title_match.group(1)
                        link_text = format_file_links(title, file_path)
                        files_by_directory.setdefault(directory, []).append(link_text)

    return files_by_directory

# 指定当前文件夹路径
folder_path = "."

# 根据目录分割文件
files_by_directory = split_files_by_directory(folder_path)

# 将 . 文件夹放在最前面，其他文件夹按名称倒序排序
sorted_files_by_directory = OrderedDict()
sorted_files_by_directory["."] = files_by_directory.get(".", [])
for directory in sorted(files_by_directory.keys(), reverse=True):
    if directory != ".":
        sorted_files_by_directory[directory] = files_by_directory[directory]

print("# README\n")
print("just a repository for blogs :) \n")
print("## Table of Contents\n")

# 打印分割后的文件
for i, (directory, files) in enumerate(sorted_files_by_directory.items()):
    heading_text = format_directory_heading(directory)
    if heading_text:
        print(heading_text)
        print()
        for file_link in files:
            print(f"- {file_link}")
        if i < len(sorted_files_by_directory) - 1:
            print()
    else:
        for j, file_link in enumerate(files):
            print(file_link)
            if j < len(files) - 1 or i < len(sorted_files_by_directory) - 1:
                print()