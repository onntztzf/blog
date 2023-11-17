# 上传应用时，卡在 Authenticating with the App Store

![图片](https://file.zhangpeng.site/2020/05/26/1.jpg)

本文主要解决的是在上传应用时，卡在 `Authenticating with the App Store...` 的问题。

## 问题分析

综合网上各种解决此问题的方案，我这边猜测卡住的原因如下：

在上传 ipa 时，需要使用很多内置的资源，而这些资源是需要下载的。因为某种原因（例如 GFW，或者个人网络原因）下载缓慢或失败，都会造成卡死在这一步。

## 解决方案

### 下载所需的文件

链接：[com.apple.amp.itmstransporter.zip](https://pan.baidu.com/s/19AEdaWU8gOiIvFOhe_hyJA) 提取码：vx8z

### 修改文件中的内容

找到 `obr/2.0.0/repository.xml` 这个文件。用文本编辑器打开，**切记一定要用文本编辑器之类的打开，不要直接双击用 Xcode 打开**，因为文件太大，Xcode 会崩溃。

在文件中搜索 zhangpeng，全部替换为你电脑登录的用户名。

### 替换文件

将 `~/Library/Caches` 文件中的 `com.apple.amp.itmstransporter` 完全删除。然后将上面的解压后的文件夹放入 `~/Library/Caches`，退出 Xcode 或 Transport，重新上传即可。

> Title: 上传应用时，卡在 Authenticating with the App Store
>
> Date: 2020.05.26
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onnttf](https://github.com/onnttf)
