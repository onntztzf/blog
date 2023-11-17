# 搭建 Hexo Blog

`Hexo` 需要 `Git` 和 `Node` 的支持，所以烦请各位想用 `Hexo` 搭建博客的同学自行安装 `Git` 和 `Node`，然后再来阅读本文档。

## 安装 `hexo` 脚手架

```text
➜  ~ npm install -g hexo-cli
/usr/local/bin/hexo -> /usr/local/lib/node_modules/hexo-cli/bin/hexo
+ hexo-cli@3.1.0
added 67 packages from 317 contributors in 6.685s
```

如果因为权限问题安装失败的，那么在命令前添加 `sudo`，输入密码后就可以安装了

![图片](https://file.zhangpeng.site/2017/11/26/1.png)

通过 `hexo -v` 可以检查 `hexo-cli` 是否安装成功

```shell
➜  ~ hexo -v
hexo-cli: 3.1.0
os: Darwin 19.0.0 darwin x64
node: 12.12.0
v8: 7.7.299.13-node.12
uv: 1.32.0
zlib: 1.2.11
brotli: 1.0.7
ares: 1.15.0
modules: 72
nghttp2: 1.39.2
napi: 5
llhttp: 1.1.4
http_parser: 2.8.0
openssl: 1.1.1d
cldr: 35.1
icu: 64.2
tz: 2019a
unicode: 12.1
```

## 创建 `hexo` 博客

通过终端进入您想要创建博客的文件夹中，执行初始化命令：

```shell
hexo init
```

![图片](https://file.zhangpeng.site/2017/11/26/2.png)

创建完毕后，我们可以看到生成了很多的文件及文件夹，如下：

![图片](https://file.zhangpeng.site/2017/11/26/3.png)

其中比较主要的有：

```shell
.
├── source          //用于存放博客的 markdown 文件，以及静态文件
│   └── _posts      //博客的 markdown 文件
├── themes          //存放博客主题
└── _config.yml     //我们博客的配置文件，可以配置 title、主题、发布地址等
```

到这里，博客基本算是创建完毕了。

## 预览博客

在终端中，执行 `hexo s` 启动服务器，我们就可以在浏览器中看到我们博客了。默认情况下，访问网址为 `http：//localhost：4000/`。

![图片](https://file.zhangpeng.site/2017/11/26/4.png)

## 发布博客

本章讲述的是将博客发布到 `GitHub` 上，如果想发布到自己的服务器上，请酌情修改，基本上大同小异。

### 建立一个博客仓库

1. 我们需要准备一个 `GitHub` 账号

   首先我们需要一个 `GitHub` 账号，我想大家应该都有这个吧，如果没有请自行申请，这里我就不做赘述了。

2. 创建一个用于存放博客的仓库

   ![图片](https://file.zhangpeng.site/2017/11/26/5.png)

   网上大多数的人都建议创建一个如图所示的项目，即`xxx.github.io`，红框中的内容与账户名保持一致。PS.忽略图中红色的报错，我这边报错是因为我已经创建了相同名字的项目✧(≖ ◡ ≖✿)

   **小声哔哔：**
   通过我的测试，其实项目起什么名字并不重要，都可以访问到，我觉得大多数人以`xxx.github.io`当项目名字，只是为了后期访问好看罢了🙄

### 安装博客发布工具

为了方便快捷的将我们本地的博客发布到 `GitHub` 上，建议大家安装 `hexo-deployer-git` 自动部署发布工具。

1. 安装插件

   在博客的根目录执行 `npm install hexo-deployer-git --save`

   ![图片](https://file.zhangpeng.site/2017/11/26/6.png)

2. 修改配置文件

   发布工具安装完毕后，我们还需要在`_config.yml`文件中配置一下我们的 `GitHub` 的地址，否则我们上传到哪去呢，是不是？<(￣︶￣)>

   打开`_config.yml`文件，搜索`deploy`，这个就是我们要配置的地方了，如果没有就在文件的最后添加下面的代码。

   ```text
   deploy：
    type： git
    repo：github 上的项目地址
   ```

   **注：**
   1.上面的配置中，冒号和你填写的内容间一定要有个空格，这是标准的格式，没得谈！！！
   2.有的同学可能会问可不可以发布到某个分支上，答案是不能。原因请看下图，箭头所指处，明确说明`User pages must be built from the master branch.`

   ![图片](https://file.zhangpeng.site/2017/11/26/7.png)

### 编译&部署博客

接下来就剩下发布这一步了，在终端中进入博客的根目录，执行：

```text
hexo clean && hexo g && hexo d
```

当您看到 `INFO Deploy done： git` 时，就说明您的博客成功发布到 `GitHub` 上了，通过访问 `http：//xxx.github.io/`，就可以访问到您的博客了，记得把 `xxx` 换成您的项目名。 ![图 8](https://file.zhangpeng.site/2017/11/26/8.png)

### 日常更新博客

当新写了博客文章，或者是修改了主题，仅需通过终端，进入本地博客的根目录，执行`hexo clean && hexo g && hexo d`。然后就可以在博客中看到最新的文章或是主题了。

## 参考资料

1. [Hexo Docs](https://hexo.io/docs/)

> Title: 搭建 Hexo Blog
>
> Date: 2017.11.26
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onnttf](https://github.com/onnttf)
