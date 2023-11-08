# 类的初始化方法

**原文链接：**[**深入了解 iOS 的初始化**](https://mp.weixin.qq.com/s/Qs5JDavftrlpnGkb1BTlnw)**，本文是阅读以后的摘抄。**

类（结构体、枚举）的初始化有两种初始化器（初始化方法）：

* 指定初始化器（Designated Initializers）
* 便利初始化器（Convenience Initializers）

## 指定初始化器

指定构造器是类中最主要的构造器。一个指定构造器将初始化类中提供的所有属性，并调用合适的父类构造器让构造过程沿着父类链继续往上进行。

## 便利初始化器

便利初始化器是类（结构体、枚举）的次要初始化器，作用是使类（结构体、枚举）在初始化时更方便设置相关的属性（成员变量）。便利初始化器里面最后都需要调用自身的指定初始化器。

## 核心原则

1. 必须至少有一个指定初始化器，在指定初始化器里保证所有非可选类型属性都得到正确的初始化（有值）
2. 便利初始化器必须调用其他初始化器，使得最后肯定会调用指定初始化器

如果文字不好理解，可以根据下面的图，进行理解：

![&#x6838;&#x5FC3;&#x539F;&#x5219;&#x56FE;&#x89E3;](https://docs.swift.org/swift-book/_images/initializerDelegation02_2x.png)

## Objective-C 和 Swift 的差异

### Objective-C

`Objective-C` 在初始化时，会**自动给每个属性（成员变量）赋值为 0 或者 nil**，没有强制要求额外为每个属性（成员变量）赋值，**方便的同时也缺少了代码的安全性**。

`Objective-C` 中的指定初始化器会在后面被 `NS_DESIGNATED_INITIALIZER` 修饰，以下为 `NSObject` 和 `UIView` 的指定初始化器：

```text
// NSObject
@interface NSObject <NSObject>
- (instancetype)init
#if NS_ENFORCE_NSOBJECT_DESIGNATED_INITIALIZER
    NS_DESIGNATED_INITIALIZER
#endif
    ;
@end

// UIView
@interface UIView : UIResponder
- (instancetype)initWithFrame:(CGRect)frame NS_DESIGNATED_INITIALIZER;
- (nullable instancetype)initWithCoder:(NSCoder *)coder NS_DESIGNATED_INITIALIZER;
@end
```

无论继承自什么类，都经常需要新的初始化方法，而这个新的初始化方法其实就是新的指定初始化器。**如果存在一个新的指定初始化器，那么原来的指定初始化器就会自动退化成便利初始化器。为了遵循必须要调用指定初始化器的规则，就必须重写旧的定初始化器，在里面调用新的指定初始化器，这样就能确保所有属性（成员变量）被初始化。**

#### 举例

由于 UIView 拥有新的指定初始化器 `-initWithFrame:`，导致父类 `NSObject` 的指定初始化器 `-init` 退化成便利初始化器。所以当调用 `[[UIView alloc] init]` 时，`-init` 里面必然调用了 `-initWithFrame:`。

#### 建议

当存在一个新的指定初始化器的时候，推荐在方法名后面加上 `NS_DESIGNATED_INITIALIZER`，主动告诉编译器有一个新的指定初始化器，这样就可以使用 Xcode 自带的 Analysis 功能分析，找出初始化过程中可能存在的漏洞。

如果不想去重写旧的指定初始化器，但又不想存在漏洞和隐患，那么可以使用 `NS_UNAVAILABLE` 把旧的指定初始化器都废弃，外界就无法调用旧的指定初始化器。

### Swift

相对于 `Objective-C`，`Swift` 多了一些规则：

1. 初始化的时候需要保证类（结构体、枚举）的所有非可选类型属性都会有值，否则会报错
2. 在没有给所有非可选类型属性赋值（初始化完成）之前，不能调用 self 相关的任何东西，例如：调用实例属性，调用实例方法

#### 不存在继承

这种情况处理就十分简单，自己里面的 `init` 方法就是它的指定初始化器，而且可以随意创建多个它的指定初始化器。如果需要创建便利初始化器，则在方法名前面加上 `convenience`，且在里面必须调用其他初始化器，使得最后肯定调用指定初始化器。

```swift
class Student: Person {
    var score: Double = 100
}
```

#### 存在继承

如果**子类没有新的非可选类型属性，或者保证所有非可选类型属性都已经有默认值**，则可以直接继承父类的指定初始化器和便利初始化器。

如果**子类有新的非可选类型属性，或者无法保证所有非可选类型属性都已经有默认值**，则需要新创建一个指定初始化器，或者重写父类的指定初始化器。

* 新创建一个指定初始化器，会覆盖父类的指定初始化器，需要先给当前类所有非可选类型属性赋值，然后再调用父类的指定初始化器
* 重写父类的指定初始化器，需要先给当前类所有非可选类型属性赋值，然后再调用父类的指定初始化器
* 在保证子类有指定初始化器，才能创建便利初始化器，且在便利初始化器里面必须调用指定初始化器

```swift
class Student: Person {
    var score: Double
    // 新的指定初始化器，如果有新的指定初始化器，就不会继承父类的所有初始化器，除非重写
    init(name: String, age: Int, score: Double) {
        self.score = score
        super.init(name: name, age: age)
    }
    // 重写父类的指定初始化器，如果不重写，则子类不存在这个方法
    override init(name: String, age: Int) {
        score = 100
        super.init(name: name, age: age)
    }
    // 便利初始化器
    convenience init(name: String) {
        // 必须要调用自己的指定初始化器
        self.init(name: name, age: 10, score: 100)
    }
}
```

需要注意的是，**如果子类重写父类所有指定初始化器，则会继承父类的便利初始化器。**原因也是很简单，因为父类的便利初始化器，依赖于自己的指定初始化器。

#### 可失败的初始化器

可失败的初始化器（Failable Initializers），表示在某些情况下会创建实例失败。只有在表示创建失败的时候才有返回值，并且返回值为 `nil`。

子类可以把父类的可失败的初始化器重写为不可失败的初始化器，但不能把父类的不可失败的初始化器重写为可失败的初始化器。

```swift
class Animal {
    let name: String
    // 可失败的初始化器，如果把 ! 换成 ?，则为隐式的可失败的初始化器
    init?(name: String) {
        if name.isEmpty {
            return nil
        }
        self.name = name
    }
}
class Dog: Animal {
    override init(name: String) {
        if name.isEmpty {
            super.init(name: "旺财")!
        } else {
            super.init(name: name)!
        }
    }
}
```

#### 必须的初始化器

可以使用 `required` 修饰初始化器，来指定子类必须实现该初始化器。需要注意的是，如果子类可以直接继承父类的指定初始化器和便利初始化器，也就可以不用额外实现 required 修饰的初始化器。

> Title: 类的初始化方法
>
> Date: 2019.12.05
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onntztzf](https://github.com/onntztzf)
