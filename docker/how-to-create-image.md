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

口说无凭，这里我们以创建一个 vim 镜像举例，完成一次镜像的构建。

#### 创建 Dockerfile

步骤 1、创建一个文件夹 `vim` 用于存储镜像相关的文件

```powershell
➜  Desktop mkdir vim && cd vim
➜  vim 
```

步骤 2、创建一个名字为 `Dockerfile` 的文件，里面填充我们构建镜像所需的指令。

```powershell
➜  vim touch Dockerfile
```

下面是构建一个 `vim` 镜像的 `Dockerfile`，可以将它直接复制到我们创建的 `Dockerfile` 文件中。

```powershell
# 指定基础镜像
FROM ubuntu:latest
# 镜像作者及联系方式
LABEL author="zhangpeng" \
      mail="zhangpeng.0304@aliyun.com"
# 更新源
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list 
RUN sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
# 更新可用包
RUN apt update \
    && apt full-upgrade -y 
# 安装 vim
# vimrc 是目前 github 上 star数量最多的 vimrc
# 部分时候，下载过于费劲，因此提前准备好，使用时，直接复制到镜像内
RUN apt -y install vim
COPY vimrc /root/.vim_runtime/ 
RUN sh /root/.vim_runtime/install_awesome_vimrc.sh
# 清理 apt 缓存
RUN apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*
```

`Dockerfile` 支持的指令还有很多，例如：`CMD`、`ENV`、`ENTRYPOINT` 等，有兴趣可以去[官方文档](https://docs.docker.com/engine/reference/builder/)中学习。

#### 构建镜像

使用 `docker build` 命令构建镜像。

```powershell
➜  vim docker build -t vim .
[+] Building 2.5s (13/13) FINISHED
 => [internal] load build definition from Dockerfile                     0.0s
 => => transferring dockerfile: 37B                                      0.0s
 => [internal] load .dockerignore                                        0.0s
 => => transferring context: 2B                                          0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest         0.0s
 => [internal] load build context                                        0.2s
 => => transferring context: 168.85kB                                    0.2s
 => [1/8] FROM docker.io/library/ubuntu:latest                           0.0s
 => CACHED [2/8] RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g  0.0s
 => CACHED [3/8] RUN sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/  0.0s
 => CACHED [4/8] RUN apt update     && apt full-upgrade -y               0.0s
 => CACHED [5/8] RUN apt -y install vim                                  0.0s
 => [6/8] COPY vimrc /root/.vim_runtime/                                 0.3s
 => [7/8] RUN sh /root/.vim_runtime/install_awesome_vimrc.sh             0.3s
 => [8/8] RUN apt autoremove -y     && apt clean -y     && rm -rf /var/  1.3s
 => exporting to image                                                   0.3s
 => => exporting layers                                                  0.3s
 => => writing image sha256:67474823a3828a6ecefa0ba6b61909e81f8d2a7de0c  0.0s
 => => naming to docker.io/library/vim                                   0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```

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

## 参考文献

1. [Create a base image](https://docs.docker.com/develop/develop-images/baseimages/)
2. [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
3. [docker save与docker export的区别](https://jingsam.github.io/2017/08/26/docker-save-and-docker-export.html)
4. [Difference Between Docker Save and Export](https://www.baeldung.com/ops/docker-save-export)

## 

如果觉得本篇文章不错，麻烦给个**点赞👍、收藏🌟、分享👊、在看👀**四连！

![干货输出机](https://img.zhangpeng.site/wechat/qrcode.jpg)
