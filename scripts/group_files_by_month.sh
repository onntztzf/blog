#!/bin/bash

# 屏蔽的文件夹数组
excluded_folders=("draft" "temp" "backup")

# 检查文件夹是否需要被屏蔽
function is_excluded_folder() {
  local folder="$1"

  for excluded_folder in "${excluded_folders[@]}"; do
    if [[ "$folder" == "$excluded_folder" ]]; then
      return 0
    fi
  done

  return 1
}

# 递归遍历函数
function traverse_directory() {
  local dir="$1"

  # 遍历当前目录下的文件和目录
  for file in "$dir"/*; do
    if [ -f "$file" ] && [[ ! "$(basename "$file")" == .* ]]; then
      # 获取文件最后一次 Git 提交记录
      git_log=$(git log -n 1 --pretty=format:"%h %ad %s" -- "$file")
      if [ -n "$git_log" ]; then
        # 提取提交记录中的年份和月份
        year=$(git log -n 1 --pretty=format:"%ad" --date=format:"%Y" -- "$file")
        month=$(git log -n 1 --pretty=format:"%ad" --date=format:"%m" -- "$file")

        # 创建以年份/月份命名的文件夹
        folder="${year}/${month}"
        mkdir -p "$folder"

        # 移动文件到相应的文件夹，前提是不在屏蔽的文件夹中
        # if ! is_excluded_folder "$(dirname "$file")"; then
          mv "$file" "$folder/"
        # fi
      fi
    elif [ -d "$file" ] && [[ ! "$(basename "$file")" == .* ]]; then
        # echo "$(basename "$file")"
      # 递归遍历子目录，前提是不进入屏蔽的文件夹
      if ! is_excluded_folder "$(basename "$file")"; then
        echo "$file"
        traverse_directory "$file"
      fi
    fi
  done
}

# 调用遍历函数，传入当前目录
traverse_directory "."