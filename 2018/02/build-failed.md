# 常见的编译失败

## -fobjv-weak is not supported on the current deloyment target

![图片](https://file.zhangpeng.site/2018/02/09/1.jpg)

**解决方案：**
更新 `xcodeproj` 版本。

1. 通过终端进到项目目录
2. 查看 `xcodeproj` 版本

   ```text
    gem list xcodeproj
   ```

3. 安装 `xcodeproj` 最新版本 可以在 [rubygems.org](https://rubygems.org/gems/xcodeproj)查看到最新的版本，目前应该是 1.5.6。

   ```text
   gem install xcodeproj -v 1.5.6
   ```

4. 再次查看 `xcodeproj` 版本

   ```text
   gem list xcodeproj
   ```

5. 卸载旧版本的 `xcodeproj`

   ```text
   gem uninstall xcodeproj -v 1.5.6
   ```

按下 `command + b`，你会发现已经可以成功编译了！

> Title: 常见的编译失败
>
> Date: 2018.02.09
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onntztzf](https://github.com/onntztzf)
