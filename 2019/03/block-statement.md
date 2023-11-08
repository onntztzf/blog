# Block 的声明方式

原文链接：[How Do I Declare A Block in Objective-C?](http://fuckingblocksyntax.com)

* 局部变量

  ```objc
  returnType (^blockName)(parameterTypes) = ^returnType(parameters) {...};
  ```

* 属性

  ```objc
  @property (nonatomic, copy, nullability) returnType (^blockName)(parameterTypes);
  ```

* 方法参数

  ```objc
  - (void)someMethodThatTakesABlock:(returnType (^nullability)(parameterTypes))blockName;
  ```

* 方法调用的参数

  ```objc
  [someObject someMethodThatTakesABlock:^returnType (parameters) {...}];
  ```

* C 函数的参数

  ```objc
  void SomeFunctionThatTakesABlock(returnType (^blockName)(parameterTypes));
  ```

* 类型定义

  ```objc
  typedef returnType (^TypeName)(parameterTypes);
  TypeName blockName = ^returnType(parameters) {...};
  ```

> Title: Block 的声明方式
>
> Date: 2019.03.10
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onntztzf](https://github.com/onntztzf)
