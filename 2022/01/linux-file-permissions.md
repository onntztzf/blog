# 搞懂 Linux 的文件权限

![permission denied](https://file.zhangpeng.site/2022/01/27/1.png)

`permission denied` 这个错误应该很多人都见到过，一般常见于执行脚本、读写文件等。它是什么原因造成的？我们又该如何解决它？本文将带给你答案。如果迫不及待地想要看解决办法，请直接翻到本文最下方。

## 问题的本质

这个问题的本质是**当前用户或者当前用户组没有执行该文件的权限**。`Linux` 系统是一种[多用户系统](https://www.runoob.com/linux/linux-user-manage.html)，不同的用户处于不同的地位，拥有不同的权限。文章开头的 `case` 便是执行用户缺少执行该文件的权限。

常见的权限有：**可读权限、可写权限、可执行权限**等。

## 如何查看文件权限

使用 `ll` 或 `ls -l` 命令，即可输出[文件的属性](https://www.runoob.com/linux/linux-file-attr-permission.html)。

```shell
➜  temp ll
total 32
-rwxr-xr-x  1 zhangpeng  staff       10K 10 29 19:41 init_dotfiles.sh
-rwxr-xr-x  1 zhangpeng  everyone   664B 11  1 13:15 reset.sh
```

### 文件的属主及属组

执行上面命令输出内容的第三部分和第四部分分别表示文件的所有者（后文简称属主）和文件的所属组（后文简称属组）。如上面输出：

`reset.sh` 的属主是 `zhangpeng`，属组是 `everyone`。

### 文件权限

文件的权限可以从第一部分的字符中解读：

![图片](https://www.runoob.com/wp-content/uploads/2014/08/file-permissions-rwx.jpg)

第 1 位代表类型，用来表示这个文件是目录、文件或链接文件等等。常见的有两种：

- `-` 文件
- `d` 目录

接下来的 9 位字符中，每三个分成一组，分别表示属主权限、文件所属组权限，其他用户权限。即：

- 第 2-4 位表示属主的权限
- 第 5-7 位表示属组的权限
- 第 8-10 位表示其他用户的权限

其中，`r` 代表可读权限、`w` 代表可写权限、`x` 代表可执行权限，这三个权限的位置不会改变，如果没有某权限，那对应位置就会变成 `-`。

## 如何修改文件权限

![图片](https://www.runoob.com/wp-content/uploads/2014/08/rwx-standard-unix-permission-bits.png)

如果想要修改文件的权限，需要使用 [`chmod`](https://www.runoob.com/linux/linux-comm-chmod.html) 命令。`chmod` 命令有两种使用方式：符号模式和数字模式。

### 符号模式

符号模式是使用符号来设置文件或文件夹的权限。用到的符号有以下几种类型：

- 用户类型
    | 符号 | 用户类型    | 说明                                     |
    | ---- | ----------- | ---------------------------------------- |
    | u    | user        | 文件所有者                               |
    | g    | group       | 文件所属组                               |
    | o    | other users | 既不是文件所有者，也不在文件所属组的用户 |
    | a    | all         | 所有用户，相当于 ugo 的合集              |

- 操作类型
    | 符号 | 说明     |
    | ---- | -------- |
    | +    | 增加权限 |
    | -    | 去除权限 |
    | =    | 设置权限 |

- 权限类型
    | 符号 | 说明       |
    | ---- | ---------- |
    | r    | 可读权限   |
    | w    | 可写权限   |
    | x    | 可执行权限 |

    除了上面表格中的权限，还有一些不常用的，如：`X`，`s`，`t` 等，请自行查阅[相关信息](https://www.runoob.com/linux/linux-comm-chmod.html)。

### 数字模式

数字模式就是将上面提到的可读、可写、可执行分别对应到一个数字上，最终以一个八进制数来设置文件或文件夹不同用户类型的权限。对应关系：

| 权限类型 | 对应数字 | 说明       |
| -------- | -------- | ---------- |
| r        | 4        | 可读权限   |
| w        | 2        | 可写权限   |
| x        | 1        | 可执行权限 |
| -        | 0        | 无权限     |

### 举个例子

将文章开篇的提到的 `reset.sh` 设置为属主可读可写可执行，属组可读可执行，其他用户可执行。

- 符号模式：

    ```shell
    ➜  temp chmod u=rwx,g=rx,o=x reset.sh
    ➜  temp ll
    total 32
    -rwxr-xr-x  1 zhangpeng  staff    10K 10 29 19:41 init_dotfiles.sh
    -rwxr-x--x  1 zhangpeng  staff   664B 11  1 13:15 reset.sh
    ```

- 数字模式

    ```shell
    ➜  temp chmod 751 reset.sh
    ➜  temp ll
    total 32
    -rwxr-xr-x  1 zhangpeng  staff    10K 10 29 19:41 init_dotfiles.sh
    -rwxr-x--x  1 zhangpeng  staff   664B 11  1 13:15 reset.sh
    ```

## 总结

到此，对于文章开头提到的问题，大家心中应该已经有了答案。执行 `reset.sh` 文件时，提示 `permission denied`，是因为当前用户或当前用户组没有该文件的执行权限。因此解决方案也很简单：**使用 `chmod +x` 对文件添加可执行权限**，具体操作如下：

```shell
➜  temp chmod +x reset.sh
➜  temp ./reset.sh
macOS:
done.
```

######

如果觉得本篇文章不错，麻烦给个**点赞👍、收藏🌟、分享👊、在看👀**四连！

![干货输出机](https://file.zhangpeng.site/wechat/qrcode.jpg)
