<!-- Date: 2020.03.01 -->

# 如何保持 SSH 服务不掉线

常见的保持 `SSH` 服务不掉线的方法有两种：

1. 服务端发送心跳包
2. 客户端发送心跳包  

本篇文章将**以 `Ubuntu 18.04.4 LTS` 为例**，分别对以上两种方法进行讲解。

## 服务端发送心跳包

1. 登陆您的服务器后，打开 **/etc/ssh/sshd\_config** 文件。
2. 将 `ClientAliveInterval` 和 `ClientAliveCountMax` 前面的 \# 去掉。（如果没有则添加这两个字段）
3. 将 `ClientAliveInterval` 的值修改为 60，`ClientAliveCountMax` 的值修改为 6
4. 保存上述修改，如果提示 `'readonly' option is set (add ! to override)`，请以系统管理者的身份执行指令。
5. 重启 `SSH` 服务

> **ClientAliveInterval** 服务器端向客户端请求消息的时间间隔，单位为秒，默认是 0，不发送  
> **ClientAliveCountMax** 服务器发出请求后，客户端没有响应的重试次数，到达次数后断开

## 客户端发送心跳包

1. 进入客户端的 `~/.ssh/` 文件夹
2. 打开 `config` 文件，如果没有请创建
3. 在 `config` 文件中添加以下内容，然后保存

   ServerAliveInterval 20

   ServerAliveCountMax 999

> **ServerAliveInterval** 客户端向服务器端请求消息的时间间隔，单位为秒，默认是 0，不发送  
> **ServerAliveCountMax** 客户端发出请求后，服务器没有响应的重试次数，到达次数后断开

## 总结

两种方式均可以实现 `SSH` 服务不掉线，可以根据自己的情况进行选择。

* 一台服务器，多台客户端

  可以在用服务端发送心跳包的方法。这样就不需要在每台客户端上进行修改。

* 一台客户端，多台服务器

  可以在用客户端发送心跳包的方法。这样就不需要在每台服务器上进行修改。

## 

如果觉得本篇文章不错，麻烦给个**点赞👍、收藏🌟、分享👊、在看👀**四连！

![干货输出机](https://img.zhangpeng.site/wechat/qrcode.jpg)
