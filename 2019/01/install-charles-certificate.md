# Charles 安装证书

## Charles 是什么

`Charles` 是一个 `HTTP` 代理服务器, `HTTP` 监视器,反转代理服务器，当浏览器连接 `Charles` 的代理访问互联网时，`Charles` 可以监控浏览器发送和接收的所有数据。它允许一个开发者查看所有连接互联网的 `HTTP` 通信，这些包括 `request`, `response` 和 `HTTP headers`（包含cookies与caching信息）。

## Charles 能做什么

1. 抓取 http 和 https 的请求和响应，这是最常用的。
2. 重发网络请求，方便后端调试。
3. 修改网络请求参数（客户端向服务器发送的时候，可以修改后再转发出去）。
4. 网络请求的截获和动态修改。
5. 支持模拟慢速网络，主要是模仿手机上的2G/3G/4G的访问流程。
6. 支持本地映射和远程映射，比如你可以把线上资源映射到本地某个文件夹下，这样可以方便的处理一些特殊情况下的bug和线上调试（网络的css，js等资源用的是本地代码，这些你可以本地随便修改，数据之类的都是线上的环境，方面在线调试）。
7. 可以抓手机端访问的资源（如果是配置HOST的环境，手机可以借用host配置进入测试环境）。

## 安装证书

通过菜单拦中的选项，我们可以安装整数：

![Charles](http://img.zhangpeng.site/2019/01/02/1.jpg)

### 给 `PC` 安装证书

1. **安装证书**

   > Help -&gt; SSL Proxying -&gt; Install Charles Root Certificate

   在弹框中，根据自己的情况选择对应的钥匙串 ![Charles](http://img.zhangpeng.site/2019/01/02/2.jpg)

2. **信任证书**

   进入菜单，选择钥匙串访问，在搜索框中搜索 `Charles` ，找到 `Charles Proxy CA`。双击打开证书的信息界面，将红框中的选项改为始终信任。 ![Charles](http://img.zhangpeng.site/2019/01/02/3.jpg)

### 给 `iOS` 模拟器安装证书

1. **安装证书**

   > Help -&gt; SSL Proxying -&gt; Install Charles Root Certificate in iOS Simulators

2. **信任证书**

   > Settings -&gt; General -&gt; About -&gt; Certificate Trust Settings

   打开 `iOS Simulators` 的证书信任选项 ![Charles](http://img.zhangpeng.site/2019/01/02/4.jpg)

### 给手机安装证书

1. **安装证书**

   > Help -&gt; SSL Proxying -&gt; Install Charles Root Certificate on a Mobile Device or Remote Broswer

   ![Charles](http://img.zhangpeng.site/2019/01/02/5.jpg)

   1. 将手机和电脑都连接到同一无线局域网，进入无线局域网设置，手动设置代理
   2. 按照提示框中的提示, 在无线网设置中，将代理改为手动设置，按图中所示填写 `xxx.xx.xxx.xxx:xxxx`
   3. 使用手机浏览器访问 [chls.pro/ssl](https://github.com/2hangpeng/blog/tree/322c1a6adda8dd6be880c9622823871046e6654b/mac/chls.pro/ssl/README.md)，按照提示安装证书

      ![Charles](http://img.zhangpeng.site/2019/01/02/6.jpg)

2. **信任证书**

   > 设置 -&gt; 通用 -&gt; 关于本机 -&gt; 证书信任设置

   打开刚刚安装的证书的信任选项 ![Charles](http://img.zhangpeng.site/2019/01/02/7.jpg)

> Title: Charles 安装证书
>
> Date: 2019.01.02
>
> Author: zhangpeng
>
> Github: [https://github.com/2hangpeng](https://github.com/2hangpeng)
