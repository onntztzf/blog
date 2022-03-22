# 神奇的位运算

## 位运算是什么

二进制是计算技术中广泛采用的一种数制。二进制数据是用 `0` 和 `1` 两个数码来表示的数。程序中的所有数在计算机内存中都是以二进制的形式储存的，而直接**对内存中的二进制数据进行操作就叫做位运算**。

## 位运算的运算方式

基本的位运算共 6 种，如下：

1. 按位与
2. 按位或
3. 按位异或
4. 按位取反
5. 左移
6. 右移

下面我们分别来讲讲。

### 按位与

运算符号：`&`

运算规则：相同位的两个数字都为 `1`，则为 `1`；若有一个不为 `1`，则为 `0`

运算示例：

```text
0 0 1 0 1 1 1 0   46
1 0 0 1 1 1 0 1   157
———————————————
0 0 0 0 1 1 0 0   12
```

### 按位或

运算符号：`|`

运算规则：相同位只要一个为 `1` 即为 `1`

运算示例：

```text
0 0 1 0 1 1 1 0   46
1 0 0 1 1 1 0 1   157
———————————————
1 0 1 1 1 1 1 1   191
```

### 按位异或

运算符号：`^`

运算规则：相同位不同则为 `1`，相同则为 `0`

运算示例：

```text
0 0 1 0 1 1 1 0   46
1 0 0 1 1 1 0 1   157
———————————————
1 0 1 1 0 0 1 1   179
```

### 按位取反

运算符号：`~`

运算规则：`~` 是一元运算符，用来对一个二进制数按位取反，即将 `0` 变 `1`，将 `1` 变 `0`

运算示例：

```text
0 0 1 0 1 1 1 0   46
———————————————
1 1 0 1 0 0 0 1   225
```

### 左移

运算符号：<<

运算规则：`a` << `b` 就表示把a转为二进制后左移 `b` 位（在后面添 `b` 个 `0`）。即各二进位全部左移若干位，高位丢弃，低位补 `0`

运算示例：

```text
0011 << 1 => 0110
```

### 右移

运算符号：>>

运算规则：各二进位全部右移若干位，对无符号数，高位补 `0`，有符号数，各编译器处理方法不一样，有的补符号位（算术右移），有的补 `0`（逻辑右移）

运算示例：

```text
0110 >> 1 => 0011
```

## 位运算在日常开发中应用

### 交换两个变量的值

有两个数字 `a` 和 `b`，如何不通过第三个变量交换 `a` 和 `b`的值？

1. `a^=b` 即 `a=(a^b)`;
2. `b^=a` 即 `b=b^(a^b)` ，由于^运算满足交换律，`b^(a^b)=b^b^a` 。由于一个数和自己异或的结果为0并且任何数与0异或都会不变的，所以此时b被赋上了 `a` 的值。
3. `a^=b` 就是 `a=a^b`，由于前面二步可知 `a=(a^b)`，b=a，所以 `a=a^b即a=(a^b)^a` 。故 `a` 会被赋上b的值。

代码如下：

```objc
int a = 10;
int b = 20;
if (a != b) {
   a ^= b;
   b ^= a;
   a ^= b;
}
NSLog(@"a: %@ -- b: %@", @(a), @(b));

// 输出结果为
// a: 20 -- b: 10
```

### 判断奇偶

我们可以根据最末位是0还是1来决定，为0就是偶数，为1就是奇数。因此可以用 `((a & 1) == 0)` 代替 `(a % 2 == 0)` 来判断数字是奇数还是偶数。

```text
for (int i = 0; i < 5; i++) {
   NSLog(@"i: %@, 是%@\n", @(i), (i & 1) ? @"奇数" : @"偶数");
}

// 输出结果为
// i: 0, 是偶数
// i: 1, 是奇数
// i: 2, 是偶数
// i: 3, 是奇数
// i: 4, 是偶数
```

### 变换符号

变换符号简单来讲就是正数变负数，负数变正数。通过对数字取反加 `1` 就可以完成符号的变换。

```text
int a = -10;
NSLog(@"a 变换符号后为：%@", @(~a + 1));

// 输出结果为
// a 变换符号后为：10
```

### 位移枚举

在 `iOS` 中，我们有两个枚举类型：`NS_OPTION` 和 `NS_ENUM`。他们两个的本质都是一样的，差异就在于**是否可以多选**。

* `NS_OPTION`：多个枚举值同时使用按位或 (`|`) 相加表示进行多选操作。位移不同位数得到值不同即数值代表的枚举值不同, 多个枚举同时使用仍具有唯一性。
* `NS_ENUM`：不可多选，唯一互斥性。

#### 位移枚举是什么

位移枚举是一种特殊的枚举，它和普通的枚举的差异就在于**是否可以多选**。

位移枚举的多个枚举值同时使用按位或(`|`)相加表示进行多选操作。位移不同位数得到值不同即数值代表的枚举值不同,多个枚举同时使用仍具有唯一性。

#### 举例

自定义一个视图 `AddLabelView` ，创建一个属性，用于定义在什么位置添加 `label` 。

```objc
// AddLabelView
typedef NS_OPTIONS(NSUInteger, AddLabelPosition) {
   AddLabelTopLeft    = 1 << 0,
   AddLabelTopRight   = 1 << 1,
   AddLabelBottomLeft  = 1 << 2,
   AddLabelBottomRight = 1 << 3,
   AddLabelAllCorners  = 1 << 4
};

@interface AddLabelView : UIView
@property (nonatomic, assign) AddLabelPosition addLabelPosition;
@end

@implementation AddLabelView
- (instancetype)initWithFrame:(CGRect)frame
{
   self = [super initWithFrame:frame];
   if (self) {
      self.backgroundColor = [UIColor greenColor];
   }
   return self;
}
- (void)setAddLabelPosition:(AddLabelPosition)addLabelPosition {
   if (addLabelPosition & AddLabelTopLeft) {
      UILabel *label = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, self.bounds.size.width * 0.5, self.bounds.size.height * 0.5)];
      label.text = @"1";
      label.textAlignment = NSTextAlignmentCenter;
      [self addSubview:label];
   }
   if (addLabelPosition & AddLabelTopRight) {
      UILabel *label = [[UILabel alloc] initWithFrame:CGRectMake(self.bounds.size.width * 0.5, 0, self.bounds.size.width * 0.5, self.bounds.size.height * 0.5)];
      label.text = @"2";
      label.textAlignment = NSTextAlignmentCenter;
      [self addSubview:label];
   }
   if (addLabelPosition & AddLabelBottomLeft) {
      UILabel *label = [[UILabel alloc] initWithFrame:CGRectMake(0, self.bounds.size.width * 0.5, self.bounds.size.width * 0.5, self.bounds.size.height * 0.5)];
      label.text = @"3";
      label.textAlignment = NSTextAlignmentCenter;
      [self addSubview:label];
   }
   if (addLabelPosition & AddLabelBottomRight) {
      UILabel *label = [[UILabel alloc] initWithFrame:CGRectMake(self.bounds.size.width * 0.5, self.bounds.size.width * 0.5, self.bounds.size.width * 0.5, self.bounds.size.height * 0.5)];
      label.text = @"4";
      label.textAlignment = NSTextAlignmentCenter;
      [self addSubview:label];
   }
   if (addLabelPosition & AddLabelAllCorners) {
      UILabel *label = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, self.bounds.size.width, self.bounds.size.height)];
      label.text = @"5";
      label.textAlignment = NSTextAlignmentCenter;
      [self addSubview:label];
   }
}
@end
```

创建一个我们自定义的视图，通过 `addLabelPosition`，控制我们在什么位置显示一个 `label` 。

```objc
AddLabelView *view = [[AddLabelView alloc] initWithFrame:CGRectMake(100, 100, 200, 200)];
view.addLabelPosition = AddLabelTopRight | AddLabelBottomRight | AddLabelBottomLeft;
[self.view addSubview:view];
```

通过上面的代码，您应该已经明白了位移枚举的多选是什么概念了，如果真的不明白，欢迎私信。

## 最后

希望本篇文章的位运算介绍可以给你带来收获，在日常工作中利用它更简单的解决问题。

## 

如果觉得本篇文章不错，麻烦给个**点赞👍、收藏🌟、分享👊、在看👀**四连！

![干货输出机](https://img.zhangpeng.site/wechat/qrcode.jpg)
