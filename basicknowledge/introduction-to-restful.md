# RESTful 笔记

## REST 是什么

> `REST` 这个词是出自 [Roy Thomas Fielding](https://en.wikipedia.org/wiki/Roy_Fielding) 的一篇[论文](https://link.zhihu.com/?target=http%3A//www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)，如果有兴趣了解，可以查阅 [REST相关章节](https://link.zhihu.com/?target=http%3A//www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)。

`REST`，并不是简单的四个字母，它是 `Representational State Transfer` 的缩写，可译为"表现层状态转化”。

看不懂没关系，在前面加一个 `Resource`，就可以很好的理解了：**资源在网络中以某种表现形式进行状态转移**

* Resource

  这边的 `Resource` 指的就是我们的资源、数据等，可以用一个URI（统一资源定位符）指向它，每种资源对应一个特定的URI。要获取这个资源，访问它的URI就可以，因此URI就成了每一个资源的地址或独一无二的识别符。

* Representational

  资源的表现形式，比如我们常见的：

  ```text
    数据：HTML格式、XML格式、JSON格式、二进制格式等；

    图片：JPG格式、PNG格式等；
  ```

  具体表现形式，在 `HTTP` 请求的头信息中用 `Accept` 和 `Content-Type` 字段指定

* State Transfer

  客户端和服务器的一个互动过程，势必涉及到数据和状态的变化。

  互联网通信协议HTTP协议，是一个无状态协议。这意味着，所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器端发生"状态转化"。而这种转化是建立在表现层之上的，所以就是"表现层状态转化"。

## RESTful API

> 遵守了 `REST` 原则的 API

### 特点

* 每个URL表示一种资源
* URL语义清晰明确，不出现动词，只有名词复数（操作的动词是通过请求方式来表示）
* 使用HTTP的方法来表示对资源的增删改查
  * GET（常用）：从服务器上获取一个具体的资源或者一个资源列表。**安全且幂等**
  * POST（常用）： 在服务器上创建一个新的资源。**不安全且不幂等**
  * PUT（常用）：以整体的方式更新服务器上的一个资源。**不安全但幂等**
  * DELETE（常用）：删除服务器上的一个资源。**不安全但幂等**
  * PATCH：只更新服务器上一个资源的一个属性。
  * HEAD： 获取一个资源的元数据，如数据的哈希值或最后的更新时间
  * OPTIONS：获取客户端能对资源做什么操作的信息。
* 使用HTTP的状态来表示结果
  * 200 OK
  * 400 Bad Request
  * 500 Internal Server Error

> 幂等：无边际效应，多次操作得到相同的结果

简单来讲就是：

1. 看 `Url` 就知道要什么
2. 看 `http method` 就知道干什么
3. 看 `http status code` 就知道结果如何

### 优点

* 透明性，暴露资源存在。
* 充分利用 HTTP 协议本身语义。
* 无状态，这点非常重要。在调用一个接口（访问、操作资源）的时候，可以不用考虑上下文，不用考虑当前状态，极大的降低了复杂度HTTP。
* 本身提供了丰富的内容协商手段，无论是缓存，还是资源修改的乐观并发控制，都可以以业务无关的中间件来实现。

## 附

1. [理解RESTful架构](https://www.ruanyifeng.com/blog/2011/09/restful.html)
2. [RESTful API 编写指南](https://juejin.im/post/57d168e9bf22ec005f98a3a5)
3. [如何给老婆解释什么是RESTful](https://zhuanlan.zhihu.com/p/30396391)
4. [GitHub API](https://developer.github.com/v3/#client-errors)
5. [Microsoft REST API Guidelines](https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md)

> Title: RESTful 笔记
>
> Date: 2019.03.26
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)

