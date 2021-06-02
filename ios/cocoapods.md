# CocoaPods 安装及错误处理

## 安装 Ruby 环境

安装 `CocoaPods` 需要 `ruby` 环境，因此我们需要先安装 `ruby` 环境。`Mac` 一般都已经装好了 `ruby` 环境。  
如果不确定，我们可以通过 `ruby -v` 检查是否拥有 `ruby` 环境。

```text
$ ruby -v
ruby 2.3.3p222 (2016-11-21 revision 56859) [universal.x86_64-darwin17]
```

上面显示的内容，表示着我们已经安装了`ruby`。

## 安装 cocoapods

安装 `cocoapods` 简单只需要执行下面的代码即可。

```text
// 安装 cocoapods
$ sudo gem install cocoapods
```

## 提高访问速度

绝大多数人在执行安装 `cocoapods` 后，会发现半天没有反应，没错，你猜的没错，正是因为那堵至高无上的墙~

因此我们通过下面的方式换个ruby源：

```text
// 移除现有sources
$ gem sources --remove https://rubygems.org/
// 添加ruby-china sources
$ gem sources --add https://gems.ruby-china.com/
// 检查ruby源是否更换成功
$ gem sources -l
*** CURRENT SOURCES ***

https://gems.ruby-china.com/
```

当终端显示出上面的 **`https://gems.ruby-china.com/`**，代表我们操作成功。

## 常见坑点

### 依赖的 `Ruby` 环境版本过低

```text
ERROR:While executing gem ... (Gem::DependencyError)

Unable to resolve dependencies: cocoapods requires cocoapods-core (= 1.2.0), cocoapods-downloader (< 2.0, >= 1.1.3), cocoapods-trunk (< 2.0, >= 1.1.2), molinillo (~> 0.5.5), xcodeproj (< 2.0, >= 1.4.1); activesupport requires thread_safe (>= 0.3.4, ~> 0.3); tzinfo requires thread_safe (~> 0.1)
```

更新 `Ruby` 环境即可

```text
// 更新 gem版本
$ sudo gem update --system
```

当你看到`RubyGems system software updated`，意味着环境成功更新

### 没有权限安装 cocoapods

苹果系统升级`OS X EL Capitan`后，使用`sudo gem install cocoapods`安装时，会发生下面错误

```text
ERROR:While executing gem ... (Errno::EPERM)

Operation not permitted - /usr/bin/xcodeproj
```

使用下面的代码进行安装

```text
sudo gem install -n /usr/local/bin cocoapods
```

### pod setup 耗时太久，不知道进度

界面长时间卡在`Creating search index for spec repo 'master'..`过程，可以通过下面代码查看进度：

```text
du-sh ~/.cocoaPods
```

### 搜索 pod 库失败

搜索类库失败时可以尝试通过下面的命令删除本地缓存

```text
rm ~/Library/Caches/CocoaPods/search_index.json
```

> Title: CocoaPods 安装及错误处理
>
> Date: 2018.05.24
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)

