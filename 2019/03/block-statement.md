# Block 的声明方式

原文链接：[How Do I Declare A Block in Objective-C?](http://fuckingblocksyntax.com)

* 局部变量

  ```text
    returnType (^blockName)(parameterTypes) = ^returnType(parameters) {...};
  ```

* 属性

  ```text
    @property (nonatomic, copy, nullability) returnType (^blockName)(parameterTypes);
  ```

* 方法参数

  ```text
    - (void)someMethodThatTakesABlock:(returnType (^nullability)(parameterTypes))blockName;
  ```

* 方法调用的参数

  ```text
    [someObject someMethodThatTakesABlock:^returnType (parameters) {...}];
  ```

* C 函数的参数

  ```text
    void SomeFunctionThatTakesABlock(returnType (^blockName)(parameterTypes));
  ```

* 类型定义

  ```text
    typedef returnType (^TypeName)(parameterTypes);
    TypeName blockName = ^returnType(parameters) {...};
  ```

> Title: Block 的声明方式
>
> Date: 2019.03.10
>
> Author: zhangpeng
>
> Github: [https://github.com/2hangpeng](https://github.com/2hangpeng)
