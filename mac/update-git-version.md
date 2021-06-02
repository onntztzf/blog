# Mac 升级 Git 版本

**不吹牛的说，这篇文章绝对是目前网上最简单的 `Git` 升级教程了**

## 安装 Homebrew

[Homebrew](https://brew.sh/) 是一个软件包管理器。它的作用就是将软件包安装到自己的目录中，然后将其文件符号链接到 `/usr/local`。更多信息，请自行进入官网查看。

在将下面代码复制进终端，点击回车，然后打开零食，边吃边等就好。

```text
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

## 升级 git

1. 安装最新版的 `git`

   ```text
    brew install git
   ```

   当看到下面输出时，说明 `git` 已经安装完成：

   ```text
    Already downloaded: /Users/zhangpeng/Library/Caches/Homebrew/downloads/c5f94c257b885992f680bbe3c2b8ec009e8856aefebac2cc1fb6608d7f006152--git-2.20.1.mojave.bottle.2.tar.gz
    ==> Pouring git-2.20.1.mojave.bottle.2.tar.gz
    ==> Caveats
    Bash completion has been installed to:
        /usr/local/etc/bash_completion.d

    zsh completions and functions have been installed to:
        /usr/local/share/zsh/site-functions

    Emacs Lisp files have been installed to:
        /usr/local/share/emacs/site-lisp/git
    ==> Summary
    🍺  /usr/local/Cellar/git/2.20.1: 1,528 files, 41.3MB
   ```

2. 改变默认 `Git` 指向

   在终端中查看我们的 `git` 指向和版本信息。

   ```text
    ➜  ~ which git
    /usr/bin/git
    ➜  ~ git --version
    git version 2.17.2 (Apple Git-113)
   ```

   接下来我们通过 `brew link` 将 `git` 指向我们通过 `Homebrew` 安装的 `git`

   ```text
    ➜  ~ brew link git --overwrite
    Warning: Already linked: /usr/local/Cellar/git/2.20.1
    To relink: brew unlink git && brew link git
   ```

   link 成功后，退出终端后，再次打开。然后查看 `git` 指向和版本信息。

   ```text
    ➜  ~ which git
    /usr/local/bin/git
    ➜  ~ git --version
    git version 2.20.1
   ```

   可以看到，我们的 `git` 版本已经升级到最新版了。

> Title: Mac 升级 Git 版本
>
> Date: 2019.01.16
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)

