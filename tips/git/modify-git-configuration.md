# 修改 git 配置

![git config](https://img.zhangpeng.site/2021/12/06/1.png)

在开始修改配置前，我们需要明确修改配置的目的是什么？是需要当前电脑的全部 `git` 仓库生效？还是只对某个 `git` 仓库生效？不同的目的需要修改的配置文件不一样。

## git 配置文件

我们常用的配置文件有两个：

1. **全局级别**的配置文件：`~/.gitconfig`
2. **仓库级别**的配置文件：`git` 仓库中的`.git/config`

除了上面这两个，还有两个不怎么常用的配置文件：

1. **系统级别**的配置文件：`/etc/gitconfig`
2. **工作区级别**的配置文件：`git` 仓库中的`.git/config.worktree`

这四个配置文件的优先级由高至低为：

工作区（`.git/config.worktree`） > 仓库（`.git/config`） > 用户（`~/.gitconfig`） > 系统（`/etc/gitconfig`）

## 修改 git 配置

### 可视化

使用文本编辑器（如 `Sublime Text`）打开配置文件，然后对需要修改的配置项进行修改即可。至于什么配置该如何修改，请参照 `git` 的[官方文档](https://git-scm.com/docs/git-config)

### 命令行

命令行修改 `git` 配置的命令如下：

```powershell
git config [--local|--global|--system] [key] [value]
```

举个例子，修改全局级别的用户信息：

```powershell
git config --global user.name "您的名字"
git config --global user.email "您的邮箱"
```

## 参考

1. [git-config - Get and set repository or global options](https://git-scm.com/docs/git-config)
2. [git-worktree - Manage multiple working trees](https://git-scm.com/docs/git-worktree)

##

![干货输出机](https://img.zhangpeng.site/wechat/qrcode.jpg)
