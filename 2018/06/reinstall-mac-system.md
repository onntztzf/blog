# macOS 系统重装

## 为什么要重装系统

### 无用的东西太多，忍不了了

在日常工作中，我们难免要安装各式各样的软件，插件，环境等，随着时间的推移，我们电脑中的东西越来越多，虽然不会引起卡顿，但是想想就觉得心里膈应，像我这种强迫症就会选择开始删。但是删的时候就很麻烦了，`App` 从 `Application` 文件夹中删除后，还会有些配置文件保留在电脑中，很难完全移除。而插件，环境等，删除的操作就更为麻烦。

最后的最后就会有一部分人选择重装系统，因为他也不确定是不是删了什么不应该删的东西。

### 步入了 Beta 版的坑，忍不了了

世上永远少不了想要第一个吃螃蟹的人，新版系统一发布，便毫不犹豫的进行了升级，在使用一段时间后，发现坑太多，就不想被这些坑折磨了。

但是苹果爸爸会这么容易让一个小白鼠跑掉吗？不存在的！

只有两条路可以选择：

1. 等到更高版本的系统出现，进行升级

   需要在坑中再待一段时间，时间不确定。

2. 重装回低版本的系统

   **切记备份好所有的数据**，因为这种方案要抹掉磁盘，即一切从零开始。

## 重装系统的几种方式

系统重装有以下几种方式，文中以苹果最新的系统 `macOS High Sierra` 为例。

### 从 `App Store` 安装

两种获取系统镜像的方式：

1. 打开 `App Store`，搜索 `macOS High Sierra` 点击下载按钮
2. 直接打开 [macOS High Sierra](https://search.itunes.apple.com/WebObjects/MZContentLink.woa/wa/link?mt=11&path=mac%2fmacoshighsierra) 页面，点击下载按钮

下载完成后，安装器会自动打开，按照提示即可完成新系统的安装。

### 在线恢复

1. 进入 `macOS` 恢复模式。
    根据不同的目标，我们可以按不同的组合键。

    | 组合键                                                             | 目标                                                        |
    | :----------------------------------------------------------------- | :---------------------------------------------------------- |
    | Command + R                                                        | 安装您在 Mac 上安装过的最新 macOS，但不会升级到更高的版本。 |
    | Option + Command + R                                               | 升级到与您的 Mac 兼容的最新 macOS                           |
    | Shift-Option-Command-R（需要安装 macOS Sierra 10.12.4 或更高版本） | 安装 Mac 附带的 macOS 或最接近的仍可用版本。                |

2. 进入恢复模式后，我们可以看到下面四个功能：

    ![图片](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0d87aacfd674425a6a892f90e42f795~tplv-k3u1fbpfcp-zoom-1.image)

    选择重新安装 `macOS`，根据提示我们就可以完成新系统的安装了。

    1. 从 macOS 恢复功能的实用工具窗口中选择“磁盘工具”，然后点按“继续”。
    2. 在“磁盘工具”边栏中选择您的设备或宗卷。
    3. 点按“抹掉”按钮或标签页。
    4. 弹框中的东西一般不需要我们修改，直接点击弹框中“抹掉”以开始抹掉磁盘。
    5. 完成后，退出“磁盘工具”以回到实用工具窗口。

    **注：** 在系统安装之前，根据具体的情况，决定是否要通过磁盘工具抹掉磁盘。

### U 盘安装

1. 下载系统镜像 通过上面的方式，将我们需要的系统下载到电脑中，下载完成后，我们直接关闭安装界面，不要继续安装。这时我们可以在应用程序文件夹下看到我们刚刚下载的安装程序。
2. 通过终端创建 U 盘启动器
    1. 首先我们要确认我们刚刚下载的安装程序的位置以及优盘的名字。
    2. 假设安装程序仍位于“应用程序”文件夹中，并且 U 盘名称是 `MyVolume`。我们要在终端中使用 `createinstallmedia` 命令，输入命令后点击回车。

       ```text
        sudo /Applications/Install\ macOS\ High\ Sierra.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume --applicationpath /Applications/Install\ macOS\ High\ Sierra.app
       ```

    3. 然后输入密码，密码是不会显示出来的，输入后点击回车。
    4. 接下来按着终端中的提示即可完成启动盘的制作。
3. 使用 U 盘启动器安装新系统
    1. 将 U 盘查到电脑上
    2. 进入恢复模式，将启动磁盘改为我们制作的启动盘，启动盘的修改可以看考附件
    3. 从“实用工具”窗口中选择“安装 macOS”（或“安装 OS X”），然后点按“继续”，按照屏幕上的说明进行操作

## 参考资料

1. 苹果官方提供的 `macOS` 安装文档：[如何安装 macOS](https://support.apple.com/zh-cn/HT204904)
2. 目前 `macOS` 的版本列表：[macOS 版本列表](https://support.apple.com/zh-cn/HT201686)
3. 通过 `App Store` 安装 `macOS High Sierra`：[如何下载安装 macOS High Sierra](https://support.apple.com/zh-cn/HT201475#appstore)
4. `macOS` U 盘启动盘制作教程：[如何创建可引导的 macOS 安装器](https://support.apple.com/zh-cn/HT201372)
5. 通过恢复模式安装新系统：[macOS 恢复模式](https://support.apple.com/zh-cn/HT201314)
6. 两台 `Mac` 电脑间的数据迁移方法：[如何将内容移至新 Mac](https://support.apple.com/zh-cn/HT204350)
7. 如何修改启动盘：[如何选择其他启动磁盘](https://support.apple.com/zh-cn/HT202796)

> Title: Mac 系统重装
>
> Date: 2018.06.16
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onnttf](https://github.com/onnttf)
