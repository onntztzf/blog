# iTerm2 一个更好用的终端

本文意图是给终端小白提供一个 **效(fang)率(bian)更(zhuang)高(bi)** 的终端使用方式。

## 安装 iTerm2

1. 下载[iTerm2](https://iterm2.com/downloads.html)
2. 进行常规安装

## 提(kai)高(shi)效(zhuang)率(bi)的方式

### 命令行工具 `oh-my-zsh`

- `oh-my-zsh` 是什么

    `oh-my-zsh`是一款社区驱动的命令行工具，正如它的主页上说的，`oh-my-zsh`是一种生活方式。它基于`zsh`命令行，提供了主题配置，插件机制，已经内置的便捷操作。给我们一种全新的方式使用命令行。
    `oh-my-zsh`这个名字听起来就很有意思，它是基于`zsh`命令行的一个扩展工具集，提供了丰富的扩展功能。
    `oh-my-zsh`只是一个对`zsh`命令行环境的配置包装框架，但它不提供命令行窗口，更不是一个独立的APP。
    详细介绍可以看它的主页[oh-my-zsh](https://ohmyz.sh/)。

- `oh-my-zsh` 怎么安装

    ```shell
    // Via curl
    sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
    // Via wget
    sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
    ```

- `oh-my-zsh` 个性化配置
  1. 更换自己喜欢主题，可以百度找配置也可以使用[官方提供的主题1](https://github.com/robbyrussell/oh-my-zsh/wiki/themes)、[官方提供的主题2](https://github.com/robbyrussell/oh-my-zsh/wiki/External-themes)
  2. 安装插件，通过安装插件使 `oh-my-zsh` 更加强大。[官方插件1](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins)、[官方插件2](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins-Overview)，我这边常用的有一下几个：
     1. `zsh-syntax-highlighting` - 命令高亮
     2. `z` - 快速跳转之前已经进入过的路径，会根据频率进行权重调整

### 命令高亮

命令行中的命令高亮是通过`zsh-syntax-highlighting`实现，安装 `zsh-syntax-highlighting`的方法有很多，具体可以查看 [Install zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)
如果您已经安装了`oh-my-zsh`，可以直接按照下面的步骤安装：

1. **将 zsh-syntax-highlighting 克隆到指定文件夹**

    ```shell
    // Clone this repository in 'oh-my-zsh's plugins directory
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    ```

2. **在`~/.zshrc`中的插件列表中添加插件**

    ```vim
    // Activate the plugin in `~/.zshrc`
    plugins=( [plugins...] zsh-syntax-highlighting)
    ```

3. **编译 `~/.zshrc` 后即可看到改变**

   ```shell
   // Source `~/.zshrc` to take changes into account
   source ~/.zshrc
   ```

### 让 iTerm2 变的色彩缤纷

让 `iTerm2` 是通过 [coreutils](https://blog.csdn.net/lengye7/article/details/80270379) 实现。

1. **安装 `coreutils`**

    ```shell
    // 通过brew安装 `coreutils`
    brew install xz coreutils
    ```

2. **生成颜色定义文件**

    ```shell
    // 生成颜色定义文件
    gdircolors --print-database > ~/.dir_colors
    ```

3. **打开 `~/.zshrc`，在您喜欢的位置添加下面代码**

    ```vim
    if brew list | grep coreutils > /dev/null ; then
    PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"
    alias ls='ls -F --show-control-chars --color=auto'
    eval `gdircolors -b $HOME/.dir_colors`
    fi
    ```

4. **编译一下 `~/.zshrc` 就可以看到效果了**

    ```shell
    // source ~/.zshrc
    source ~/.zshrc
    ```

## 附

1. [iTerm2](https://iterm2.com/)
2. [利用Oh-My-Zsh打造你的超级终端](https://blog.csdn.net/czg13548930186/article/details/72858289)
3. [让Mac OS X的终端多姿多彩](http://linfan.info/blog/2012/02/27/colorful-terminal-in-mac/)

---

> Title: iTerm2 一个更好用的终端
>
> Date: 2018.12.18
>
> Author: zhangpeng
>
> Github: <https://github.com/gh-zhangpeng>
