# 二维码生成及定制

目前比较常见的二维码库有[ZXing](https://github.com/zxing/zxing)，[ZBar](https://github.com/ZBar/ZBar)等，网上对于这些知名库的使用及分析已经很多了，在这就不做赘述了。
我们本篇文章的目标是采用 **CIQRCodeGenerator** 来完成二维码的生成及定制化。 `CIQRCodeGenerator` 在 iOS7 之后，苹果自身提供的 `API`，用于方便快捷的集成二维码的生成和读取功能。使用苹果提供的方法好处就在于不用额外引入其他的第三方库，可以减少打包后的 `App` 大小。

写博客不给[Demo](https://github.com/onntztzf/QRCodeDemo)的博主都不是好博主，没[Demo](https://github.com/onntztzf/QRCodeDemo)没 XX。授人予鱼，不如授人与渔。鱼在上面的 Demo 中，渔在下面的文章中。下面开始我的表演。&lt;(￣ ﹌ ￣)&gt;

## 需求

最近产品看支付宝红包的二维码分享功能不错，于是乎提出了需求：

* 一个用于分享的二维码，用于跳转到相关页面
* 添加 logo
* 拼接一个背景图

以上就是写出这篇文章的原因。(๑•̀ㅂ•́)و✧

## 生成二维码

我认为这个二维码的需求很多地方都会需要，所以我这边写在了一个`UIImage`的扩展中，方便以后的使用。

### 创建二维码图片

引入头文件 `CoreImage.h`

```objc
#import <CoreImage/CoreImage.h>
```

通过 `CIFilter` 创建一个二维码图片

```objc
//创建名为"CIQRCodeGenerator"的 CIFilter
CIFilter *filter = [CIFilter filterWithName:@"CIQRCodeGenerator"];
//将 filter 所有属性设置为默认值
[filter setDefaults];

//将所需尽心转为 UTF8 的数据，并设置给 filter
NSData *data = [string dataUsingEncoding:NSUTF8StringEncoding];
[filter setValue:data forKey:@"inputMessage"];

//设置二维码的纠错水平，越高纠错水平越高，可以污损的范围越大
/*
    * L: 7%
    * M: 15%
    * Q: 25%
    * H: 30%
    */
[filter setValue:@"H" forKey:@"inputCorrectionLevel"];

//拿到二维码图片，此时的图片不是很清晰，需要二次加工
CIImage *outPutImage = [filter outputImage];
```

### 调整二维码图片清晰度

方法一

```objc
/**
调整二维码清晰度

@param img 模糊的二维码图片
@param size 二维码的宽高
@return 清晰的二维码图片
*/
- (UIImage *)getHDImgWithCIImage:(CIImage *)img size:(CGSize)size {
    CGRect extent = CGRectIntegral(img.extent);
    CGFloat scale = MIN(size.width/CGRectGetWidth(extent), size.height/CGRectGetHeight(extent));

    //1.创建bitmap;
    size_t width = CGRectGetWidth(extent) * scale;
    size_t height = CGRectGetHeight(extent) * scale;
    //创建一个DeviceGray颜色空间
    CGColorSpaceRef cs = CGColorSpaceCreateDeviceGray();
    //CGBitmapContextCreate(void * _Nullable data, size_t width, size_t height, size_t bitsPerComponent, size_t bytesPerRow, CGColorSpaceRef  _Nullable space, uint32_t bitmapInfo)
    //width：图片宽度像素
    //height：图片高度像素
    //bitsPerComponent：每个颜色的比特值，例如在rgba-32模式下为8
    //bitmapInfo：指定的位图应该包含一个alpha通道。
    CGContextRef bitmapRef = CGBitmapContextCreate(nil, width, height, 8, 0, cs, (CGBitmapInfo)kCGImageAlphaNone);
    CIContext *context = [CIContext contextWithOptions:nil];
    //创建CoreGraphics image
    CGImageRef bitmapImage = [context createCGImage:img fromRect:extent];

    CGContextSetInterpolationQuality(bitmapRef, kCGInterpolationNone);
    CGContextScaleCTM(bitmapRef, scale, scale);
    CGContextDrawImage(bitmapRef, extent, bitmapImage);

    //2.保存bitmap到图片
    CGImageRef scaledImage = CGBitmapContextCreateImage(bitmapRef);
    CGContextRelease(bitmapRef); CGImageRelease(bitmapImage);

    //清晰的二维码图片
    UIImage *outputImage = [UIImage imageWithCGImage:scaledImage];
    return outputImage;
}
```

方法二

相对于方法一，这个方法可以更方便的修改二维码的颜色

```objc
/**
调整二维码清晰度

@param img 模糊的二维码图片
@param size 二维码的宽高
@return 清晰的二维码图片
*/
- (UIImage *)sencond_getHDImgWithCIImage:(CIImage *)img size:(CGSize)size {
    //二维码的颜色
    UIColor *pointColor = [UIColor blackColor];
    //背景颜色
    UIColor *backgroundColor = [UIColor whiteColor];
    CIFilter *colorFilter = [CIFilter filterWithName:@"CIFalseColor"
                                    keysAndValues:
                            @"inputImage", img,
                            @"inputColor0", [CIColor colorWithCGColor:pointColor.CGColor],
                            @"inputColor1", [CIColor colorWithCGColor:backgroundColor.CGColor],
                            nil];

    CIImage *qrImage = colorFilter.outputImage;

    //绘制
    CGImageRef cgImage = [[CIContext contextWithOptions:nil] createCGImage:qrImage fromRect:qrImage.extent];
    UIGraphicsBeginImageContext(size);
    CGContextRef context = UIGraphicsGetCurrentContext();
    CGContextSetInterpolationQuality(context, kCGInterpolationNone);
    CGContextScaleCTM(context, 1.0, -1.0);
    CGContextDrawImage(context, CGContextGetClipBoundingBox(context), cgImage);
    UIImage *codeImage = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();

    CGImageRelease(cgImage);

    return codeImage;
}
```

> 通过上面两部，就可以得到一张清晰的二维码图片了。

![图片](https://file.zhangpeng.site/2017/12/15/1.jpeg)

## 定制二维码

### 修改二维码颜色

当我美滋滋的生成一个二维码图片以后，有个 `Android` 的同事说可以把二维码周围的白边去掉，这个真的是程序员给程序员找麻烦~

修改二维码的原理是改变每个像素点的颜色，具体代码如下：

```objc
/**
 修改二维码颜色

 @param image 二维码图片
 @param red red
 @param green green
 @param blue blue
 @return 修改颜色后的二维码图片
 */
+ (UIImage *)changeColorWithQRCodeImg:(UIImage *)image red:(NSUInteger)red green:(NSUInteger)green blue:(NSUInteger)blue {
    const int imageWidth = image.size.width;
    const int imageHeight = image.size.height;
    size_t bytesPerRow = imageWidth * 4;
    uint32_t * rgbImageBuf = (uint32_t *)malloc(bytesPerRow * imageHeight);
    CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();
    CGContextRef context = CGBitmapContextCreate(rgbImageBuf, imageWidth, imageHeight, 8, bytesPerRow, colorSpace, kCGBitmapByteOrder32Little | kCGImageAlphaNoneSkipLast);

    CGContextDrawImage(context, (CGRect){(CGPointZero), (image.size)}, image.CGImage);
    //遍历像素
    int pixelNumber = imageHeight * imageWidth;
    [self changeColorOnPixel:rgbImageBuf pixelNum:pixelNumber red:red green:green blue:blue];

    CGDataProviderRef dataProvider = CGDataProviderCreateWithData(NULL, rgbImageBuf, bytesPerRow, ProviderReleaseData);

    CGImageRef imageRef = CGImageCreate(imageWidth, imageHeight, 8, 32, bytesPerRow, colorSpace, kCGImageAlphaLast | kCGBitmapByteOrder32Little, dataProvider, NULL, true, kCGRenderingIntentDefault);
    UIImage * resultImage = [UIImage imageWithCGImage: imageRef];
    CGImageRelease(imageRef);
    CGColorSpaceRelease(colorSpace);
    CGContextRelease(context);
    return resultImage;
}

/**
 遍历像素点，修改颜色

 @param rgbImageBuf rgbImageBuf
 @param pixelNum pixelNum
 @param red red
 @param green green
 @param blue blue
 */
+ (void)changeColorOnPixel: (uint32_t *)rgbImageBuf pixelNum: (int)pixelNum red: (NSUInteger)red green: (NSUInteger)green blue: (NSUInteger)blue {
    uint32_t * pCurPtr = rgbImageBuf;
    for (int i = 0; i < pixelNum; i++, pCurPtr++) {
        //通过颜色区分是不是要改变的区域
        if ((*pCurPtr & 0xffffff00) < 0xd0d0d000) {
            uint8_t * ptr = (uint8_t *)pCurPtr;
            ptr[3] = red;
            ptr[2] = green;
            ptr[1] = blue;
        } else {
            //将白色变成透明色
            uint8_t * ptr = (uint8_t *)pCurPtr;
            ptr[0] = 0;
        }
    }
}
```

![图片](https://file.zhangpeng.site/2017/12/15/2.jpeg)

### 添加水印图片（Logo）

```objc
/**
 调整二维码清晰度，添加水印图片

 @param img 模糊的二维码图片
 @param size 二维码的宽高
 @param waterImg 水印图片
 @return 添加水印图片后，清晰的二维码图片
 */
- (UIImage *)getHDImgWithCIImage:(CIImage *)img size:(CGSize)size waterImg:(UIImage *)waterImg {
    CGRect extent = CGRectIntegral(img.extent);
    CGFloat scale = MIN(size.width/CGRectGetWidth(extent), size.height/CGRectGetHeight(extent));

    //1.创建 bitmap;
    size_t width = CGRectGetWidth(extent) * scale;
    size_t height = CGRectGetHeight(extent) * scale;
    //创建一个 DeviceGray 颜色空间
    CGColorSpaceRef cs = CGColorSpaceCreateDeviceGray();
    //CGBitmapContextCreate(void * _Nullable data, size_t width, size_t height, size_t bitsPerComponent, size_t bytesPerRow, CGColorSpaceRef  _Nullable space, uint32_t bitmapInfo)
    //width：图片宽度像素
    //height：图片高度像素
    //bitsPerComponent：每个颜色的比特值，例如在 rgba-32 模式下为 8
    //bitmapInfo：指定的位图应该包含一个 alpha 通道。
    CGContextRef bitmapRef = CGBitmapContextCreate(nil, width, height, 8, 0, cs, (CGBitmapInfo)kCGImageAlphaNone);
    CIContext *context = [CIContext contextWithOptions:nil];
    //创建 CoreGraphics image
    CGImageRef bitmapImage = [context createCGImage:img fromRect:extent];
    CGContextSetInterpolationQuality(bitmapRef, kCGInterpolationNone);
    CGContextScaleCTM(bitmapRef, scale, scale);
    CGContextDrawImage(bitmapRef, extent, bitmapImage);

    //2.保存bitmap到图片
    CGImageRef scaledImage = CGBitmapContextCreateImage(bitmapRef);
    CGContextRelease(bitmapRef); CGImageRelease(bitmapImage);

    //清晰的二维码图片
    UIImage *outputImage = [UIImage imageWithCGImage:scaledImage];
    //给二维码加 logo 图
    UIGraphicsBeginImageContextWithOptions(outputImage.size, NO, [[UIScreen mainScreen] scale]);
    [outputImage drawInRect:CGRectMake(0, 0, size.width, size.height)];
    //水印图片
    //把水印图片画到生成的二维码图片上，注意尺寸不要太大（根据上面生成二维码设置的纠错程度设置），否则有可能造成扫不出来
    [waterImg drawInRect:CGRectMake((size.width-waterImg.size.width)/2.0, (size.height-waterImg.size.height)/2.0, waterImg.size.width, waterImg.size.height)];
    UIImage *newPic = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();

    return newPic;
}
```

### 拼接图片

```objc
/**
 拼接图片

 @param img1 图片 1
 @param img2 图片 2
 @param location 图片 2 相对于图片 1 的左上角位置
 @return 拼接后的图片
 */
+ (UIImage *)spliceImg1:(UIImage *)img1 img2:(UIImage *)img2 img2Location:(CGPoint)location {
//    CGSize size1 = img1.size;
    CGSize size2 = img2.size;

    UIGraphicsBeginImageContextWithOptions(img1.size, NO, [[UIScreen mainScreen] scale]);
    [img1 drawInRect:CGRectMake(0, 0, img1.size.width, img1.size.height)];

//    [img2 drawInRect:CGRectMake((size1.width-size2.width)/2.0, (size1.height-size2.height)/2.0, size2.width, size2.height)];
//    [img2 drawInRect:CGRectMake(size1.width/4.0, size1.height/2.5, size1.width/2, size1.width/2)];
    [img2 drawInRect:CGRectMake(location.x, location.y, size2.width, size2.height)];
    UIImage *newPic = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();

    return newPic;
}
```

![图片](https://file.zhangpeng.site/2017/12/15/3.jpeg)

## 附

1. [官方对于 CIQRCodeGenerator 的介绍](https://developer.apple.com/library/content/documentation/GraphicsImaging/Reference/CoreImageFilterReference/#//apple_ref/doc/filter/ci/CIQRCodeGenerator)

> Title: 二维码生成及定制
>
> Date: 2017.12.15
>
> Author: zhangpeng
>
> GitHub: [https://github.com/onntztzf](https://github.com/onntztzf)
