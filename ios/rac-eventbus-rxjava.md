# Rac EventBus RxJava

## Rac 是什么

`Rac` 全称 `Reactivecocoa`，是一个应用于 `iOS` 和 `OS X` 开发的框架，它的灵感来自[函数式](https://baike.baidu.com/item/%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B) [响应式](https://baike.baidu.com/item/%E5%93%8D%E5%BA%94%E5%BC%8F%E7%BC%96%E7%A8%8B)编程。

## Rac 做了什么

将原有的各种设计模式，包括 中心以及观察者模式各种『输入』，都抽象成了信号，通过信号的传递来处理这些行为。简化了事件的传递，每个部分只需要关注信号的传递及状态即可。最终将信号通过不同的组合，达成我们最终的目的。

## Rac 的组成

### 1. 核心组件

* 信号源

  `RACStream` 及其子类；

* 订阅者

  `RACSubscriber`及其子类

* 调度器

  `RACScheduler`及其子类

* 清洁工

  `RACDisposable`及其子类

### 2. 组件间的关系

1. 订阅者订阅信号源后，调度器保证信号源的传递及顺序
2. 信号到达后，根据信号的状态，进行不同的操作
3. 操作完成后，通过清洁工清理掉信号源

## Rac 的用处

* 处理异步或者事件驱动数据源
* 连接依赖的操作
* 并行地独立地工作
* 简化集合转换

## Rac 的使用

[Rac 的简单使用](https://github.com/gh-zhangpeng/RacDemo)

## 对比 EventBus RxJava

### EventBus

EventBus是一款针对Android设计的发布/订阅事件总线，使用订阅/发布模式让组件间的通信变得简单。主要功能是替代Intent，Handler，BroadCast在Fragment，Activity，Service，线程之间的消息传递。

* `EventBus` 四大组成部分： 1. Publisher发布者 用于分发我们的Event事件，在EventBus中通过post方法进行分发传送。 2. Subscriber订阅者 用于接受我们的事件，我们在订阅事件中处理我们接收的数据。 3. Event事件 任何一个对象都可以作为事件，比如任何字符串，事件是发布者和订阅者之间的通信载体。 4. EventBus 类似于中转站，将我们的事件进行对应的分发处理。
* 优点 1. 简化了组件之间的通信
  * 将事件发送者和接收者分离
  * 在`Activities`，`Fragments`和`background threads`中表现良好
  * 避免复杂且容易出错的依赖关系和生命周期问题
    1. 使代码更简单
    2. 性能开销小
    3. 代码量小（约50k左右）
* 缺点 消息乱飞？不方便 Debug？
* 使用 1. 定义一个事件

  ```java
        public static class MessageEvent
        {
            /* Additional fields if needed */
        }
  ```

  1. 声明一个用于响应的方法，并且在适当的生命周期注册或注销

     ```java
        @Subscribe(threadMode = ThreadMode.MAIN)  
        public void onMessageEvent(MessageEvent event)
        {
            /* Do something */
        }
        @Override
        public void onStart() {
            super.onStart();
            <!-- 
                官方写法，但是如果不进行处理，可能会造成重复注册订阅，多次响应事件
                EventBus.getDefault().register(this); 
            -->
            // 通过 isRegistered 检查是否已经注册订阅
            if (!EventBus.getDefault().isRegistered(this)) {
                EventBus.getDefault().register(this);
            }
        }

        @Override
        public void onStop() {
            super.onStop();
            EventBus.getDefault().unregister(this);
        }
     ```

     根据不同的应用场景，可以选择在不同的声明周期注册或移除订阅

     ```java
        @Override
        protected void onCreate(Bundle savedInstanceState)
        {
            super.onCreate(savedInstanceState);
        }
        @Override
        protected void onDestroy()
        {
            super.onDestroy();
        }

        @Override
        protected void onResume()
        {
            super.onResume();
        }
        @Override
        protected void onPause()
        {
            super.onPause();
        }
     ```

  2. 发布事件，事件发布后，订阅者中的响应方法就会受到事件

     ```java
        EventBus.getDefault().post(new MessageEvent());
     ```

### RxJava

`RxJava` 在 `GitHub` 主页上的自我介绍是"a library for composing asynchronous and event-based programs using observable sequences for the Java VM"（一个在 `Java VM` 上使用可观测的序列来组成异步的、基于事件的程序的库），核心可以总结为两个字：**异步**。说到根上，它就是一个实现异步操作的库。而它的异步实现，是通过一种扩展的观察者模式来实现的。

* `RxJava` 的四个基本概念 1. `Observable` \(可观察者，即被观察者\) 决定什么时候触发事件以及触发怎样的事件。 2. `Observer` \(观察者\) 决定事件触发的时候将有怎样的行为。 3. `subscribe` \(订阅\) 创建了 `Observable` 和 `Observer` 之后，再用 subscribe\(\) 方法将它们联结起来，整条链子就可以工作了 4. 事件
* 使用

  ```java
    Observable.from(folders)
        <!-- 降维，事件转换？ -->
        .flatMap(new Func1<File, Observable<File>>() {
            @Override
            public Observable<File> call(File file) {
                return Observable.from(file.listFiles());
            }
        })
        <!-- 事件过滤 -->
        .filter(new Func1<File, Boolean>() {
            @Override
            public Boolean call(File file) {
                return file.getName().endsWith(".png");
            }
        })
        <!-- 类型转换？ -->
        .map(new Func1<File, Bitmap>() {
            @Override
            public Bitmap call(File file) {
                return getBitmapFromFile(file);
            }
        })
        <!-- 指定Observable自身在哪个调度器上执行 -->
        .subscribeOn(Schedulers.io())
        <!-- 指定一个观察者在哪个调度器上观察这个Observable -->
        .observeOn(AndroidSchedulers.mainThread())
        <!-- 事件响应？ -->
        .subscribe(new Action1<Bitmap>() {
            @Override
            public void call(Bitmap bitmap) {
                imageCollectorView.addImage(bitmap);
            }
        });
  ```

## 附

1. [Reactivecocoa](https://github.com/ReactiveCocoa/ReactiveObjC)
2. [ReactiveCocoa 常用API整理](https://juejin.im/post/578f49fa5bbb50005b95fb80)
3. [EventBus](https://github.com/greenrobot/EventBus)
4. [EventBus 中文文档](https://juejin.im/entry/5a91a02d6fb9a06340522ac0)
5. [给 Android 开发者的 RxJava 详解](https://gank.io/post/560e15be2dca930e00da1083)
6. RxJava的使用

   [RxJava的使用（一）基本用法](https://www.jianshu.com/p/19cac3c5b106)

   [RxJava的使用（二）Action](https://www.jianshu.com/p/c7a995f3763c)

   [RxJava的使用（三）转换——map、flatMap](https://www.jianshu.com/p/52cd2d514528)

> Title: 聊一聊 Rac
>
> Date: 2018.12.08
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)

