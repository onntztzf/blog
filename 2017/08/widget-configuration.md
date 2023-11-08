# Widget 开发 - 配置篇

## 前期准备

### 申请 `GroupID`

![image](http://file.zhangpeng.site/2017/08/29/1.jpeg)

**`Description`** 填写这个 `App Group` 的描述；
**`ID`** 填写这个 `App Group` 的标识，建议以 `com.{aaa}.{bbb}` 命名，填写完毕时，会默认在前面加上 `group`
**`{aaa}`:** 公司名字
**`{bbb}`:** App 名字

### 创建完毕以后，如图所示

![image](http://file.zhangpeng.site/2017/08/29/2.jpeg)

### 将 `group` 添加到 `App ID` 中

![image](http://file.zhangpeng.site/2017/08/29/3.jpeg)

![image](http://file.zhangpeng.site/2017/08/29/4.jpeg)

### 最后一步，重新激活下 `Provisioning Profile`

由于操作过 `App ID` 了，需要重新激活下 `Provisioning Profile`。至此，帐号相关的工作便完成了。

## 项目配置

### 点击进入 `App Target` 的 `Capabilities` 页

打开 App Groups 选项，这里会显示已有的 App Groups，勾选上面创建的 App Group 即可。

![image](http://file.zhangpeng.site/2017/08/29/5.jpeg)

### 点击进入 `Widget Target` 的 `General` 页

* 设置 `Bundle identifier`
* 命名规则：前缀要包括主项目的 `Bundle Identifier`。后缀不能是 `widget` 关键字

  例如主项目如果是 `com.aaa.bbb`，那 `Widget` 的 `Bundle identifier` 应该是 `com.aaa.bbb.today` 或者是 `com.aaa.bbb.ccc`

配置已完成，接下来请看开发篇[Widget 开发 - 开发篇](http://www.jianshu.com/p/9ddb712a45b4)

> Title: Widget 开发 - 配置篇
>
> Date: 2017.08.29
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onntztzf](https://github.com/onntztzf)
