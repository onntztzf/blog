# Hook 系统代理方法

本篇文章主要叙述的是通过 **`Runtime`** 相关知识，完成对 `UIScrollView` 的代理方法进行 `hook`。从而添加一个停止滚动的回调。

## Runtime

做 `iOS` 开发的同学们一定知道 `Runtime` ，这里就不讲太多了。[这个是 Runtime 文档](https://developer.apple.com/documentation/objectivec/objective_c_runtime)，有兴趣的同学，可以自己查阅一下。网上关于 `Runtime` 的博客也有很多，官方文档看不懂，可以看看其他人的博客。(๑•̀ㅂ•́)و

## `UIScrollView` 停止滚动的类型

通过调查发现 `UIScrollView` 停止滚动的类型分为三种：

1. 快速滚动，自然停止
2. 快速滚动，手指按压突然停止
3. 慢速上下滑动停止

第 1 种类型，比较简单，在 `UIScrollView` 的代理中就可以监听到。

```text
- (void)scrollViewWillBeginDecelerating:(UIScrollView *)scrollView;
```

而第 2 种类型和第 3 种类型，就没有方法让我们可以直接监听到了。但是只要是滑动了，就一定会触发 `UIScrollView` 的下面代理，然后通过 `UIScrollView` 部分属性的改变，我们就可以监听到滚动停止了，后面会详细介绍方法。

```text
- (void)scrollViewDidEndDecelerating:(UIScrollView *)scrollView;
- (void)scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate;
```

## 添加 UIScrollView 滚动停止回调

### 监听 UIScrollView 停止滚动

通过翻阅文档，我们可以看到 `UIScrollView` 有三个属性：**tracking、dragging、decelerating。**

```text
// returns YES if user has touched. may not yet have started dragging
@property(nonatomic,readonly,getter=isTracking) BOOL tracking;

// returns YES if user has started scrolling. this may require some time and or distance to move to initiate dragging
@property(nonatomic,readonly,getter=isDragging) BOOL dragging;

// returns YES if user isn't dragging (touch up) but scroll view is still moving
@property(nonatomic,readonly,getter=isDecelerating) BOOL decelerating;
```

在滚动和滚动结束时，这三个属性的值都不相同。我们利用这三个属性，完成对 `UIScrollView` 停止滚动的监听。

停止类型 1：

```text
- (void)scrollViewDidEndDecelerating:(UIScrollView *)scrollView;
tracking:0,dragging:0,decelerating:0
```

停止类型 2：

```text
- (void)scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate;
tracking:1,dragging:0,decelerating:1

- (void)scrollViewDidEndDecelerating:(UIScrollView *)scrollView;
tracking:0,dragging:0,decelerating:0
```

停止类型 3：

```text
- (void)scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate;
tracking:1,dragging:0,decelerating:0
```

通过上面的代码，可以发现，我们只需要对 `UIScrollView` 的这三个属性进行相应的组合，就可以监听到 `UIScrollView` 停止滚动的事件了。

```text
- (void)scrollViewDidEndDecelerating:(UIScrollView *)scrollView {
    // 停止类型 1、停止类型 2
    BOOL scrollToScrollStop = !scrollView.tracking && !scrollView.dragging && !scrollView.decelerating;
    if (scrollToScrollStop) {
        [self scrollViewDidEndScroll];
    }
}

- (void)scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate {
    if (!decelerate) {
        // 停止类型 3
        BOOL dragToDragStop = scrollView.tracking && !scrollView.dragging && !scrollView.decelerating;
        if (dragToDragStop) {
            [self scrollViewDidEndScroll];
        }
    }
}

#pragma mark - scrollView 滚动停止
- (void)scrollViewDidEndScroll {
    NSLog(@"停止滚动了！！！");
}
```

**上面的代码具体请看** [**监听 UIScrollView 停止滚动的 Demo**](https://github.com/onntztzf/P_App_OC) **中的`Demo6-UIScrollView停止滚动`**

### 添加停止滚动的回调

#### Hook setDelegate

因为我们要对 `UIScrollView` 的 `setDelegate` 进行方替换，因此我们需要创建一个创建一个 `UIScrollView` 的 `Category` ，在 `load` 中进行替换。使用`dispatch_once`包住替换方法的代码，保证只进行一次替换操作，不会因多次替换同一方法，产生隐患。我这边只想对 `UIScrollView` 添加滚动停止的监听，所以在 `hook_setDelegate` 进行了判断，如果是 `[UIScrollView class]` 才会去 Hook 系统的代理方法。

```text
+ (void)load {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        Method originalMethod = class_getInstanceMethod([UIScrollView class], @selector(setDelegate:));
        Method replaceMethod = class_getInstanceMethod([UIScrollView class], @selector(hook_setDelegate:));
        method_exchangeImplementations(originalMethod, replaceMethod);
    });
}

- (void)hook_setDelegate:(id<UIScrollViewDelegate>)delegate {
    [self hook_setDelegate:delegate];
    if ([self isMemberOfClass:[UIScrollView class]]) {
        NSLog(@"是 UIScrollView，hook 方法");
        //Hook (scrollViewDidEndDecelerating:) 方法
        Hook_Method([delegate class], @selector(scrollViewDidEndDecelerating:), [self class], @selector(p_scrollViewDidEndDecelerating:), @selector(add_scrollViewDidEndDecelerating:));
        //Hook (scrollViewDidEndDragging:willDecelerate:) 方法
        Hook_Method([delegate class], @selector(scrollViewDidEndDragging:willDecelerate:), [self class], @selector(p_scrollViewDidEndDragging:willDecelerate:), @selector(add_scrollViewDidEndDragging:willDecelerate:));
    } else {
        NSLog(@"不是 UIScrollView，不需要 hook 方法");
    }
}
```

#### Hook Method

如果我们想要 hook 某个代理方法，我们需要考虑这几种情况：

* 代理对象实现了 `scrollViewDidEndDecelerating:` 方法，那么我们直接交换就行。
* 代理对象如果没有实现 `scrollViewDidEndDecelerating:` 方法，而我们又想监听时，就需要我们动态的添加 `scrollViewDidEndDecelerating:` 方法。
* `setDelegate:` 万一重复设置了，会导致 `scrollViewDidEndDecelerating:` 多次交换，我们需要预防这种情况。

```text
static void Hook_Method(Class originalClass, SEL originalSel, Class replacedClass, SEL replacedSel, SEL noneSel){
    // 原实例方法
    Method originalMethod = class_getInstanceMethod(originalClass, originalSel);
    // 替换的实例方法
    Method replacedMethod = class_getInstanceMethod(replacedClass, replacedSel);
    // 如果没有实现 delegate 方法，则手动动态添加
    if (!originalMethod) {
        Method noneMethod = class_getInstanceMethod(replacedClass, noneSel);
        BOOL addNoneMethod = class_addMethod(originalClass, originalSel, method_getImplementation(noneMethod), method_getTypeEncoding(noneMethod));
        if (addNoneMethod) {
            NSLog(@"******** 没有实现 (%@) 方法，手动添加成功！！",NSStringFromSelector(originalSel));
        }
        return;
    }
    // 向实现 delegate 的类中添加新的方法
    // 这里是向 originalClass 的 replaceSel（@selector(p_scrollViewDidEndDecelerating:)）添加 replaceMethod
    BOOL addMethod = class_addMethod(originalClass, replacedSel, method_getImplementation(replacedMethod), method_getTypeEncoding(replacedMethod));
    if (addMethod) {
        // 添加成功
        NSLog(@"******** 实现了 (%@) 方法并成功 Hook 为 --> (%@)", NSStringFromSelector(originalSel), NSStringFromSelector(replacedSel));
        // 重新拿到添加被添加的 method，这里是关键 (注意这里 originalClass, 不 replacedClass), 因为替换的方法已经添加到原类中了，应该交换原类中的两个方法
        Method newMethod = class_getInstanceMethod(originalClass, replacedSel);
        // 实现交换
        method_exchangeImplementations(originalMethod, newMethod);
    }else{
        // 添加失败，则说明已经 hook 过该类的 delegate 方法，防止多次交换。
        NSLog(@"******** 已替换过，避免多次替换 --> (%@)",NSStringFromClass(originalClass));
    }
}
```

#### 实现我们自己方法

```text
// 已经实现需要 hook 的代理方法时，调用此处方法进行替换
#pragma mark - Replace_Method
- (void)p_scrollViewDidEndDecelerating:(UIScrollView *)scrollView {
    NSLog(@"%s", __func__);
    [self p_scrollViewDidEndDecelerating:scrollView];
    // 停止类型 1、停止类型 2
    BOOL scrollToScrollStop = !scrollView.tracking && !scrollView.dragging && !scrollView.decelerating;
    if (scrollToScrollStop) {
        [scrollView stopScroll:scrollView];
    }
}

- (void)p_scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate {
    NSLog(@"%s", __func__);
    [self p_scrollViewDidEndDragging:scrollView willDecelerate:decelerate];
    if (!decelerate) {
        // 停止类型 3
        BOOL dragToDragStop = scrollView.tracking && !scrollView.dragging && !scrollView.decelerating;
        if (dragToDragStop) {
            [scrollView stopScroll:scrollView];
        }
    }
}

// 那没有实现需要 hook 的代理方法时，调用此处方法
#pragma mark - Add_Method
- (void)add_scrollViewDidEndDecelerating:(UIScrollView *)scrollView {
    NSLog(@"%s", __func__);
    // 停止类型 1、停止类型 2
    BOOL scrollToScrollStop = !scrollView.tracking && !scrollView.dragging && !scrollView.decelerating;
    if (scrollToScrollStop) {
        [scrollView stopScroll:scrollView];
    }
}

- (void)add_scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate {
    NSLog(@"%s", __func__);
    if (!decelerate) {
        // 停止类型 3
        BOOL dragToDragStop = scrollView.tracking && !scrollView.dragging && !scrollView.decelerating;
        if (dragToDragStop) {
            [scrollView stopScroll:scrollView];
        }
    }
}

#pragma mark - scrollView 滚动停止时触发的方法
- (void)stopScroll:(UIScrollView *)scrollView {
    NSLog(@"滚动已停止");
}
```

#### 添加回调

接下来，再通过 `Runtime` 在 `Category` 中对 `UIScrollView` 添加一个回调属性`stopScrollBlock`。

`UIScrollView+Category.h`文件

```text
@property(nonatomic, copy) StopScrollBlock stopScrollBlock;
```

`UIScrollView+Category.m`文件

```text
static const char p_stopScrollBlock = '\0';
- (StopScrollBlock)stopScrollBlock {
    return objc_getAssociatedObject(self, &p_stopScrollBlock);
}

- (void)setStopScrollBlock:(StopScrollBlock)stopScrollBlock {
    objc_setAssociatedObject(self, &p_stopScrollBlock, stopScrollBlock, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
}
```

最后在监听滚动停止的方法中调用这个回调，就大工告成了。

```text
- (void)stopScroll:(UIScrollView *)scrollView {
    if (self.stopScrollBlock) {
        self.stopScrollBlock(scrollView);
    }
}
```

### 回调的使用

```text
UIScrollView *scrollView = [[UIScrollView alloc] initWithFrame:CGRectMake(0, 0, kScreenW, kScreenH)];
scrollView.contentSize = CGSizeMake(kScreenW * 8, kScreenH);
scrollView.delegate = self;
scrollView.stopScrollBlock = ^(UIScrollView *scrollView) {
    NSLog(@"停止滑动");
};
[self.view addSubview:scrollView];
```

## 参考资料

1. [UITableView、UICollectionView 滚动结束的监测](https://www.jianshu.com/p/718862ee13b0)
2. [Method Swizzling 实战：Hook 系统代理方法](https://www.jianshu.com/p/3fafb68b1d11)

> Title: Hook 系统代理方法
>
> Date: 2018.01.14
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onntztzf](https://github.com/onntztzf)
