# double 转 NSString 出现精度异常

在日常开发中，后台再给我们返回数字类型的数据时，很有可能是带小数点的。我们只能用 `float` 或者 `double` 去接，我们如果需要显示给用户时，就会造成精度异常。

## 错误事例

```javascript
{
    "double": 79.04,
}
```

上面是服务端给我们返回的 `response`，我们将它转为字典.

```text
NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:data options:0 error:nil];
[NSString stringWithFormat:@"转换错误的结果为%@", dic[@"double"]];
```

![image](http://file.zhangpeng.site/2017/09/08/1.jpeg)

到这，也许有人会说：在转字符串时，加上保留的位数就可以了。但其实这样做并不是太合理。因为我们根本不服务端后台会给我们返回什么数据，所以我们不知道该保留几位小数。同理，我们也不能采取切割字符串的方式去保留小数位数。

## 解决办法

采用苹果提供的NSDecimalNumber解决此问题。

```text
double d = [dic[@"double"] doubleValue];
NSString *dStr = [NSString stringWithFormat:@"%f", d];
NSDecimalNumber *dn = [NSDecimalNumber decimalNumberWithString:dStr];
[NSString stringWithFormat:@"转换成功的结果为%@", dn.stringValue];
```

![image](http://file.zhangpeng.site/2017/09/08/1.jpeg)

本文的所有代码均以上传至 `GitHub`，如需[自取](https://github.com/2hangpeng/P_App_OC.git)~

> Title: double 转 NSString 出现精度异常
>
> Date: 2017.09.08
>
> Author: zhangpeng
>
> Github: [https://github.com/2hangpeng](https://github.com/2hangpeng)

