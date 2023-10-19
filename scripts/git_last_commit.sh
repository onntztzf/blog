#!/bin/bash

# 递归遍历函数
function traverse_directory() {
  local dir="$1"

  # 遍历当前目录下的文件和目录
  for file in "$dir"/*; do
    if [ -f "$file" ]; then
      # 获取文件最后一次 Git 提交记录
      git_log=$(git log -n 1 --pretty=format:"%h %ad %s" -- "$file")
      if [ -n "$git_log" ]; then
        echo "文件: $file"
        echo "最后一次提交: $git_log"
        echo
      fi
    elif [ -d "$file" ]; then
      # 递归遍历子目录
      traverse_directory "$file"
    fi
  done
}

# 调用遍历函数，传入当前目录
traverse_directory "."
