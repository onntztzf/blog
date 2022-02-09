# 忽略所有仓库中的 .DS\_Store 文件

1. 创建 `~/.gitignore_global` 文件

   这个文件中的内容要遵循 `gitignore` 的编写规范，[这篇文章](https://www.cnblogs.com/kevingrace/p/5690241.html)提供了很多忽略规则的写法，有兴趣可以看一看。

2. 将 `**/.DS_Store` 写入 `~/.gitignore_global`
3. 将上面创建的 `~/.gitignore_global` 指定为全局的忽略规则文件

   ```powershell
    git config --global core.excludesfile ~/.gitignore_global
   ```
