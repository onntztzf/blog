# 动态更换 App 图标

在`iOS 10.3`苹果添加了更换图标的功能，通过这个功能，我们可以在适当的时候采取特定的方式为我们的`App`更换图标。 听似很好很方便，实则并没有。原因如下：

1. 更换的图标，我们需要预置在项目中
2. 替换图标这个功能，一定要经过用户同意（虽然有跳过这一步的方法，但是**不建议使用**）

虽然我们在使用这个功能时有着种种限制，但是瑕不掩瑜，他同样为我们的用户体验带来了提升：

1. 逢年过节想换个应景的`App图标`，不用在进行发版了
2. 公司有个重大活动需要更换图标，不用担心活动前不能成功发版上线了

**注：** **我们更换的不只是APP的图标，还有通知栏的中的图标，以及设置界面中的图标等所有与我们 App 有关的图标。**

## 准备你要更换的图标

将我们需要更换的图标放到我们的**项目目录**中（因为放到.xcassets中不管用），图片的命名建议以下面的方式命名，例如：xx20x20@2x.png，xx20x20@3x.png…这样在填写`Info.plist`时也会省事很多。

![icon命名](http://img.zhangpeng.site/2018/07/10/1.jpg)

> **PS：**
> 其实对于更换的图标，我们也可以只提供一张，但命名时，我们就不要填写具体的尺寸了，只保留图片名字即可，例如：xx@2x.png，xx@3x.png， 但是效果上可能不如准备一整套的效果好。毕竟把一张桌面图标大小的图片塞到通知图标那么小的框里，图片会压缩。

## 修改`Info.plist`

想要实现换图标的功能，Info.plist 文件的修改是很重要的一步。

![编辑Info.plist](http://img.zhangpeng.site/2018/07/10/2.jpg)

> * `CFBundleIcons`:
>   一个字典，包含所有AppIcon信息，即上图的Icon files(iOS 5)
> * `CFBundlePrimaryIcon`:
>   如果已经在`Assets.xcassets`中设置了`AppIcon`，那么`CFBundlePrimaryIcon`中的配置会被忽略，`Assets.xcassets`的`AppIcon`将会自动配置到`CFBundlePrimaryIcon`中。
> * `CFBundleAlternateIcons`:
>   一个数组，负责配置可供替换的icon信息
> * `UIPrerenderedIcon`:
>   是否已经预渲染，如果不设置该项或者设为NO。系统会自动为icon进行渲染增加光泽

如果想详细了解`CFBundleIcons`, `CFBundlePrimaryIcon`, `CFBundleAlternateIcons`，请查看附件2

**如果iPad需要也需要更换图标，那么我们需要在`CFBundleIcons~ipad`进行同样的设置。**

**注：** **不能把图片放在.xcassets里面**

## 编写代码

通过查看文档，我们可以看到下面几个属性和方法。

```objc
// If false, alternate icons are not supported for the current process.
// 检查是否支持更换图标
@property (readonly, nonatomic) BOOL supportsAlternateIcons NS_EXTENSION_UNAVAILABLE("Extensions may not have alternate icons") API_AVAILABLE(ios(10.3), tvos(10.2));

// Pass `nil` to use the primary application icon. The completion handler will be invoked asynchronously on an arbitrary background queue; be sure to dispatch back to the main queue before doing any further UI work.
// 更换图标
- (void)setAlternateIconName:(nullable NSString *)alternateIconName completionHandler:(nullable void (^)(NSError *_Nullable error))completionHandler NS_EXTENSION_UNAVAILABLE("Extensions may not have alternate icons") API_AVAILABLE(ios(10.3), tvos(10.2));

// If `nil`, the primary application icon is being used.
// 当前图标的名称
@property (nullable, readonly, nonatomic) NSString *alternateIconName NS_EXTENSION_UNAVAILABLE("Extensions may not have alternate icons") API_AVAILABLE(ios(10.3), tvos(10.2));
```

系统提供的 API 简单明了，唯一要注意的是下面这个方法。

```objc
- (void)setAlternateIconName:(nullable NSString *)alternateIconName completionHandler:(nullable void (^)(NSError *_Nullable error))completionHandler
```

方法中的`alternateIconName`参数，是要填写您在`Info.plist` 中填写的名字，如图二中所示，我们应当在此方法中填写`female`或者`male1`.

## 代码示例

为了方便大家使用，我将更换图标相关的代码已经写好在下面，如需自取。
也可以访问 [DynamicAppIconDemo](https://github.com/gh-zhangpeng/DynamicAppIconDemo)，查看 `FSAppIconManager` 类

```objc
+ (NSString *)getCurrentAppIconName {
    if (@available(iOS 10.3, *)) {
        return ([UIApplication sharedApplication].alternateIconName.length == 0) ? @"" : [UIApplication sharedApplication].alternateIconName;
    } else {
        // Fallback on earlier versions
        return @"";
    }
}

+ (BOOL)canChangeAppIcon {
    if (@available(iOS 10.3, *)) {
        return [[UIApplication sharedApplication] supportsAlternateIcons];
    } else {
        // Fallback on earlier versions
        return NO;
    }
}

+ (void)changeAppIconWithIconName:(NSString *)iconName completionHandler:(void (^)(NSError * _Nullable))completionHandler {
    if (@available(iOS 10.3, *)) {
        [[UIApplication sharedApplication] setAlternateIconName:iconName completionHandler:^(NSError * _Nullable error) {
            if (!error) {
                completionHandler(nil);
            } else {
                completionHandler(error);
            }
        }];
    } else {
        // Fallback on earlier versions
        NSDictionary *userInfo = @{
                                   NSLocalizedDescriptionKey: NSLocalizedString(@"AppIcon change failed", nil),
                                   NSLocalizedFailureReasonErrorKey: NSLocalizedString(@"The current system version does not support replacing the AppIcon.", nil),
                                   NSLocalizedRecoverySuggestionErrorKey: NSLocalizedString(@"", nil)
                                   };
        NSError *error = [NSError errorWithDomain:@""
                                             code:34001
                                         userInfo:userInfo];
        completionHandler(error);
    }
}
```

## 下面给出部分 App Icon 相关的资料

### App Icon Attributes

|Attribute|Value|
|---|---|
|Format|PNG|
|Color space|sRGB or P3 (see [Color Management](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/color/#color-management))|
|Layers|Flattened with no transparency|
|Resolution|Varies. See [Image Size and Resolution](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution/)|
|Shape|    Square with no rounded corners|

### App Icon Sizes

|Device or context|    Icon size|
|---|---|
|iPhone|180px × 180px (60pt × 60pt @3x)|
|      |120px × 120px (60pt × 60pt @2x)|
|iPad Pro|167px × 167px (83.5pt × 83.5pt @2x)|
|iPad, iPad mini|152px × 152px (76pt × 76pt @2x)|
|App Store|1024px × 1024px (1024pt × 1024pt @1x)|

### Spotlight, Settings, and Notification Icons

|Device or context|Spotlight icon size|Settings icon size|Notification icon size|
|---|---|---|---|
|iPhone|120px × 120px (40pt × 40pt @3x)|87px × 87px (29pt × 29pt @3x)|60px × 60px (20pt × 20pt @3x)|
|      |80px × 80px (40pt × 40pt @2x)|58px × 58px (29pt × 29pt @2x)|40px × 40px (20pt × 20pt @2x)|
|iPad Pro, iPad, iPad mini|    80px × 80px (40pt × 40pt @2x)|58px × 58px (29pt × 29pt @2x)|40px × 40px (20pt × 20pt @2x)|

### Notice

Don’t add an overlay or border to your Settings icon. iOS automatically adds a 1-pixel stroke to all icons so that they look good on the white background of Settings.

## 附

1. [Human Interface Guidelines - App Icon](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/app-icon/)
2. [CFBundleIcons,CFBundlePrimaryIcon,CFBundleAlternateIcons](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249-SW10)

---

> Title: 动态更换 App 图标
>
> Date: 2018.07.10
>
> Author: zhangpeng
>
> Github: <https://github.com/gh-zhangpeng>
