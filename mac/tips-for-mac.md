# Mac 的日常使用

* [Mac 的日常使用](tips-for-mac.md#mac-的日常使用)
  * [显示/隐藏隐藏文件](tips-for-mac.md#显示隐藏隐藏文件)
  * [设置一位的密码](tips-for-mac.md#设置一位的密码)
  * [生成 SSH KEY](tips-for-mac.md#生成-ssh-key)
  * [如何打开 22 端口](tips-for-mac.md#如何打开-22-端口)

## 显示/隐藏隐藏文件

* `macOS Sierra` 及以后的系统

  可以直接通过 `command + shift + .` 控制隐藏文件的显示与隐藏。

* 之前的系统
  1. 在终端中输入如下命令，将隐藏文件隐藏或显示

     ```text
      //显示隐藏文件
      defaults write com.apple.finder AppleShowAllFiles YES
      //隐藏隐藏文件
      defaults write com.apple.finder AppleShowAllFiles NO
     ```

  2. 重启Finder

     鼠标单击窗口左上角的苹果标志--&gt;强制退出--&gt;Finder--&gt;重新启动

## 设置一位的密码

1. 在终端窗口输入以下命令并回车

   ```text
    pwpolicy -clearaccountpolicies
   ```

2. 输入当前密码（不会显示输入的内容），输入完成后点击回车键

   ![&#x8F93;&#x5165;&#x5BC6;&#x7801;](http://img.zhangpeng.site/2020/10/05/1.png)

3. 如果提示 `Clearing global account policies` 则代表操作成功

   ![&#x8F93;&#x5165;&#x5BC6;&#x7801;](http://img.zhangpeng.site/2020/10/05/2.png)

4. 在系统偏好设置-用户与群组中，将密码修改为一位即可

## 生成 SSH KEY

1. 在终端窗口输入以下命令，然后一直回车即可。

   ```text
    ssh-keygen -t rsa -C "您的邮箱"
   ```

2. 查看生成的 SSH KEY

   ```text
    cat ~/.ssh/id_rsa.pub
   ```

## 如何打开 22 端口

左上角苹果图标-&gt;系统偏好设置-&gt;共享-&gt;远程登录

> Title: Mac 的日常使用
>
> Date: 2020.10.05
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)

