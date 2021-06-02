# Widget 开发-开发篇

## 开发步骤

建议先阅读[Widget 开发-配置篇](widget-configuration.md)，再开始开发，因为开发的过程中需要提前准备一些东西

### 创建新的 `Target`，选择 `Today Extension`

创建完成后，会生成如下图的几个文件。

![image](http://img.zhangpeng.site/2017/09/07/1.jpeg)

![image](http://img.zhangpeng.site/2017/09/07/2.jpeg)

### 修改 `Today Extension` 的 `Info.plist`

* Bundle display name

  Widget在通知栏显示的名称

* NSExtension

  如果你是使用纯代码进行开发，请按照下面进行操作：

  1. 请删除 `NSExtensionMainStoryboard` 的键值对和 `MainInterface.storyboard` 文件
  2. 请添加 `NSExtensionPrincipalClass` 这个 `key`，并将 `value` 设置为控制器（如 `TodayViewController`）

     ![image](http://img.zhangpeng.site/2017/09/07/3.jpeg)

### 准备工作都已经完成，可以进入开发工作

`Widget` 的开发并没有多难，照着文档足以开发出一个很漂亮的 `Wiget` 了，不过有些版本差异要注意下。

#### iOS8

在 `iOS8` 中没有折叠和展开功能，默认的 `Widget` 高度为 `self.preferredContentSize` 设置的高度。

```text
self.preferredContentSize = CGSizeMake(kScreenW, 100);
```

`iOS8` 下所有组件**默认右移30单位**，可以通过下面的方法修改上下左右的距离

```text
- (UIEdgeInsets)widgetMarginInsetsForProposedMarginInsets:(UIEdgeInsets)defaultMarginInsets {
    return UIEdgeInsetsMake(0, 0, 0, 0);
}
```

#### iOS10

`iOS10` 以后，`Widget` 可玩性变得更高了，有了两种显示模式:

1. NCWidgetDisplayModeCompact // Fixed height，高度固定，最低高度为110
2. NCWidgetDisplayModeExpanded // Variable height，高度可变

```text
 // 5s模拟器下:
 // NCWidgetDisplayModeCompact模式下:{304, 110}
 // NCWidgetDisplayModeExpanded模式下:{304, 528}

 // 6s模拟器下：
 // NCWidgetDisplayModeCompact模式下:{359, 110}
 // NCWidgetDisplayModeExpanded模式下:{359, 616}
```

**设定显示模式，需要在设定 `Size` 前设定这个属性**，代码如下：

```text
- (void)viewDidLoad {
    [super viewDidLoad];
    if ([[UIDevice currentDevice] systemVersion].intValue >= 10) {  
        self.extensionContext.widgetLargestAvailableDisplayMode = NCWidgetDisplayModeCompact;
        // self.extensionContext.widgetLargestAvailableDisplayMode = NCWidgetDisplayModeExpanded;
    }
    self.preferredContentSize = CGSizeMake(kScreenW, 100);
    [self setupUI];
}
```

当显示模式设置为 `NCWidgetDisplayModeExpanded` 时，点击折叠和打开时，会触发下面这个方法，在这个方法中可以修改对应状态的高度。修改完毕后，更新视图即可看到最新的布局。

```text
- (void)widgetActiveDisplayModeDidChange:(NCWidgetDisplayMode)activeDisplayMode withMaximumSize:(CGSize)maxSize {
    if (activeDisplayMode == NCWidgetDisplayModeCompact) {
        self.preferredContentSize = CGSizeMake(maxSize.width, 110);
    } else {
        self.preferredContentSize = CGSizeMake(maxSize.width, 200);
    }
 }

 //在下面的方法中更新视图
 -(void)widgetPerformUpdateWithCompletionHandler:(void (^)(NCUpdateResult))completionHandler {
 //    NCUpdateResultNewData   新的内容需要重新绘制视图
 //    NCUpdateResultNoData    部件不需要更新
 //    NCUpdateResultFailed    更新过程中发生错误
   completionHandler(NCUpdateResultNoData);
 }
```

## 可能会遇上的问题&解决办法

### 代码共享

目前我见到了四种共享代码的方法：

1. 将代码打包成 `Framework`，然后 `link` 到主 `App`和 `Widget` 中 **（推荐）**
2. 不怕安装包变大的话，可以考虑将需要的第三方库在主 `App` 和 `Widget` 中分别复制一份 **（推荐）**
3. 将需要共享的文件按图中进行勾选配置

   ![image](http://img.zhangpeng.site/2017/09/07/4.jpeg)

4. 通过 `Pods` 导入，不太建议通过 `Pods` 分别向两个 `Target` 中导入第三方库，因为很容易发生一些不好处理的问题

### 数据共享

数据共享有两种常用的方法：

* NSUserDefaults  
  和我们常用的方法一样，不过在创建 `NSUserDefaults` 时，需要填写我们之前的 `GroupID`。通过 `GroupID`，我们就可以进行主 `App` 和 `Widget` 之间的数据共享了。

  ```text
  // 写入数据
  NSString *groupID = @"group.com.aaa.bbb";
  NSUserDefaults *ud = [[NSUserDefaults alloc] initWithSuiteName:groupID];[ud setObject:@"我是测试的数据" forKey:@"test"];
  [ud synchronize];

  // 读取数据
  NSString *groupID = @"group.com.aaa.bbb";
  NSUserDefaults *ud = [[NSUserDefaults alloc] initWithSuiteName:groupID];
  NSString *value = [ud objectForKey:@"test"];
  ```

* NSFileManager

  ```text
  // 写入数据
  NSString *groupID = @"group.com.aaa.bbb";
  NSError *err = nil;
  NSURL *containerURL = [[NSFileManager defaultManager] containerURLForSecurityApplicationGroupIdentifier:groupID];
  containerURL = [containerURL URLByAppendingPathComponent:@"Library/Caches/test"];
  NSString *value = @"我是测试的数据";
  BOOL result = [value writeToURL:containerURL atomically:YES encoding:NSUTF8StringEncoding error:&err];
  if(result){
      NSLog(@"写入成功");
  }

  // 读取数据
  NSString *groupID = @"group.com.aaa.bbb";
  NSError *err = nil;
  NSURL *containerURL = [[NSFileManager defaultManager] containerURLForSecurityApplicationGroupIdentifier:groupID];
  containerURL = [containerURL URLByAppendingPathComponent:@"Library/Caches/test"];
  NSString *value = [NSString stringWithContentsOfURL:containerURL encoding:NSUTF8StringEncoding error:&err];
  ```

### 数据刷新

当widget从屏幕上消失2s左右，再次出现在屏幕中时，都会重新调用viewDidLoad方法。所以每次出现都请求最新数据，进行刷新操作，widget都会闪一下，根据产品需求，可以做一下控制；

```text
- (void)viewDidLoad {
    [super viewDidLoad];
}
```

如果短时间内让Widget频繁地消失显示，那只会执行viewWillAppear方法；

```text
- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
}
```

### 打开 `App`

1. 设置 `App` 的 `URLSchemes`，打开 `APP` 主要通过 `URLScheme` 打开和传递参数值。 设置 `URLSchemes` 时，要独特一些，避免与其他 `App` 重复 ![image](http://img.zhangpeng.site/2017/09/07/5.jpeg)
2. 在 `Widget` 中添加点击事件，用于触发打开 `App` 的操作和传递参数

   ```text
    NSString *schemeString = @"zhangpeng://actionName?paramName=paramValue";

    [self.extensionContext openURL:[NSURL URLWithString:schemeString] completionHandler:^(BOOL success) {

    }];
   ```

3. `Appdelegate` 的代理方法中，截取 `URL`，做响应处理：

   ```text
    // 所有版本的都可以使用
    - (BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation {
        [self appCallbackWithOpenUrl:url];
        return YES;
    }

    // iOS 8 以后
    - (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
        [self appCallbackWithOpenUrl:url];
        return YES;
    }

    // iOS 7
    - (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url {
        [self appCallbackWithOpenUrl:url];
        return YES;
    }

    - (void)appCallbackWithOpenUrl:(NSURL *)url{
        NSLog(@"url: %@", url.host);
        // 针对url进行不同的操作
    }
   ```

> Title: Widget 开发-开发篇
>
> Date: 2017.09.07
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)

