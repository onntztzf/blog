---
title: 你好，jwt
author: zhangpeng
date: 2022-10-09
---

# 你好，jwt

![](https://img.zhangpeng.site/2022/10/09/1.jpg)

## jwt 是什么

`jwt` 的完整拼写是 `JSON Web Token`。见名知意，`jwt` 就是一种用于在各方之间安全地传输信息的令牌，令牌中的信息是以 `JSON` 对象的形式进行存储。

`jwt` 也是一种[开放标准](https://www.rfc-editor.org/rfc/rfc7519)。它定义了一种紧凑且安全的方法，用于在各方之间传递信息。在 `jwt` 中，信息会被编码为 `JSON` 对象，然后把这个 `JSON` 对象作为一个 `JSON Web Signature(JWS)` 结构的有效载荷或作为一个 `JSON Web Encryption(JWE)` 结构的明文，使信息能够被签名或者通过消息验证码(`MAC`)进行进行完整性和真实性校验。

## jwt 的构成

`jwt` 由三部分构成，分别是：头部（`header`）、有效载荷（`payload`）和签名（`signature`）。在生成 `jwt` 时，会对这三个部分分别进行 `Base64URL` 编码，然后将得到的三个字符串使用 `.` 按顺序进行连接，最后得到一个完整的 `jwt`。如下：

```text
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJqd3QiLCJzdWIiOiIxIiwiYXVkIjoiYXBwMSIsImlhdCI6MTY2NTMwNzgwMCwibmJmIjoxNjY1Mzk0MjAwLCJleHAiOjE2NjU5MTI2MDAsImp0aSI6MSwibmFtZSI6InpoYW5ncGVuZyJ9.8QhYZSONATlpO-oZtUoQOlyzjGSpeNvizPofT5ep0WQ
```

接下来，依次介绍每一部分的构成。

### 头部（`header`）

`header` 是一个描述 `jwt` 元数据的 `JSON` 对象。通常由两个字段构成：

字段 | 含义 | 描述
--- | --- | ---
typ | `type` | 表示令牌的类型，统一写为 `JWT`
alg | `algorithm` | 表示签名使用的算法，如：`HMAC SHA256`

举个例子：

```JSON
{
    "typ": "JWT",
    "alg": "HS256"
}
```

将上面的 `header` 进行 `Base64URL` 编码，就可以得到 `jwt` 的第一部分：

`eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9`

### 有效载荷（`payload`）

`payload` 是 `jwt` 的第二部分，也是一个 `JSON` 对象，其中包含需要传递的数据。[RFC7519](https://www.rfc-editor.org/rfc/rfc7519#section-4.1)中定义了一组非强制性的但建议使用的预定义字段，我们可以选择使用：

字段 | 含义 | 描述
--- | --- | ---
iss | `issuer` | 签发人，可以用于确定签发 `jwt` 的人
sub | `subject` | 签发的主题，可以用于表示被签发的人是谁或者被签发的内容是什么
aud | `audience` | `jwt` 的受众者，可以用于表示该 `jwt` 该被哪些主体使用
iat | `issued at` | `jwt` 的签发时间
nbf | `not before` | `jwt` 的启用时间，在该时间前，此 `jwt` 是无效的
exp | `expiration time` | `jwt` 的过期时间，在该时间后，此 `jwt` 是无效的
jti | `JWT ID` | `jwt` 的唯一标识

除了上面列出的预定义字段，我们还可以添加一些自定义字段。如：`name`

举个例子：

```JSON
{
    "iss": "jwt",
    "sub": "1",
    "aud": "app1",
    "iat": 1665307800,
    "nbf": 1665394200,
    "exp": 1665912600,
    "jti": 1,
    "name": "zhangpeng"
}
```

将上面的 `payload` 进行 `Base64URL` 编码，就可以得到 `jwt` 的第二部分：

`eyJpc3MiOiJqd3QiLCJzdWIiOiIxIiwiYXVkIjoiYXBwMSIsImlhdCI6MTY2NTMwNzgwMCwibmJmIjoxNjY1Mzk0MjAwLCJleHAiOjE2NjU5MTI2MDAsImp0aSI6MSwibmFtZSI6InpoYW5ncGVuZyJ9`

**注意：** 默认情况下 `jwt` 是未加密的，只是进行了 `Base64URL` 编码，所以任何人拿到 `jwt` 后都可以转换回原本的 `JSON` 数据。因此**不要添加隐私信息**，比如用户的密码等。

### 签名（`signature`）

`signature` 是 `jwt` 的最后一部分，通过它能够验证 `jwt` 是否有效和是否被篡改。将 `header` 和 `payload` 分别进行 `Base64URL` 编码，然后将它们用 `.` 连接起来，然后使用 `header` 中的签名算法（如：`HMACSHA256`）进行加密，便可以得到 `signature`。

举个例子：

```text
HMACSHA256(
  Base64URLEncode(header) + "." +
  Base64URLEncode(payload),
  secret
)
```

使用前文中的 `header` 和 `payload`，通过上面的公式，可以计算出签名为：

`8QhYZSONATlpO-oZtUoQOlyzjGSpeNvizPofT5ep0WQ-hoICKvR06A`

**注意：** `jwt` 的签发生成最好是在服务器端完成，这样可以有效地保护 `secret` 不被泄漏。因为 `secret` 是用来进行 `jwt` 的签发和验证的，一旦 `secret` 被泄漏，那就意味着任何人都可以自我签发 `jwt` 了。

将上面的到的三部分，使用 `.` 进行连接，便得到了我们最终的 `jwt`：

```text
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJqd3QiLCJzdWIiOiIxIiwiYXVkIjoiYXBwMSIsImlhdCI6MTY2NTMwNzgwMCwibmJmIjoxNjY1Mzk0MjAwLCJleHAiOjE2NjU5MTI2MDAsImp0aSI6MSwibmFtZSI6InpoYW5ncGVuZyJ9.8QhYZSONATlpO-oZtUoQOlyzjGSpeNvizPofT5ep0WQ
```

## jwt 的优缺点

### 优点

1. 因为 `json` 对象的通用性，所以 `jwt` 是可以进行跨语言支持的
2. 因为有 `payload` 部分，所以 `jwt` 可以在存储一些其他业务逻辑需要的信息
3. 因为是构成简单，所以便于传输

### 缺点

1. 服务端不保存，所以签发后，如果需要让某个 `jwt` 失效，需要补充其他逻辑
2. `payload` 部分可解码，所以如果想更安全，在得到 `jwt` 后，需要进行二次加密

## jwt 常见的使用场景

### 授权

**一般被用来在身份提供者和服务提供者间传递被认证的身份信息。** 如：

用户登录后，每个后续请求都将包含 `jwt`，允许用户访问该令牌允许的路由、服务和资源。单点登录是当今广泛使用 `jwt` 的功能，因为它的开销很小，并且能够在不同领域轻松使用。

### 信息交换

**`jwt` 是在各方之间安全传输信息的好方法。** 如：

使用公钥/私钥对，您可以确定发件人就是他们说的那个人。此外，由于签名是使用标头和有效载荷计算的，您还可以验证内容是否未被篡改。

## 总结

其实 `jwt` 也没那么神秘，对吧？**`jwt`就是一个承载了 `JSON` 信息的一个字符串。**

**为了保持紧凑，`JSON` 信息并不是直接存储的，是通过 `Base64URL` 编码后存储的。**

**为了保证安全，又通过算法，对信息做了签名和加密，保证信息不回在传输过程中被篡改。**

希望在阅读本篇文章后，可以让您对 `jwt` 豁然开朗！

## 参考文献

1. [jwt.io](https://jwt.io)
2. [JSON Web Token RFC7519](https://www.rfc-editor.org/rfc/rfc7519)
3. [JSON Web Signature RFC7515](https://www.rfc-editor.org/rfc/rfc7515)
4. [JSON Web Encryption RFC7516](https://www.rfc-editor.org/rfc/rfc7516)
5. [Payload 载荷](https://en.wikipedia.org/wiki/Payload_(computing))

---

如果觉得本篇文章不错，麻烦给个**点赞👍、收藏🌟、分享👊、在看👀**四连！

![干货输出机](https://img.zhangpeng.site/wechat/qrcode.jpg)
