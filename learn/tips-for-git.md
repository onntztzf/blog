# Git 的日常使用

## Git 的配置级别

1. 系统级别 system **【优先级最低】**

    首先会查找 `/etc/gitconfig` 文件（系统级），该文件含有对系统上所有用户及他们所拥有的仓库都生效的配置值。

2. 用户级别 global **【优先级次之】**

    接下来会查找每个用户的 `~/.gitconfig` 文件（用户级），该文件含有当前用户所拥有的仓库都生效的配置值。

3. 仓库级别 local **【优先级最高】**

    最后会查找由用户定义的各个仓库中的配置文件 `.git/config`（仓库级），该文件中的值只对当前所属仓库有效。

## 显示与编辑 Git 配置

- 显示 `Git` 配置

    ```shell
    git config -l [--local|--global|--system]
    ```

- 编辑 Git 配置

    ```shell
    git config -e [--local|--global|--system]
    ```

## 设置用户信息

```shell
git config [--local|--global|--system] user.name "您的名字"
git config [--local|--global|--system] user.email "您的邮箱"
```

## 忽略所有仓库中的 .DS_Store 文件

1. 创建 `~/.gitignore_global` 文件

    这个文件中的内容要遵循 `gitignore` 的编写规范，[这篇文章](https://www.cnblogs.com/kevingrace/p/5690241.html)提供了很多忽略规则的写法，有兴趣可以看一看。

2. 将 `**/.DS_Store` 写入 `~/.gitignore_global`
3. 将上面创建的 `~/.gitignore_global` 指定为全局的忽略规则文件

    ```shell
    git config --global core.excludesfile ~/.gitignore_global
    ```

---

> Title: Git 的日常使用
>
> Date: 2020.10.05
>
> Author: zhangpeng
>
> Github: <https://github.com/gh-zhangpeng>
