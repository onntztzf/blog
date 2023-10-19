# +load 与 +initialize

|  | +load | +initialize |
| :--- | :--- | :--- |
| 调用方式 | 根据函数地址直接调用 | 通过 objc_msgSend 调用 |
| 调用时刻 | 类、分类加载时调用 | 类第一次接收到消息的时候调用 |

## +load

1. 按照编译先后顺序调用
2. 先调用父类的 `+load` 再调用子类的 `+load`
3. 最后调用分类的 `+load` 方法

**调用方式：** 通过函数指针指向函数，拿到函数地址，分开来直接调用。

## +initialize

1. 先调用父类的 `+initialize`，再调用子类的 `+initialize`；(先初始化父类，再初始化子类，每个类只会初始化 1 次）
2. 子类内部 `+initialize` 会主动调用父类的 `+initialize`

**调用方式：** 通过 `objc_msgSend` 调用。

> Title: +load 与 +initialize
>
> Date: 2019.03.11
>
> Author: zhangpeng
>
> Github: [https://github.com/2hangpeng](https://github.com/2hangpeng)
