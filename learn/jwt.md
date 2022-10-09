---
title: 聊聊 jwt
category: learn
---

# 聊聊 jwt

## jwt 是什么

`jwt` 是三个单词的缩写，完整的拼写是 `JSON Web Token`。见名知意，`jwt` 就是一种用于在各方之间安全地传输信息的令牌，令牌中的信息是以 `JSON` 对象的形式进行存储。

`jwt` 也是一种[开放标准](https://www.rfc-editor.org/rfc/rfc7519)。它定义了一种紧凑且安全的方法，用于在各方之间传递信息。在 `jwt` 中，信息会被编码为 `JSON` 对象，然后把这个 `JSON` 对象作为一个 `JSON Web Signature(JWS)` 结构的有效载荷或作为一个 `JSON Web Encryption(JWE)` 结构的明文，使信息能够被签名或者通过消息验证码(`MAC`)进行进行完整性和真实性校验。

## jwt 的构成

`jwt` 由三部分构成，分别是：头部（`header`）、有效载荷（`payload`）和签名（`signature`）。在生成 `jwt` 时，会对这三个部分分别进行 `base64Url` 编码，然后将得到的三个字符串使用 `.` 按顺序进行连接，最后得到一个完整的 `jwt`。如下：

```text
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ6aGFuZ3BlbmciLCJzdWIiOiJqd3QiLCJhdWQiOiJ5b3UiLCJpYXQiOjE2NjUzMDc4MDAsIm5iZiI6MTY2NTM5NDIwMCwiZXhwIjoxNjY1OTEyNjAwLCJqdGkiOjF9.4S5frHTkppvjMfaBtkdEUCUBp2lH553Ps3BJZNgrZmk
```

接下来，依次介绍每一部分的构成。

### 头部（`header`）

`header` 是一个描述 `jwt` 元数据的 `JSON` 对象。通常由两个元素构成：

- `typ`
  
  `type`，表示令牌的类型，统一写为 `JWT`

- `alg`

  `algorithm`，表示签名使用的算法，如：`HMAC SHA256`

举个例子：

```JSON
{
    "typ": "JWT",
    "alg": "HS256"
}
```

将上面的 `header` 进行 `base64Url` 编码，就可以得到 `jwt` 的第一部分：

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9

### 有效载荷（`payload`）

`payload` 是 `jwt` 的第二部分，也是一个 `JSON` 对象，其中包含需要传递的数据。[RFC7519](https://www.rfc-editor.org/rfc/rfc7519#section-4.1)中定义了几个标准字段，我们可以选择使用：

- `iss`
  
  `issuer`

- sub：主题
- aud：用户
- iat：发布时间
- nbf：在此之前不可用
- exp：到期时间
- jti：JWT ID用于标识该JWT

举个例子：

```JSON
{
    "iss": "zhangpeng",
    "sub": "jwt",
    "aud": "you",
    "iat": 1665307800,
    "nbf": 1665394200,
    "exp": 1665912600,
    "jti": 1
}
```

### 签名（`signature`）

## jwt 常见的使用场景

### 授权

### jwt 与 session 的区别

### 信息交换

**一般被用来在身份提供者和服务提供者间传递被认证的身份信息**，以便于后续操作，也可以增加一些其它业务逻辑所必须的声明信息。

## jwt 的使用方式

## 参考文献

1. [jwt.io](https://jwt.io)
2. JSON Web Token
   - [维基百科](https://en.wikipedia.org/wiki/JSON_Web_Token)
   - [RFC7519](https://www.rfc-editor.org/rfc/rfc7519)
3. JSON Web Signature
   - [维基百科](https://en.wikipedia.org/wiki/JSON_Web_Signature)
   - [RFC7515](https://www.rfc-editor.org/rfc/rfc7515)
4. JSON Web Encryption
   - [维基百科](https://en.wikipedia.org/wiki/JSON_Web_Encryption)
   - [RFC7516](https://www.rfc-editor.org/rfc/rfc7516)
5. [Payload 载荷](https://en.wikipedia.org/wiki/Payload_(computing))

## 

如果觉得本篇文章不错，麻烦给个**点赞👍、收藏🌟、分享👊、在看👀**四连！

![干货输出机](https://img.zhangpeng.site/wechat/qrcode.jpg)
