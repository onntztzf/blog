# Go 基础

## 环境配置

1. [下载安装包](https://golang.google.cn/dl/)

2. 配置环境变量

   在您所使用的 `shell` 对应的配置文件中，添加下面的内容：

   ```shell
   export GOROOT="/usr/local/go"
   export GOPATH="$HOME/go"
   export PATH=$PATH:$GOPATH/bin
   # Enable the go modules feature
   export GO111MODULE=auto
   # Set the GOPROXY environment variable
   export GOPROXY=https://goproxy.io
   ```

完成上面的操作后，在终端输入 `go env`，输出下面内容，就表示 go 环境配置完成：

```shell
~ go env
GOARCH="amd64"
GOBIN=""
GOCACHE="/Users/zhangpeng/Library/Caches/go-build"
GOEXE=""
GOFLAGS=""
GOHOSTARCH="amd64"
GOHOSTOS="darwin"
GOOS="darwin"
GOPATH="/Users/zhangpeng/go"
GOPROXY="https://goproxy.io"
GORACE=""
GOROOT="/usr/local/go"
GOTMPDIR=""
GOTOOLDIR="/usr/local/go/pkg/tool/darwin_amd64"
GCCGO="gccgo"
CC="clang"
CXX="clang++"
CGO_ENABLED="1"
GOMOD=""
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -m64 -pthread -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fdebug-prefix-map=/var/folders/sk/qbbrttxx2j1d7bqf02wh90zm0000gn/T/go-build233880756=/tmp/go-build -gno-record-gcc-switches -fno-common"
```

## GOROOT & GOPATH

* **GOROOT**

  `Go` 的安装目录

  内置的包和函数，如 `fmt` 、`math`、`strings` 等都存储在这个目录的 `src` 文件夹中

* **GOPATH**

  `Go` 的工作目录

  **src:** 存放源代码。按照 `Go` 语言约定，`go run`，`go install` 等命令默认会在此路径下执行；

  **pkg:** 存放编译时生成的中间文件（ *.a ）；

  **bin:** 存放编译后生成的可执行文件 （ 在项目内执行 go install，会在 bin 目录下生成一个可执行文件）。

## 常用命令

* **go run**

  编译并执行，只能作用于命令源码文件，一般用于开发中快速测试。上文我们通过执行 go run test.go ，完成了程序的编译运行。

* **go build**

  编译代码包或者源码文件。如果带上代码包名，则表示编译指定的代码包；如果带上源码文件，则表示编译指定源码文件。

* **go get**

  下载第三方代码包并编译安装 ，需要注意的是，它会下载安装到 GOPATH 环境变量配置的第一个工作区中。

* **go install**

  这个命令用于编译安装，可以作用于 main 包和非 main 包，然后将编译后的生成的执行文件存放到工程的 bin 目录下，将生成的归档文件（即静态链接库）存放到工程的 pkg 目录下。使用方式类似于 go build，可以在某个代码包目录下直接使用，也可以指定代码包使用。

* **go env**

  用于打印 `GO` 语言的环境信息，如 `GOPATH` 是工作区目录，`GOROOT` 是 `GO` 语言安装目录，`GOBIN` 是通过 `go install` 命令生成可执行文件的存放目录（默认是当前工作区的 `bin` 目录下），`GOEXE` 为生成可执行文件的后缀

## 数据类型

布尔型，整型，浮点型，指针类型（Pointer）、数组类型、结构化类型(struct)、Channel 类型、函数类型、切片类型、接口类型（interface）、Map 类型

```go
// 布尔型
bool
// -------------------------------------------------------
// 整型
int8 int16 int32 int64
uint8 uint16 uint32 uint64
// -------------------------------------------------------
// 浮点型
float32 float64
// -------------------------------------------------------
// 字符串
string
// -------------------------------------------------------
// 结构体，结构体是由一系列具有相同类型或不同类型的数据构成的数据集合
// 用结构体可以表示一个具有某一特征的对象
type identifier struct {
  field1 type1
  field2 type2
}
// -------------------------------------------------------
// 数组，有序的元素序列
// 可以通过访问数组下标即可对数组元素进行赋值
var variable_name [SIZE] variable_type
// -------------------------------------------------------
// 切片，类似"动态数组"结构的数据类型
// 本质是一个数据结构，实现了对数组操作的封装。
var identifier []type
// -------------------------------------------------------
// map
// 如果不初始化 map，那么就会创建一个 nil map。nil map 不能用来存放键值对
// 对于 map 类型，一定要进行初始化再赋值
var map_variable map[key_data_type]value_data_type
```

## 变量声明赋值

1. 先声明，后赋值

   ```go
   // 声明变量，变量名放在类型前
   var name string
   // 赋值
   name = "test"
   ```

2. 声明并赋值

   ```go
   // 编译器会根据值自行判定变量类型
   // 方式 1
   var name = "test"
   // 方式 2
   name := "test"
   ```

常用类型初始化方式

```go
// 结构体
type Person struct {
  name string  // 姓名
  age uint32   // 年龄
  birth string  // 出生日期  用 yyyy/mm/dd 格式的字符串表示
  height float32  // 身高
  weight float32  // 体重
}
// 方式1，变量 t 是一个指向 Person 的指针，此时结构体字段的值是它们所属类型的零值
t := new(Person)
// 方式2，底层仍然会调用 new ()，这里值的顺序必须按照字段顺序来写
person : &Person {name : "juejin", age : 12}
//----------------------------------
// 初始化数组
var array = [5]string{ "go", "java", "c++" }
array = [10] int64 {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
//----------------------------------
// 初始化 int64 类型的切片
array = make([]int64, 10)
//----------------------------------
// map
dataMap := make(map[string]string)
```

## 条件语句

```go
/*
 * condition: 关系表达式或逻辑表达式，循环控制条件
 */
if condition {

}

eg.
if a == 10 {
  /* 如果条件为 true 则执行以下语句 */
  fmt.Println("a == 10" )
}

/*
 * statement: 可选语句部分，在条件判断之前运行
 * condition: 关系表达式或逻辑表达式，判断条件
 */
if statement; condition {

}

eg.
if a := 1  ;  a < 10 {
  // 如果条件为 true 则执行以下语句
  fmt.Println("a < 10" )
}
```

## 循环语句

方式 1

```go
/*
 * init： 一般为赋值表达式，给控制变量赋初值；
 * condition： 关系表达式或逻辑表达式，循环控制条件；
 * post： 一般为赋值表达式，给控制变量增量或减量。
 */
for init; condition; post {

}

eg.
for i :=1 ; i < 10 ; i ++ {
  fmt.Println("i = " , i)
}
```

方式2

```go
/*
 * condition： 关系表达式或逻辑表达式，循环控制条件
 */
for condition { }

eg.
for 0 == 0 {}
for true {}
```

方式3

```go
for { }

eg.
for {
  // 服务器监听 8080 端口
  server.Listen(8080)
}
```

## 函数

go 语言中的函数是支持多返回值的

```go
func function_name( [parameter list] ) [return_types] {
  // 函数体
}

eg.
// 此函数实现了取两个数最大值的功能
func max(a int32, b int32) int32 {
  if a > b {
    return a
  } else {
    return b
  }
}

// 此函数实现了取两个数最大值和最小值的功能
func getMaxAndMin(a int32, b int32) (int32, int32) {
  if a > b {
    return a, b
  } else {
    return b, a
  }
}
```

go 语言还有一种特殊的函数，叫做方法。一个方法就是一个包含了接受者的函数，接受者可以是命名类型或者结构体类型的一个值或者是一个指针。

```go
func (variable_name variable_data_type) function_name() [return_type]{
  /* 函数体*/
}

// 我们用 面向对象的思想实现一个封装的结构体
type Person struct{
  name string  // 姓名
  age uint32   // 年龄
}

// 获取姓名
func (p *Person) GetName() string{
  return p.name
}

// 获取年龄
func (p *Person) GetAge() uint32{
  return p.age
}

// 设置姓名
func (p *Person) SetName(name string) {
  p.name = name
}

// 设置年龄
func (p *Person) SetAge(age uint32) {
  p.age = age
}
```

## 异常处理

结合自定义的 error 类型给出一个使用 panic 和 recover 的完整例子：

```go
package main

import (
  "fmt"
)

// 定义除法运算函数
func Devide(num1, num2 int) int {
  if num2 == 0 {
    panic("num cannot be 0")
  } else {
    return num1 / num2
  }
}

func main() {
  var a, b int
  fmt.Scanf("%d %d", &a, &b)

  defer func() {
    if r := recover(); r != nil {
      fmt.Printf("panic的内容%v\n", r)
    }
  }()

  rs := Devide(a, b)
  fmt.Println("结果是：", rs)
}
```

## 权限控制

**在 go 语言中，是通过约定来实现权限控制的**。变量和方法都遵守驼峰式命名。变量和方法的首字母大写，相当于 `public`，变量和方法的首字母小写，相当于 `private`。同一个包中访问，相当于 `default` ，由于 `go` 语言没有继承，所以也没有 `protected` 权限。

## 继承

go 语言是没有继承的。但是 go 语言可以通过结构体之间的组合来实现类似继承的效果。

```go
package main
import "fmt"
type oo struct {
  inner
  ss1 string
  ss2 int
  ss3 bool
}
type inner struct {
  ss4 string
}
func (i *inner) testMethod () {
  fmt.Println("testMethod is called!!!")
}
func main()  {
  oo1 := new(oo)
  fmt.Println("ss4无值："+oo1.ss4)
  oo1.ss4 = "abc"
  fmt.Println("ss4已赋值"+oo1.ss4)
  oo1.testMethod()//继承调用
  oo1.inner.testMethod()//继承调用 这里也可以重写
}
```

## 多态

在 go 语言中，只要某个 struct 实现了某个 interface 的所有方法，那么我们就认为这个 struct 实现了这个类。

```go
package main
import (
  "fmt"
)
type Person interface {
  Sing ()
}
type Girl struct {
  Name string
}
type Boy struct {
  Name string
}
func (this *Girl) Sing () {
  fmt.Println("Hi, I am  " + this.Name)
}
func (this *Boy) Sing () {
  fmt.Println("Hi, I am  " + this.Name)
}
func main() {
  g := &Girl{"Lucy"}
  b := &Boy{"Dave"}

  p := map[int]Person{}
  p[0] = g
  p[1] = b

  for _, v := range p {
    v.Sing()
  }
}
```

---

> Title: Go 基础
>
> Date: 2019.07.20
>
> Author: zhangpeng
>
> Github: <https://github.com/gh-zhangpeng>
