# 快速生成表结构的结构体

## 前言

通过下图 [The TIOBE Programming Community](https://www.tiobe.com/tiobe-index/) 的统计可以看到 `Go` 的发展如火如荼，于是我也迈进了 `gophers` 大军之中。

![图片](https://file.zhangpeng.site/2022/02/18/1.jpeg)

在 [GitHub](https://github.com/search?l=Go&o=desc&q=orm&s=stars&type=Repositories) 搜索 `Go` 语言的 `orm` 框架。可以看到 `gorm` 的 `star` 远超其他同类框架。因此我们跟随大流，选用 [gorm](https://gorm.io/zh_CN/) 框架。

![图片](https://file.zhangpeng.site/2022/02/18/2.jpeg)

## 依赖安装

### 依赖

这边使用的是 [gen](https://github.com/go-gorm/gen) 完成表结构体的生成。

`gen` 是字节无恒实验室之前发布的一个 `gorm` 相关的开源工具。其主要功能有：

- ⚡️ 自动同步库表，省去繁琐复制
- 🔗 代码一键生成，专注业务逻辑
- 🐞 字段类型安全，执行 SQL 也安全
- 😉 查询优雅返回，完美兼容 GORM

其他相关资料可以从 [无恒实验室联合 GORM 推出安全好用的 ORM 框架-GEN](https://mp.weixin.qq.com/s/SfLIkU8E2b3sAO1qSUkyXA) 或者 [README](https://github.com/go-gorm/gen/blob/master/README.ZH_CN.md) 了解。

### 安装

在终端进入项目根目录，使用下面命令安装 `gen`：

```shell
go get -u gorm.io/gen
```

## 表结构体生成

### 编写生成工具

在项目中找个合适的位置，创建一个文件 `tools.go`，然后将下面代码填入文件内。

```golang
import (
    "gorm.io/gen"
    "gorm.io/gorm"
    "strings"
)

func GenerateTableStruct(db *gorm.DB) {
    //根据配置实例化 gen
    g := gen.NewGenerator(gen.Config{
        //文件生成路径
        ModelPkgPath: "./dal/model",
        //是否需要索引
        FieldWithIndexTag: true,
        //是否需要类型
        FieldWithTypeTag: true,
        //还有一些配置，不过我觉得暂时不需要。如果有兴趣，可以直接点进 config 查看...
    })
    //使用数据库的实例
    g.UseDB(db)
    //模型结构体的命名规则
    g.WithModelNameStrategy(func(tableName string) (modelName string) {
        if strings.HasPrefix(tableName, "tbl") {
            return firstUpper(tableName[3:])
        }
        if strings.HasPrefix(tableName, "table") {
            return firstUpper(tableName[5:])
        }
        return firstUpper(tableName)
    })
    //模型文件的命名规则
    g.WithFileNameStrategy(func(tableName string) (fileName string) {
        if strings.HasPrefix(tableName, "tbl") {
            return firstLower(tableName[3:])
        }
        if strings.HasPrefix(tableName, "table") {
            return firstLower(tableName[5:])
        }
        return tableName
    })
    //数据类型映射
    dataMap := map[string]func(detailType string) (dataType string){
        "int": func(detailType string) (dataType string) {
            //if strings.Contains(detailType, "unsigned") {
            //    return "uint64"
            //}
            return "int64"
        },
        "bigint": func(detailType string) (dataType string) {
            //if strings.Contains(detailType, "unsigned") {
            //    return "uint64"
            //}
            return "int64"
        },
    }
    //使用上面的类型映射
    g.WithDataTypeMap(dataMap)
    //生成数据库内所有表的结构体
    g.GenerateAllTable()
    //生成某张表的结构体
    //g.GenerateModelAs("tblUser", "User")
    //执行
    g.Execute()
}

//字符串第一位改成小写
func firstLower(s string) string {
    if s == "" {
        return ""
    }
    return strings.ToLower(s[:1]) + s[1:]
}

//字符串第一位改成大写
func firstUpper(s string) string {
    if s == "" {
        return ""
    }
    return strings.ToUpper(s[:1]) + s[1:]
}
```

上面代码中只是我这边的配置，`gen` 的配置还有很多，有兴趣的话，可以看[官方文档](https://github.com/go-gorm/gen/blob/master/README.ZH_CN.md)或者直接点进代码去看。

### 使用工具生成结构体

工具的使用有很多种方式，选择一个适合你项目的方式就好，比如：

- 写个接口，使用接口触发结构体的生成
- 使用 [cobra](https://github.com/spf13/cobra)，生成个命令行工具，使用命令触发结构体的生成

######

如果觉得本篇文章不错，麻烦给个**点赞👍、收藏🌟、分享👊、在看👀**四连！

![干货输出机](https://file.zhangpeng.site/wechat/qrcode.jpg)
