# iOS 消息转发机制

当对象接收到无法解读的消息（`unrecognized selector sent to instance 0x87`），就会启动消息转发机制，由程序员指定处理方法。

## 消息转发两大阶段

1. 动态方法解析

   检查当前接收者能否动态添加方法，处理这个`unrecognized selector`。

2. 完整的消息转发

   第一阶段执行完毕后，如接收者不能以动态新增方法处理这个`unrecognized selector`，接下来，会分两种情况：

   * 有备援接收者（replacement receiver）

     在运行期将消息转给备援接收者，由备援接收者完成消息的处理。

   * 无备援接收者（replacement receiver）
   * 启动一套“完整的消息转发机制”，将消息封装到NSInvocation对象中，交给接收者处理。

### 动态方法解析

如果没有找到需要执行的方法，会根据方法的类型，执行不同的处理方法。

处理无法调用的**类方法**

```text
+ (BOOL)resolveClassMethod:(SEL)sel;
```

处理无法调用的**实例方法**

```text
+ (BOOL)resolveInstanceMethod:(SEL)sel;
```

一般是提前写好相关的实现代码，通过 Runtime 在此处插入到类中。

**e.g.**

```text
/**
 没有找到SEL的实现时会执行下方的方法
 @param sel 当前对象调用并且找不到IML的SEL
 @return 是否可以处理这个方法，并返回yes
 */
+ (BOOL)resolveInstanceMethod:(SEL)sel
{
// 当返回YES时
// 在这里通过Runtime在将已经写好实现的代码插入到类中。
// ...
    return YES;
// 当返回NO时
// 会接着执行forwordingTargetForSelector:方法
//    return NO;  
}
```

### 消息转发

#### 有备援接收者

在方法 `- (id)forwardingTargetForSelector:(SEL)aSelector` 中返回可以处理该消息的对象，交由该对象去处理这个消息。  
如果此处返回nil，则表示没有其他对象可以处理这个消息，然后通过完整的消息转发机制来处理。

```text
/**
 将当前对象不存在的SEL传给其他存在该SEL的对象
 @param aSelector 当前类中不存在的SEL
 @return 存在该SEL的对象
 */
- (id)forwardingTargetForSelector:(SEL)aSelector 
{
// 不传递给其他对象
// 将会执行- (void)forwardInvocation:(NSInvocation *)anInvocation;
    return nil;

// 传递给一个其他对象，处理这个方法。
// 可以做相应的错误处理等
// 让OtherClass中相应的SEL去执行该方法
//    return [[OtherClass alloc] init];
}
```

#### 无备援接收者

如果接收者不能处理消息，并且没有备援接收者，最终只能采取一个完整的消息转发来处理消息。

通过NSInvocation包装方法的目标、参数等，然后通过 `- (void)forwardInvocation:(NSInvocation *)invocation` 将消息指派给目标对象。

```text
- (void)forwardInvocation:(NSInvocation *)invocation
{
    SecondClass * forwardClass = [SecondClass new];
    SEL sel = invocation.selector;
    if ([forwardClass respondsToSelector:sel]) {
        [invocation invokeWithTarget:forwardClass];
    } else {
        [self doesNotRecognizeSelector:sel];
    }
}
```

> Title: iOS 消息转发机制
>
> Date: 2018.04.02
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)

