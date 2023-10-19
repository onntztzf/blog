# 如何创建自己 module

我们为什么要创建自己的 `module`？原因有二：

1. 不用再一遍又一遍的写重复代码
2. 可以持续迭代优化我们写出的代码

希望在阅读本篇文章后，您可以成功创建出自己的 `module`。

## 创建 mymodule

1. 在 `GitHub` 中创建一个仓库  `mymodule`，然后 `clone` 到本地

    ```shell
    git clone git@github.com:2hangpeng/mymodule.git
    ```

2. 进入我们刚刚 `clone` 下来的仓库中

    ```shell
    cd mymodule && vim hello.go
    ```

3. 编写我们需要放入 `module` 中的代码

    ```go
    package mymodule

    import (
        "fmt"
    )

    func Hello(name string) string {
        return fmt.Sprintf("Hello, %s", name)
    }
    ```

4. 生成 `go.mod` 文件

    使用我们在第一步中创建的仓库，生成我们 `mymodule` 的 `go.mod`

    ```shell
    go mod init github.com/2hangpeng/mymodule
    ```

    生成后的文件内容如下：

    ```shell
    module github.com/2hangpeng/mymodule

    go 1.16
    ```

5. 将我们的刚刚编写的代码提交到 `github` 中

    ```shell
    git add . && git commit -m "init mymodule" && git push
    ```

代码推送成功后，`mymodule` 就已经创建完成了。

## 使用 mymodule

进入一个使用 `go mod` 进行包管理的项目，使用 `go get` 命令将 `mymodule` 包添加到依赖中，然后我们就可以使用 `mymodule` 包中的代码了。

1. 在项目中添加 `mymodule` 的依赖

    ```shell
    $ go get github.com/2hangpeng/mymodule
    go: downloading github.com/2hangpeng/mymodule v0.0.0-20211019160614-87837bdd5f7a
    ```

    此时查看 `go.mod` 文件，可以看到文件内多了一行 `mymodule` 的依赖。表示当前项目依赖 `mymodule` 的 `v0.0.0-20211019160614-87837bdd5f7a` 版本

    ```go
    require github.com/2hangpeng/mymodule v0.0.0-20211019160614-87837bdd5f7a // indirect
    ```

2. 使用 `mymodule` 中的方法

    ```go
    package main

    import (
     "fmt"

     "github.com/2hangpeng/mymodule"
    )

    func main() {
     fmt.Println(mymodule.Hello("jack"))
    }
    ```

## 创建版本

当有了稳定的或者准备长期使用的 `module` 后，我们就可以为它创建一个版本。`module` 的版本是由 `git` 的 `tag` 控制的，因此我们在代码仓库中添加 `tag`。

```shell
git tag v1.0.0
git push --tags
```

现在我们将 `go.mod` 中依赖的 `mymodule` 的版本改为 `v1.0.0`。然后执行下面的代码，这样就将项目中依赖的 `mymodule` 版本设置为 `v1.0.0` 了。

```shell
go get github.com/2hangpeng/mymodule
```

`go module` 的版本号规范可以参考 [Module version numbering](https://golang.org/doc/modules/version-numbers#pre-release-version) 这篇文章，在此就不多做赘述了。

## 最后

看到文章这个位置，您应该已经使用上了自己创建的 `module` 了。如果还没有，欢迎留言~

![图片](https://file.zhangpeng.site/wechat/qrcode.jpg)
