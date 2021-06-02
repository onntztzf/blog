# App 沙盒

**从 `iOS8` 以后，每次App重新运行后，沙盒路径都会变化。**

## Documents 目录

保存应用运行时生成的需要持久化的数据，`iTunes` 会自动备份该目录。苹果建议将程序中建立的或在程序中浏览到的文件数据保存在该目录下，`iTunes` 备份和恢复的时候会包括此目录。

```objc
NSString *path = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) firstObject];
```

## Library 目录

存储程序的默认设置和其他状态信息，`iTunes` 会自动备份该目录（仅`Preferences`）。

```objc
NSString *path = [NSSearchPathForDirectoriesInDomains(NSLibraryDirectory, NSUserDomainMask, YES) firstObject];
```

这个目录下有两个子目录：`Caches` 和 `Preferences`

### Preferences

保存应用的所有偏好设置，`iOS` 的 `Settings`（设置）应用会在该目录中查找应用的设置信息，`iTunes` 会自动备份该目录。

### Caches

存放缓存文件，`iTunes` 不会备份此目录，此目录下文件不会在应用退出删除。一般存放体积比较大，不是特别重要的资源。

```objc
NSString *path = [NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES) firstObject];
```

## Tmp 目录

保存应用运行时所需的临时数据，使用完毕后再将相应的文件从该目录删除。应用没有运行时，系统也有可能会清除该目录下的文件，`iTunes` 不会同步该目录。设备重启时，该目录下的文件会丢失。

```objc
NSString *path = NSTemporaryDirectory();
```

---

> Title: App 沙盒
>
> Date: 2019.04.15
>
> Author: zhangpeng
>
> Github: <https://github.com/gh-zhangpeng>
