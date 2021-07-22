# 如何解决端口占用问题

![图-1](https://img.zhangpeng.site/2021/07/20/1.png)

当我们启动某项服务时，经常会出现 **address already in use** 这个错误。该错误是指**当前使用的端口被某个进程占用，导致本次服务无法正常启动**。通常情况下，导致端口被占用的原因有两个：

1. 已启动的某个服务使用的也是这个端口
2. 当前服务在上次启动后没有正常退出

本⽂将告知⼤家如何解决该问题。

## 查看端口占用情况

首先，需要确认当前要用的端口目前被哪个进程占用。

- macOS

  打开终端，输入 `lsof -i :port`，将 `port` 换成端口号，如:`8080`

  ```shell
  $ lsof -i :8080
  COMMAND  PID      USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
  main    6667 zhangpeng    7u  IPv6 0x645a94383c79337f      0t0  TCP *:http-alt (LISTEN)
  ```

- Linux

  输入 `netstat -tunlp | egrep "PID|port"`，将 `port` 换成端口号，如:`8080`

  ```shell
  $ netstat -tunlp | egrep "PID|8080"
  Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
  tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      131/nginx: master p
  ```

- Windows

  1. 启动命令窗口

     同时点击 `windows` 和 `r` 键，在输入框输入 `cmd`，点击回车

  2. 在命令窗口中输入 `netstat -ano | findstr "PID port"`，将 `port` 换成端口号，如:`8080`

     ```shell
     $ netstat -ano | findstr "PID 8080"
     	协议  本地地址          外部地址        状态           PID
       TCP    0.0.0.0:8080           0.0.0.0:0              LISTENING       16248
       TCP    [::]:8080              [::]:0                 LISTENING       16248
       TCP    [::1]:8080             [::1]:51273            ESTABLISHED     16248
     ```

找到占用端口的进程后，需要**自行判断一下该进程能否被终止**。如果不可以，则需要换一个端口启动服务；如果可以，那么请继续往下阅读。

## 终止占用端口的进程

通过上文，已经找到了占用端口的进程。接下来，我们要终止它。

- macOS

  使用 `kill -9 PID` 命令终止占用端口的进程，将  `PID` 换成要终止的进程的 `PID`

  ```shell
  kill -9 6667
  ```

- Linux

  使用 `kill -9 PID` 命令终止占用端口的进程，将  `PID` 换成要终止的进程的 `PID`

  ```shell
  kill -9 131
  ```

- Windows

  使用 `taskkill /PID processid /t /f` 命令终止占用端口的进程，将  `processid` 换成要终止的进程的 `PID`

  ```shell
  taskkill /PID 16248 /t /f
  ```

到此，占⽤着我们端⼝的进程都已被终止，我们可以愉快的启动服务了。

> Title: 如何解决端口占用问题
>
> Date: 2021.07.22
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)
