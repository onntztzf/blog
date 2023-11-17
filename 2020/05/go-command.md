# Go 1.13 中 Go command 修改

`go1.13` 已经发布了一个多月了，本次的大部分修改都是工具链、运行时和核心库。而本文主要是记录的命令行的修改。

## go env

`go env` 添加几个新的参数，使修改环境变量变得更方便快捷。

### -w

设置环境变量，通过此方式设置的默认值存储在 [os.UserConfigDir()](https://golang.org/pkg/os/#UserConfigDir) 中的 `go/env` 文件中。

### -u

取消以前设置的默认变量

## go version

现在 `go version` 命令的参数既可以是可执行文件又可以是项目目录。如果在 `go version` 命令中加上 `-m` 参数，则会打印可执行文件的引用模块的相关版本信息。

* 可执行文件

  打印用于构建该可执行文件的 `go sdk` 版本。

  ```text
  ➜  GoProject go version ./GoProject
  ./GoProject: go1.13.1
  ➜  GoProject go version -m ./GoProject
  ./GoProject: go1.13.1
   path GoProject
   mod GoProject (devel)
   dep github.com/gin-contrib/sse v0.0.0-20190301062529-5545eab6dad3 h1:t8FVkw33L+wilf2QiWkw0UV77qRpcH/JHPKGpKa2E8g=
   dep github.com/gin-gonic/gin v1.4.0 h1:3tMoCCfM7ppqsR0ptz/wi1impNpT7/9wQtMZ8lr1mCQ=
   dep github.com/golang/protobuf v1.3.1 h1:YF8+flBXS5eO826T4nzqPrxfhQThhXl0YzfuUPu4SBg=
   dep github.com/mattn/go-isatty v0.0.7 h1:UvyT9uN+3r7yLEYSlJsbQGdsaB/a0DlgWP3pql6iwOc=
   dep github.com/ugorji/go v1.1.4 h1:j4s+tAvLfL3bZyefP2SEWmhBzmuIlH/eqNuPdFPgngw=
   dep gopkg.in/go-playground/validator.v8 v8.18.2 h1:lFB4DoMU6B626w8ny76MV7VX6W2VHct2GVOI3xgiMrQ=
   dep gopkg.in/yaml.v2 v2.2.2 h1:ZCJp+EgiOT7lHqUV2J862kp8Qj64Jo6az82+3Td9dZw=
  ```

* 项目目录

  打印目录及其子目录中包含的可执行文件的信息。

  ```text
  ➜  GoProject go version .
  GoProject: go1.13.1
  ➜  GoProject go version -m .
  GoProject: go1.13.1
   path GoProject
   mod GoProject (devel)
   dep github.com/gin-contrib/sse v0.0.0-20190301062529-5545eab6dad3 h1:t8FVkw33L+wilf2QiWkw0UV77qRpcH/JHPKGpKa2E8g=
   dep github.com/gin-gonic/gin v1.4.0 h1:3tMoCCfM7ppqsR0ptz/wi1impNpT7/9wQtMZ8lr1mCQ=
   dep github.com/golang/protobuf v1.3.1 h1:YF8+flBXS5eO826T4nzqPrxfhQThhXl0YzfuUPu4SBg=
   dep github.com/mattn/go-isatty v0.0.7 h1:UvyT9uN+3r7yLEYSlJsbQGdsaB/a0DlgWP3pql6iwOc=
   dep github.com/ugorji/go v1.1.4 h1:j4s+tAvLfL3bZyefP2SEWmhBzmuIlH/eqNuPdFPgngw=
   dep gopkg.in/go-playground/validator.v8 v8.18.2 h1:lFB4DoMU6B626w8ny76MV7VX6W2VHct2GVOI3xgiMrQ=
   dep gopkg.in/yaml.v2 v2.2.2 h1:ZCJp+EgiOT7lHqUV2J862kp8Qj64Jo6az82+3Td9dZw=
  ```

## go build

### -trimpath

从编译的可执行文件中删除所有文件系统路径，以提高构建的可重复性。

### -o

如果传入一个目录，则会将可执行文件写入该文件夹。

## 参考资料

1. [Go 1.13 Release Notes](https://golang.org/doc/go1.13)
2. [UserConfigDir](https://golang.org/pkg/os/#UserConfigDir)

> Title: Go 1.13 中 Go command 修改
>
> Date: 2020.05.07
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onnttf](https://github.com/onnttf)
