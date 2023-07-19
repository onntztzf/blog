# Shebang 是什么？

`Shebang` 是一种在 `Unix` 和 `Linux` 系统中使用的特殊注释，通常用于指定脚本文件的解释器。在本文中，我们将详细介绍 `Shebang` 的作用、语法和示例，以帮助您更好地了解它。

## Shebang 的作用

当您在 `Unix` 或 `Linux` 系统中执行一个可执行文件时，系统会尝试使用默认解释器来执行该文件。例如，如果您运行一个以 `.sh` 结尾的脚本文件，系统会默认使用 `/bin/bash` 解释器来执行该脚本。但是，有时您可能想要使用其他解释器来执行脚本文件，例如 `Python`，这时 `Shebang` 就派上用场了。

使用 `Shebang`，您可以在脚本文件的第一行添加一条注释，告诉系统要使用哪个解释器来执行该脚本。例如，如果您想使用 `bash` 来执行脚本文件，您可以在该文件的第一行添加如下注释：

```bash
#!/bin/bash
```

这条注释告诉 `shell` 查找 `bash` 解释器，然后使用找到的解释器执行该脚本。

## Shebang 的语法

`Shebang` 的语法非常简单。它只需要在文件的第一行添加一个井号 (#) 和一个惊叹号 (!)，紧接着是解释器的完整路径或可执行文件名。例如：

```python
#!/usr/bin/python

print("公众号：干货输出机")
```

或者：

```python
#!/usr/bin/env python

print("公众号：干货输出机")
```

在第二个例子中，我们使用 `env`。那么，使用 `env` 和不使用 `env` 的区别在哪里呢？

### 使用 env

使用 `env` 可以使**脚本更加可移植。** 因为它会使用环境变量中的 `PATH` 变量来查找解释器，而不是硬编码解释器的路径。这样，即使解释器在不同的系统上安装在不同的路径上，也可以确保脚本在任何地方都能够正常运行。

但是由于从环境变量中寻找解释器，会**造成一定的安全隐患。** 因为我们可以伪造一个假的命令，写入到环境变量中靠前的位置，这样，脚本就会使用我们伪造的解释器执行。

### 不使用 env

如果你确定脚本将在特定的系统上运行，并且已经知道了解释器的确切路径，那么可以直接在 `Shebang` 中使用解释器的路径，这样可以避免在环境变量中寻找解释器。

因此，使用 `env` 还是直接使用解释器路径取决于你的需求和具体情况。

## Shebang 的示例

在日常工作中，我们经常需要远程登录到服务器上进行管理操作。为了方便起见，我们可以编写脚本来实现自动化操作，这样可以提高工作效率并减少错误。

```bash
#!/usr/bin/expect -f

# setting the timeout period
set timeout 30

# use ssh login your jump server
spawn ssh [lindex $argv 1]@[lindex $argv 0]
# start expect
expect {
      "*yes/no*?"
      {send "yes\r";exp_continue;}
      "*assword:*"
      { send "[lindex $argv 2]\r" }
}
interact
```

上面的脚本就是一个使用 `expect` 编写的自动化远程登录脚本。在这个脚本中，我们使用了 `expect` 的自动交互功能，实现了自动化远程登录的功能。下面解释一下这个脚本内容：

首先，我们使用 `Shebang` 指定了解释器为 `expect`，然后将执行脚本的超时时间设置为 `30` 秒。然后，我们使用 `spawn` 命令根据用户输入的内容启动 `ssh` 进程。接下来，我们使用 `expect` 命令来等待 `ssh` 进程输出的信息，并根据输出的信息来发送相应的命令。在这个脚本中，我们使用了两个 `expect` 匹配规则：

1. 用于检测 `ssh` 连接时出现的询问信息，如果出现了类似 `Are you sure you want to continue connecting (yes/no)?` 的信息，就会自动发送 `yes` 命令确认连接。如果没有出现这样的信息，则继续等待。
2. 用于检测 `ssh` 登录时出现的密码输入提示信息。如果出现了 `password:` 的提示信息，则会自动发送密码给远程服务器进行登录。如果没有出现这样的信息，则继续等待。

最后，我们使用 `interact` 命令将控制权交还给用户，以便用户手动操作远程服务器。

使用方法：

1. 将上面的代码保存到 `ssh_login.sh` 文件中
2. 使用 `chmod` 命令给这个文件添加执行权限

   ```shell
   chmod +x ssh_login.sh
   ```

3. 然后执行这个文件时，在后面补上机器ip，需要登录的用户及密码

   ```shell
   ➜  Desktop ./ssh_login.sh 1.2.3.4 ubuntu Abc12345
   spawn ssh ubuntu@1.2.3.4
   The authenticity of host '1.2.3.4 (1.2.3.4)' can't be established.
   ED25519 key fingerprint is SHA256:G2QvR/KLSRunuijt2J+K5nra5to9CWL6OSHnRndwCI0.
   This key is not known by any other names
   Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
   Warning: Permanently added '1.2.3.4' (ED25519) to the list of known hosts.
   ubuntu@1.2.3.4's password:
   Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.15.0-56-generic x86_64)

   * Documentation:  https://help.ubuntu.com
   * Management:    https://landscape.canonical.com
   * Support:      https://ubuntu.com/advantage

   System information as of Mon Feb 27 07:47:16 PM CST 2023

   System load:  0.17822265625    Processes:          105
   Usage of /:   7.1% of 49.10GB   Users logged in:      0
   Memory usage: 27%            IPv4 address for eth0: 1.2.3.4
   Swap usage:   0%

   * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

   To run a command as administrator (user "root"), use "sudo <command>".
   See "man sudo_root" for details.

   ubuntu@VM-0-15-ubuntu:~$
   ```

## 总结

`Shebang` 是一种非常有用的工具，可让您指定脚本文件的解释器。使用 `Shebang`，您可以轻松地在 `Unix` 和 `Linux` 系统中执行各种类型的脚本，例如 `Python`、`Bash` 等。希望这篇文章能够帮助您更好地理解 `Shebang` 的作用和语法，并且能够在实际使用中提供帮助。

######

如果觉得本篇文章不错，麻烦给个**点赞👍、收藏🌟、分享👊、在看👀**四连！

![干货输出机](https://file.zhangpeng.site/wechat/qrcode.jpg)
