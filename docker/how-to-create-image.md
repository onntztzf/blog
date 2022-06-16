# 如何构建一个镜像

## 镜像是什么

要构建一个镜像，首先要清楚镜像是什么。[docker 文档](https://docs.docker.com/get-started/overview/) 对镜像的解释如下：

> An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization. For example, you may build an image which is based on the ubuntu image, but installs the Apache web server and your application, as well as the configuration details needed to make your application run.

简单来讲就是：镜像就是一个带有创建 `Docker` 容器指令的**只读模板**。镜像中可以包含着系统、应用及应用配置等。

## 如何构建镜像

构建镜像的方法有：

1. 使用 `Dockerfile` 构建镜像（推荐）
2. 基于已有镜像构建镜像
3. 基于已有容器构建镜像

### 使用 `Dockerfile` 构建镜像（推荐）

`Dockerfile` 是一个普通的文本文件，其中包含构建镜像所需的一组[指令](https://docs.docker.com/engine/reference/builder/)。当我们编写完成后，使用 [docker build](https://docs.docker.com/engine/reference/commandline/build/) 命令来构建镜像，这个命令会读取 `Dockerfile` 中的指令来自动构建镜像。

下文，我们会提供一个 `Dockerfile` 的[例子](#构建一个-vim-镜像的-dockerfile)

### 基于已有镜像构建镜像

首先，我们需要弄清楚已有镜像是什么镜像？镜像大概可以分为两种：

- 带有文件系统的镜像
  
  带有文件系统的镜像是指通过 [docker export](https://docs.docker.com/engine/reference/commandline/export/) 导出的容器镜像。如果想使用这类镜像构建镜像，需要使用 [docker import](https://docs.docker.com/engine/reference/commandline/import/) 命令。

- 普通镜像
  
  普通镜像是指通过 [docker save](https://docs.docker.com/engine/reference/commandline/save/) 打包的镜像。如果想使用这类镜像构建镜像，需要使用 [docker load](https://docs.docker.com/engine/reference/commandline/load/) 命令。

### 基于已有容器构建镜像

基于已有容器构建镜像主要用于跟进一些异常情况，如：`cpu`或内存异常突增、异常 `bug` 现场等。这时我们就可以通过保存容器的即时镜像，方便复现问题。

这里用到的是 [docker commit](https://docs.docker.com/engine/reference/commandline/commit/) 命令。伪代码如下：

```powershell
$ docker commit \
    --author "Zhang Peng <zhangpeng.0304@aliyun.com>" \
    --message "保存容器镜像" \
    image:case1
```

然后就可以通过 [docker run](https://docs.docker.com/engine/reference/commandline/run/) 将这个镜像运行起来了。

## 构建一个 vim 镜像的 Dockerfile

```powershell
# 指定基础镜像
FROM ubuntu:latest
LABEL author="zhangpeng" \
      mail="zhangpeng.0304@aliyun.com"
# 更新源
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list 
RUN sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# sudo
RUN apt update \
    && apt full-upgrade -y \
    && apt install -y sudo 

# 创建 ubuntu 用户
RUN useradd -m ubuntu -s /bin/bash && adduser ubuntu sudo \
    && echo "ubuntu ALL=(ALL) NOPASSWD : ALL" | tee /etc/sudoers.d/nopasswd4sudo

USER ubuntu
WORKDIR /home/ubuntu

# zsh
COPY oh-my-zsh .oh-my-zsh
RUN sudo apt -y install zsh git \
    && sudo cp .oh-my-zsh/templates/zshrc.zsh-template .zshrc \
    && sudo git clone https://github.com/zsh-users/zsh-autosuggestions.git .oh-my-zsh/plugins/zsh-autosuggestions \
    && sudo git clone https://github.com/zsh-users/zsh-syntax-highlighting.git .oh-my-zsh/plugins/zsh-syntax-highlighting \
    && sudo sed -i "s/^plugins=(.*)$/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/g" .zshrc \
    && sudo usermod -s /bin/zsh ubuntu

# vim
RUN sudo apt -y install vim && sudo apt -y install nodejs && sudo apt -y install fzf
COPY vimrc my_configs.vim .vim_runtime/ 
COPY my_plugins .vim_runtime/my_plugins
RUN sh .vim_runtime/install_awesome_vimrc.sh

RUN sudo apt autoremove -y \
    && sudo apt clean -y \
    && sudo rm -rf /var/lib/apt/lists/*
```

## 参考文献

1. [Create a base image](https://docs.docker.com/develop/develop-images/baseimages/)
2. [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
3. [docker save与docker export的区别](https://jingsam.github.io/2017/08/26/docker-save-and-docker-export.html)
4. [Difference Between Docker Save and Export](https://www.baeldung.com/ops/docker-save-export)

## 

如果觉得本篇文章不错，麻烦给个**点赞👍、收藏🌟、分享👊、在看👀**四连！

![干货输出机](https://img.zhangpeng.site/wechat/qrcode.jpg)
