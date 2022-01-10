### Tornado基本介绍
```html
Tornado是一个基于Python的Web服务框架和异步网络库，Tornado利用非阻塞网络I/O，可以承载成千上万的活动链接，完美的实现长连接、WebSocket、其他对于每一个用户来说需要长连接的程序。
```

### Tornado主要组件
```html
Web框架包括用来创建Web应用程序的「RequestHandler」类，还有很多其他支持的类。
```
```html
HTTP客户端和服务端的实现类「HTTPServer」和「AsyncHTTPClient」。
```
```html
异步网络库「IOLoop」和「IOStream」，对HTTP的实现提供构建模块，还可以用来实现其他协议。
```
```
协程库「tornado.gen」让用户通过更直接的方式实现异步编程，而不是通过回调的方式。
```

### Tornado功能特点
```html
Tornado Web框架和HTTP服务器提供了一整套WSGI方案。可以让Tornado编写的Web框架运行在一个WSGI容器中「WSGIAdapter」，或者使用Tornado HTTP服务器作为一个WSGI容器「WSGIContainer」，这两种解决方案都有各自的局限性，为了充分利用Tornado的特性，你需要同时使用Tornado的Web框架和HTTP服务器。
```

### Tornado异步非阻塞IO
```html
实时的Web特性通常需要为每个用户提供一份大部分时间都处于空闲的长链接。在传统的同步Web服务器中，这意味着需要给每个用户分配一个专用的线程，这样导致开销巨大，为了减少对于并发连接需要的开销，Tornado使用了一种单线程时间循环的方式，这意味着所有应用程序代码都应该是异步和非阻塞的，因为同一时刻只有一个操作是有效的
```
```html
一个函数通常在他等待返回值的时候被阻塞，一个函数被阻塞可能由于很多原因：网络IO，磁盘IO，互斥锁等，事实上每个函数都会被阻塞，只是时间会比较短而已，当一个函数运行时并且占用CPU。

一个函数可以在某些方面阻塞而在其他方面不阻塞，比如：「tornado.httpclient」在默认设置下将阻塞在DNS解析，但是其他的网络请求时不会阻塞(为了减轻这种影响，可以用「ThreadResolve」或正确配置「liburl」使用「tornado.curl_httpclient」)。在Tornado上下文中我们通常讨论的是网络IO上下文阻塞，虽然各种阻塞已经被最小化。
```

```html
异步：一个异步函数是在全部结束前部分结果返回，而且通常会在程序中触发一些动作然后在后台执行一些任务，和正常的同步函数相比，同步函数在返回之前做完了所有的任务。这里有几种类型的异步接口：
```
```html
1.回调函数
2.返回一个占位符(Future,Promise,Deffered)
3.传送一个队列
4.回调注册(比如：POSIX信号)
```