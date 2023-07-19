# URI、URL、URN 的差异与联系

![URI&#x3001;URL&#x3001;URN](http://file.zhangpeng.site/2018/02/24/1.png)

在开发过程中，经常见到有同事把链接命名为 `uri_xxx_yyy` 或者 `url_xxx_yyy`，可是`uri`和`url`分别是什么意思呢？希望在阅读这篇文章后，您可以明白～

## URI

**`URI`**全称为 `Universal Resource Identifier`，统一资源标识符，用来唯一的标识一个资源。

在电脑术语中，统一资源标识符（Uniform Resource Identifier，或URI\)是一个用于**标识某一互联网资源名称**的字符串。 该种标识允许用户对任何（包括本地和互联网）的资源通过特定的协议进行交互操作。`URI` 由包括确定语法和相关协议的方案所定义。Web上可用的每种资源（HTML文档、图像、视频片段、程序等）由一个通用资源标识符（Uniform Resource Identifier, 简称"URI"）进行定位。

通常由下面几部分组成：

1. 访问资源的命名机制
2. 存放资源的主机名
3. 资源自身的名称，由路径表示，着重强调于资源。

## URL

**`URL`**全称为 `Universal Resource Locator`，统一资源定位符，用来**标识一个资源**。

`URL` 通常以协议`(http)`开头，包含网络主机名 `(example.com)` 和文档路径 `(/foo/mypage.html)` 等信息。`URL` 还可能具有查询参数和锚点标识符。

统一资源定位符是对可以从互联网上得到的资源的位置和访问方法的一种简洁的表示，是互联网上标准资源的地址。互联网上的每个文件都有一个唯一的URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它。

通常由下面几部分组成：

1. 协议\(或称为服务方式\)
2. 存有该资源的主机IP地址\(有时也包括端口号\)
3. 主机资源的具体地址。如目录和文件名等

## URN

**`URN`**全称为 `Universal Resource Name`，统一资源名称，用来定位的**标识一个资源**。

通过唯一且持久的名称来标识资源，但不一定告诉你如何在互联网上找到它。

`URN`不仅限于识别文件，还可以识别想法和概念。当`URN`确实代表文档时，可以通过“解析器”将其翻译成URL。然后可以从`URL`下载文档。

统一资源名称 \(Uniform Resource Name, URN\)，唯一标识一个实体的标识符，但是不能给出实体的位置。系统可以先在本地寻找一个实体，在它试着在Web上找到该实体之前。它也允许Web位置改变，然而这个实体却还是能够被找到。

通常以前缀urn开头

## 区别与联系

首先我们要弄清楚一件事：**`URL` 和 `URN` 都是 `URI` 的子集。** 换言之，`URL` 和 `URN`都是 `URI`，但是 `URI` 不一定是 `URL` 或者 `URN`。为了更好的理解这个概念，看下面这张图片。

![URI&#x3001;URL&#x3001;URN](http://file.zhangpeng.site/2018/02/24/2.jpg)

`URI` 负责识别，`URL` 负责定位;然而，定位符也是标识符的一种，因此每个 `URL` 都是 `URI`，但是每个 `URI` 并不全是 `URL`。

二者的区别在于，URI表示请求服务器的路径，定义这么一个资源。而URL同时说明要如何访问这个资源（`http://`）。

一句话解释：`URI` 和 `URL` 都定义了 `what the resource is`。URL 还定义了 `how to get the resource`。

可以举个例子解释：

身份证号：类似于 `URI`，通过身份证号能让我们能且仅能确定一个人。

身份证地址：类似于URL://地球/中国/浙江省/杭州市/西湖区/某大学/14号宿舍楼/525号寝/张三.人可以看到，这个字符串同样标识出了唯一的一个人，起到了`URI`的作用，所以`URL`是`URI`的子集。

## 参考资料

[W3C-URIs, URLs, and URNs](https://www.w3.org/TR/uri-clarification/)

[HTTP 协议中 URI 和 URL 有什么区别？](https://www.zhihu.com/question/21950864)

[这三个你懂不懂？URL & URI & URN](https://www.jianshu.com/p/cb0dbbf2fd15)

[URL 和 URI 有什么不同?](https://www.zhihu.com/question/19557151)

> Title: URI、URL、URN 的差异与联系
>
> Date: 2018.02.24
>
> Author: zhangpeng
>
> Github: [https://github.com/2hangpeng](https://github.com/2hangpeng)

