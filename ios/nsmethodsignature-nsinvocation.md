# NSMethodSignature 和 NSInvocation

## 常见的调用方法的两种方式

* performSelector: withObject:  

    **优点：** 可以调用运行时添加方法  

    **缺点：** 在编译阶段不会做校验。只有在程序运行的时候，才会知道是否存在即将调用的方法，如果方法不存在，程序会崩溃。因此为了保证程序的健壮，在调用方法前应该使用 `- (BOOL)respondsToSelector:(SEL)aSelector`，检查方法是否实现。  

* 直接调用方法  

  **优点：** 在编译阶段就会教研方法是否存在，Xcode会有相应提示  

  **缺点：** 局限性大，如果想调用某个方法，必须先实现这个方法，不如 `performSelector: withObject:` 灵活。

## 使用 NSMethodSignature 和 NSInvocation 调用方法

使用 `NSMethodSignature` 和 `NSInvocation` 组合实现方法的调用。

### NSMethodSignature

通过 `NSMethodSignature` 可以获取方法的参数类型和返回值类型。常用方法有：

```text
//从实例中获取实例方法签名，或者从类中获取类方法签名
+ (NSMethodSignature *)instanceMethodSignatureForSelector:(SEL)aSelector

//从一个类中获取实例方法签名
- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
```

可以通过下面的代码，更好的理解该怎么获取方法签名：

```text
SEL initSEL = @selector(init);
SEL allocSEL = @selector(alloc);

// 从NSString类中获取实例方法(init)的方法签名
NSMethodSignature *initSig = [NSString instanceMethodSignatureForSelector:initSEL];
// 从test实例中获取实例方法(init)的方法签名
initSig = [@"test" methodSignatureForSelector:initSEL];
// 从NSString类中获取类方法签名
NSMethodSignature *allocSig = [NSString methodSignatureForSelector:allocSEL];
```

### NSInvocation

`NSInvocation` 可以说是 `performSelector: withObject:` 的升级版，可以调用较为复杂的方法，进行参数、返回值的处理等;

### NSMethodSignature 和 NSInvocation 搭配的使用方法

```text
NSString *str = @"Test";
str = [str stringByAppendingString:@" AppendingString"];
NSLog(@"str: %@", str);

//需要调用的方法
SEL selector = @selector(stringByAppendingString:);
//获取方法签名
NSMethodSignature *signature = [str methodSignatureForSelector:selector];
//创建 NSInvocation 对象
NSInvocation *invocation = [NSInvocation invocationWithMethodSignature:signature];
//设置消息接受对象
invocation.target = str;
//设置发送的消息
invocation.selector = selector;

//建议通过signature.numberOfArgument获取参数个数
//可以保证不多参，不少参
//这边减2的原因是：
//0位置的参数是 目标（self）
//1位置的参数是 selector（_cmd）
//所以2位置才是所需要的第一个参数
NSInteger paramCount = signature.numberOfArguments - 2;
NSLog(@"paramCount: %@", @(paramCount));

for (int i = 0; i < paramCount; i++) {
    //设置参数
    [invocation setArgument:&str atIndex:i + 2];
}
//执行 invocation
[invocation invoke];

//获取返回值
id returnValue = nil;
if (signature.methodReturnLength) {
    [invocation getReturnValue:&returnValue];
}
NSLog(@"returnValue: %@", returnValue);
```

> Title: NSMethodSignature 和 NSInvocation
>
> Date: 2018.03.10
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)

