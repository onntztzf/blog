# 读取一个带有加密印章的 PDF

之前公司在和一个做电子签章的公司合作时，他们给我们提供了一份带有加密印章的 `PDF`。在测试中发现，不论通过 `UIWebView` 或者 `WKWebView` 打开，`PDF` 中的加密印章都不能成功展示。

通过不断的调研及尝试，最终成功展示出了 `PDF` 中的加密印章。现在把方法分享给大家～

本文的所有代码均以上传至 `GitHub`，如需[自取](https://github.com/onntztzf/ShowPDFDemo.git)~

## 实现步骤

### 宏

为了方便我进行代码编写，我们提前设置几个宏：

```text
#define kScreenW [UIScreen mainScreen].bounds.size.width
#define kScreenH [UIScreen mainScreen].bounds.size.height

#define DOCUMENTS_DIRECTORY [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) lastObject]
```

### 详细代码

本文中的 `Demo` 是以 `WKWebView` 进行开发，如果您需要使用 `UIWebView`，请自行修改。

1. 添加 `WKWebView`

   ```objc

   **import &lt;WebKit/WebKit.h&gt;**

   WKWebViewConfiguration *config = [[WKWebViewConfiguration alloc] init];

   WKUserContentController *wkUController = [[WKUserContentController alloc]init];

   config.userContentController = wkUController;

   // 注入JS对象名称AppModel，当JS通过AppModel来调用时，我们可以在WKScriptMessageHandler代理中接收到 // 此处是为了得到PDF加载完成或失败的反馈 [config.userContentController addScriptMessageHandler:self name:@"AppModel"];

   // 改变页面内容宽度，适配屏幕大小 NSString *js = @"var meta = document.createElement('meta'); meta.setAttribute('name', 'viewport'); meta.setAttribute('content', 'width=device-width'); document.getElementsByTagName('head')[0].appendChild(meta);";

   WKUserScript *wkUserScript = [[WKUserScript alloc] initWithSource:js injectionTime:WKUserScriptInjectionTimeAtDocumentEnd forMainFrameOnly:YES]; [wkUController addUserScript:wkUserScript];

```text
WKWebView *webView = [[WKWebView alloc] initWithFrame:CGRectMake(0, 0, kScreenW, kScreenH - 64)
                                        configuration:config];
webView.backgroundColor = [UIColor whiteColor];
webView.UIDelegate = self;
webView.navigationDelegate = self;
[self.view addSubview:webView];
```

```text
1. 下载PDF

   ```text
    NSString *urlStr = @"http://file.zhangpeng.site/jianLi_zhangpeng.pdf";

    NSURLRequest *request = [NSURLRequest requestWithURL:[NSURL URLWithString:urlStr]];
    NSURLSession *session = [NSURLSession sharedSession];

    NSURLSessionDataTask *sessionDataTask = [session dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {
        NSLog(@"从服务器获取到 pdf 数据");
        //对从服务器获取到的数据 data 进行相应的处理：
        dispatch_async(dispatch_get_main_queue(), ^{
            NSString *path = [DOCUMENTS_DIRECTORY stringByAppendingPathComponent:@"contract.pdf"];
            NSFileManager *fm = [NSFileManager defaultManager];
            if ([fm fileExistsAtPath:path]) {
                [fm removeItemAtPath:path error:nil];
            }
            BOOL success =  [data writeToFile:path atomically:YES];
            if (success) {
                NSLog(@"保存成功");
                NSURL *baseURL = [NSURL fileURLWithPath:[self getHtmlBasePath]];
                NSString *path = [self getHtmlPath];
                NSString *htmlStr = [NSString stringWithContentsOfFile:path encoding:NSUTF8StringEncoding error:nil];

                [self.webView loadHTMLString:htmlStr baseURL:baseURL];
            }
        });
    }];
    [sessionDataTask resume];
```

1. 打开 `PDF`

   ```text
    - (void)webView:(WKWebView *)webView didFinishNavigation:(WKNavigation *)navigation {
        [self loadPDF];
    }

    - (void)loadPDF {
      NSString *path = [DOCUMENTS_DIRECTORY stringByAppendingPathComponent:@"contract.pdf"];
      NSData *data = [NSData dataWithContentsOfFile:path options:NSDataReadingMappedAlways error:nil];

      NSString *paraStr = [data base64EncodedStringWithOptions:NSDataBase64EncodingEndLineWithCarriageReturn];
      NSString *js = [NSString stringWithFormat:@"loadMyJS('%@')",paraStr];
      //NSLOG(@"%@",method);

      [self.webView evaluateJavaScript:js completionHandler:^(id _Nullable response, NSError * _Nullable error) {
          if (error) {
              NSLog(@"%@", error);
              NSLog(@"当前手机系统版本较低，不支持查看，请升级系统或者到 PC 端查看。");
          }
      }];
    }
   ```

2. 在 `WKWebView` 的代理中，我们可以知道 `PDF` 是否成功打开，

   ```text
    - (void)userContentController:(WKUserContentController *)userContentController didReceiveScriptMessage:(WKScriptMessage *)message {
        if ([message.name isEqualToString:@"AppModel"]) {
            //和 customview.js 文件交互，js 调 oc 的代码
            // 打印所传过来的参数，只支持 NSNumber, NSString, NSDate, NSArray, NSDictionary, and NSNull 类型
            if ([message.body[@"code"] isEqualToString:@"00000"]) {
                NSLog(@"%@", message.body[@"msg"]);
            }
       }
   }
   ```

3. `PDF` 是否读取成功是在 `customview.js` 中通知控制器的，具体可以查看下面的代码。

   ```javascript
    function handlePages(page)
    {
    //create new canvas
    var viewport = page.getViewport(1);
    var canvas = document.createElement( "canvas" );
    canvas.style.display="block";

    var context = canvas.getContext('2d');
    canvas.height = viewport.height;
    canvas.width = viewport.width;

    //render page
    page.render({canvasContext: context, viewport: viewport});

    //add canvas to body
    document.body.appendChild(canvas);

    //render new page
    pageNum++;
        if(pdfDoc!=null && pageNum<=numPages){
            pdfDoc.getPage(pageNum).then(handlePages);
            // PDF 加载失败
        }else{
            console.log("pdf load complete");
            // PDF 加载完毕，body的内容可以根据具体的业务需求进行修改
            window.webkit.messageHandlers.AppModel.postMessage({ code: "00000", msg: "pdf load complete" });//和wkWebView交互
        }

    }
   ```

到此，我们已经可以在 `iOS9` 以上的系统中，成功打开带加密印章的 `PDF`。至于 `iOS8` 为什么不行呢？下面给大家讲解及提供方案。

在 `iOS8` 上，`html` 及 `js` 文件的路径为 `tmp` 目录下，`iOS9` 及以上则在 `bundle` 里。

解决方案：

```text
- (NSString*)getHtmlBasePath {
    NSString *basePath = @"";
    if ([[[UIDevice currentDevice]systemVersion]floatValue]<9.0) {
        basePath = NSTemporaryDirectory();
    }else{
        basePath = [[NSBundle mainBundle] bundlePath];
    }
    return basePath;
}

- (NSString*)getHtmlPath{
    //在 iOS8 上，html 及 js 文件的路径为 tmp 目录下，iOS9 及以上则在 bundle 里
    NSString *path = @"";
    if ([[[UIDevice currentDevice]systemVersion] floatValue] < 9.0) {
        path = [self copyHtmlToTemp];
    } else {
        path = [[NSBundle mainBundle] pathForResource:@"index" ofType:@".html"];
    }
    return path;
}

//在 iOS8 上，html 及 js 文件要放到 tmp 目录下才能正常访问，iOS9 及以上不用
- (NSString*)copyHtmlToTemp {
    NSString* htmlPath = [[NSBundle mainBundle] pathForResource:@"index" ofType:@".html"];
    NSString *compatibilityJSPath = [[NSBundle mainBundle] pathForResource:@"compatibility" ofType:@".js"];
    NSString *customviewJSPath = [[NSBundle mainBundle] pathForResource:@"customview" ofType:@".js"];
    NSString *minimalCSSPath = [[NSBundle mainBundle] pathForResource:@"minimal" ofType:@".css"];
    NSString *pdfJSPath = [[NSBundle mainBundle] pathForResource:@"pdf" ofType:@".js"];
    NSString *pdfWorkerJSPath = [[NSBundle mainBundle] pathForResource:@"pdf.worker" ofType:@".js"];

    NSString *tempPath = NSTemporaryDirectory();

    NSString *htmlTempPath = [tempPath stringByAppendingPathComponent:@"index.html"];
    NSString *compatibilityJSTempPath = [tempPath stringByAppendingPathComponent:@"compatibility.js"];
    NSString *customviewJSTempPath = [tempPath stringByAppendingPathComponent:@"customview.js"];
    NSString *minimalCSSTempPath = [tempPath stringByAppendingPathComponent:@"minimal.css"];
    NSString *pdfJSTempPath = [tempPath stringByAppendingPathComponent:@"pdf.js"];
    NSString *pdfWorkerJSTempPath = [tempPath stringByAppendingPathComponent:@"pdf.worker.js"];

    NSFileManager *fm = [NSFileManager defaultManager];

    if (![fm fileExistsAtPath:htmlTempPath]) {
        [fm copyItemAtPath:htmlPath toPath:htmlTempPath error:nil];
    }
    if (![fm fileExistsAtPath:compatibilityJSTempPath]) {
        [fm copyItemAtPath:compatibilityJSPath toPath:compatibilityJSTempPath error:nil];
    }
    if (![fm fileExistsAtPath:customviewJSTempPath]) {
        [fm copyItemAtPath:customviewJSPath toPath:customviewJSTempPath error:nil];
    }
    if (![fm fileExistsAtPath:minimalCSSTempPath]) {
        [fm copyItemAtPath:minimalCSSPath toPath:minimalCSSTempPath error:nil];
    }
    if (![fm fileExistsAtPath:pdfJSTempPath]) {
        [fm copyItemAtPath:pdfJSPath toPath:pdfJSTempPath error:nil];
    }
    if (![fm fileExistsAtPath:pdfWorkerJSTempPath]) {
        [fm copyItemAtPath:pdfWorkerJSPath toPath:pdfWorkerJSTempPath error:nil];
    }
    return htmlTempPath;
}
```

> Title: 读取一个带有加密印章的 PDF
>
> Date: 2017.08.29
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onntztzf](https://github.com/onntztzf)
