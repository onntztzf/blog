# 如何创建一个公有 Pod 库

**注意：** 文中使用 `{}` 包裹的位置都需要根据您自身情况进行设置。

如果您已经是 `COCOAPODS` 用户，请直接跳到第二节。

## 注册 `COCOAPODS` 用户

### 注册 Session

```text
$ pod trunk register {YOURMAIL} '{YOURNAME}' --verbose
opening connection to trunk.cocoapods.org:443...
opened
starting SSL for trunk.cocoapods.org:443...
SSL established, protocol: TLSv1.2, cipher: ECDHE-RSA-AES128-GCM-SHA256
<- "POST /api/v1/sessions HTTP/1.1\r\nContent-Type: application/json; charset=utf-8\r\nAccept: application/json; charset=utf-8\r\nUser-Agent: CocoaPods/1.7.2\r\nAccept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3\r\nHost: trunk.cocoapods.org\r\nContent-Length: 75\r\n\r\n"
<- "{\"email\":\"YOURMAIL\",\"name\":\"YOURNAME\",\"description\":null}"
-> "HTTP/1.1 201 Created\r\n"
-> "Date: Thu, 20 Jun 2019 14:17:48 GMT\r\n"
-> "Connection: keep-alive\r\n"
-> "Strict-Transport-Security: max-age=31536000\r\n"
-> "Content-Type: application/json\r\n"
-> "Content-Length: 192\r\n"
-> "X-Content-Type-Options: nosniff\r\n"
-> "Server: thin 1.6.2 codename Doc Brown\r\n"
-> "Via: 1.1 vegur\r\n"
-> "\r\n"
reading 192 bytes...
-> "{\"created_at\":\"2019-06-20 14:17:48 UTC\",\"valid_until\":\"2019-10-26 14:17:48 UTC\",\"verified\":false,\"created_from_ip\":\"223.104.3.12\",\"description\":null,\"token\":\"xxxxxxxxxx\"}"
read 192 bytes
Conn keep-alive
[!] Please verify the session by clicking the link in the verification email that has been sent to YOURMAIL
```

### 去邮箱点击验证链接

此时您的邮箱中应该有一封主题是 **[CocoaPods] Confirm your session.** 的邮件，点击邮件中的链接进行验证。

### 验证是否注册成功

下面内容，表示您已经注册成功。

```text
$ pod trunk me
  - Name:     YOURNAME
  - Email:    YOURMAIL
  - Since:    May 23rd, 2018 03:02
  - Pods:
    - PodName
  - Sessions:
    - June 20th, 08:17     -        October 26th, 08:39. IP: xxx.xxx.xxx.xxx
```

## 创建公有 Pod 库

### 创建一个 `Git` 仓库

创建过程请自行百度，谢谢！！！如果是在搜不到，那就私信我吧！😓

假设我们已经成功创建了一个仓库，关键信息如下：

* 仓库主页 进入您创建的仓库后，地址栏中的地址：[https://github.com/{YOURGITHUBNAME}/{YOURPODNAME}](https://github.com/{YOURGITHUBNAME}/{YOURPODNAME})
* git 地址 点击 **Clone or download** 按钮，就可以看到了。我们选择 `HTTPS` 地址，别问为什么，因为 `CocoaPods` 要求：[https://github.com/{YOURGITHUBNAME}/{YOURPODNAME}.git](https://github.com/{YOURGITHUBNAME}/{YOURPODNAME}.git)

### 创建 Pod 库

在终端中执行：`pod lib create {YOURPODNAME}`，接下来按照提示，根据自己的情况进行选择就可以了。

```text
$ pod lib create {YOURPODNAME}
Cloning `https://github.com/CocoaPods/pod-template.git` into `YOURPODNAME`.
Configuring YOURPODNAME template.
security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain.

------------------------------

To get you started we need to ask a few questions, this should only take a minute.

If this is your first time we recommend running through with the guide:
 - https://guides.cocoapods.org/making/using-pod-lib-create.html
 ( hold cmd and click links to open in a browser. )


What platform do you want to use?? [ iOS / macOS ]
 > {iOS}

What language do you want to use?? [ Swift / ObjC ]
 > {ObjC}

Would you like to include a demo application with your library? [ Yes / No ]
 > {Yes}

Which testing frameworks will you use? [ Specta / Kiwi / None ]
 > {None}

Would you like to do view based testing? [ Yes / No ]
 > {No}

What is your class prefix?
 > {Prefix}
security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain.
security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain.
security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain.
security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain.
security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain.
security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain.

Running pod install on your new library.

Analyzing dependencies
Fetching podspec for `YOURPODNAME` from `../`
Downloading dependencies
Installing YOURPODNAME (0.1.0)
Generating Pods project
Integrating client project

[!] Please close any current Xcode sessions and use `YOURPODNAME.xcworkspace` for this project from now on.
Sending stats
Pod installation complete! There is 1 dependency from the Podfile and 1 total pod installed.

 Ace! you're ready to go!
 We will start you off by opening your project in Xcode
  open 'YOURPODNAME/Example/YOURPODNAME.xcworkspace'

To learn more about the template see `https://github.com/CocoaPods/pod-template.git`.
To learn more about creating a new pod, see `https://guides.cocoapods.org/making/making-a-cocoapod`.
```

### 编辑 YOURPODNAME.podspec

```text
Pod::Spec.new do |s|
  s.name             = '{YOURPODNAME}'
  s.version          = '0.1.0'
  s.summary          = 'A short description of {YOURPODNAME}.'

# This description is used to generate tags and improve search results.
#   * Think: What does it do? Why did you write it? What is the focus?
#   * Try to keep it short, snappy and to the point.
#   * Write the description between the DESC delimiters below.
#   * Finally, don't worry about the indent, CocoaPods strips it!

  s.description      = <<-DESC
TODO: Add long description of the pod here.
                       DESC

  s.homepage         = 'https://github.com/{YOURGITHUBNAME}/{YOURPODNAME}'
  # s.screenshots     = 'www.example.com/screenshots_1', 'www.example.com/screenshots_2'
  s.license          = { :type => 'MIT', :file => 'LICENSE' }
  s.author           = { '{YOURNAME}' => '{YOURMAIL}' }
  s.source           = { :git => 'https://github.com/{YOURGITHUBNAME}/{YOURPODNAME}.git', :tag => s.version.to_s }
  # s.social_media_url = 'https://twitter.com/<TWITTER_USERNAME>'

  s.ios.deployment_target = '8.0'

  s.source_files = '{YOURPODNAME}/Classes/**/*'

  # s.resource_bundles = {
  #   '{YOURPODNAME}' => ['{YOURPODNAME}/Assets/*.png']
  # }

  # s.public_header_files = 'Pod/Classes/**/*.h'
  # s.frameworks = 'UIKit', 'MapKit'
  # s.dependency 'AFNetworking', '~> 2.3'
end
```

**必须要修改的**:
`s.summary`: pod 摘要
`s.description`: pod 描述
`s.homepage`: pod 在 github 中的地址
`s.author`: 作者姓名及邮箱
`s.source`: pod 的 git 地址

其余的根据您的实际情况进行修改，每个字段的描述，下篇文章中会详细介绍！

### 验证 YOURPODNAME.podspec

```text
$ pod lib lint

 -> YOURPODNAME (0.1.0)
    - WARN  | summary: The summary is not meaningful.
    - WARN  | url: The URL (https://github.com/{YOURGITHUBNAME}/YOURPODNAME) is not reachable.
    - NOTE  | xcodebuild:  note: Using new build system
    - NOTE  | [iOS] xcodebuild:  note: Planning build
    - NOTE  | [iOS] xcodebuild:  note: Constructing build description
    - NOTE  | xcodebuild:  note: Execution policy exception registration failed and was skipped: Error Domain=NSPOSIXErrorDomain Code=1 "Operation not permitted"
    - NOTE  | [iOS] xcodebuild:  warning: Skipping code signing because the target does not have an Info.plist file and one is not being generated automatically.

[!] YOURPODNAME did not pass validation, due to 2 warnings (but you can use `--allow-warnings` to ignore them).
You can use the `--no-clean` option to inspect any issue.
```

虽然上面还有两个 `WARN`，但是已经符合官方的标准了，可以进行提交操作了。但是！如果您是完美主义者，可以彻底处理干净后在进行提交！（我解决了，您随意！）

### 提交代码

```text
git add .
git commit -m "创建 pod 库"
git push
```

### 创建并提交 tag

```text
git tag -a 0.1.0 -m '创建 pod 库'
git push origin --tags
```

**注意：** 此处的 `tag` 应与 `.podspec` 文件中的 `s.version` 保持一致。每次修改 `pod` 中的代码，添加 `tag` 后，都应同时修改 `.podspec` 文件中的 `s.version`

## 提交 pod

```text
$ pod trunk push

[!] Found podspec `YOURPODNAME.podspec`
Updating spec repo `master`
Validating podspec
 -> YOURPODNAME (0.1.0)
    - NOTE  | xcodebuild:  note: Using new build system
    - NOTE  | [iOS] xcodebuild:  note: Planning build
    - NOTE  | [iOS] xcodebuild:  note: Constructing build description
    - NOTE  | xcodebuild:  note: Execution policy exception registration failed and was skipped: Error Domain=NSPOSIXErrorDomain Code=1 "Operation not permitted"
    - NOTE  | [iOS] xcodebuild:  warning: Skipping code signing because the target does not have an Info.plist file and one is not being generated automatically.

Updating spec repo `master`

--------------------------------------------------------------------------------
 🎉  Congrats

 🚀  YOURPODNAME (0.1.0) successfully published
 📅  June 18th, 10:30
 🌎  https://cocoapods.org/pods/YOURPODNAME
 👍  Tell your friends!
--------------------------------------------------------------------------------
```

恭喜您，您已经成功的将您创建的 pod 库推送到了官方 pod 库！

## 坑点 & 解决方案

### Failed to open TCP connection to trunk.cocoapods.org:443 (getaddrinfo: nodename nor servname provided, or not known)

**解：** 此问题常见于 `pod trunk` 相关的命令。网络大环境不行，要么呢啥（技术都懂的），要么连接手机开热点进行操作。

### Unable to accept duplicate entry for: YOURPODNAME (0.1.0)

**解：** `pod trunk push` 时发生此错误，说明该 `pod` 库在远端已经有了 0.1.0 版本。解决方案有两个：

1. 使用一个远端还没有的版本号
2. 使用 `pod trunk delete YOURPODNAME 0.1.0` 删除远端的 0.1.0 版本，然后重新进行推送

### unable to find a pod with name, author, summary, or description matching 'YOURPODNAME'

**解：** 信息更新不及时导致。

首先删除本地缓存

```text
rm ~/Library/Caches/CocoaPods/search_index.json
```

然后执行：

```text
pod update
```

> Title: 如何创建一个公有 Pod 库
>
> Date: 2019.06.21
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onntztzf](https://github.com/onntztzf)
