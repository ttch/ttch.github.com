
 ***本文仅供学习和交流使用，如果您发现我已经侵犯到原作者的版权，请邮件我ttchgm@gmail.com。以便我及时删除和处理。如果翻译有错误或者交流可以随时mail我。或者在sina微博 @天天吃好，私信与我。 本文拒绝任何形式转载。***


`Lambda`表达式，也常常叫做`闭包`，是一个在很多现代程序语言中十分流行的特性。在众多不同的原因中当中，Java平台最迫切的原因之一是`lambda`表达式能简化多线程上的`集合`的分布式处理。`列表`和`集`是有代表性，在客户端代码获取一个来自`集合`的`迭代器`，那么使用通过元素的迭代和轮流取出并处理他们。如果在并行中处理不同元素，客户端代码的有责任把它组织起来。

在`Java 8`中，目的是替代集合提供的函数，获取函数并使用他们以各种不同的方法处理元素（我们将使用非常简单的函数`forEach`为例子，通过它获取一个函数并适用于任何元素）优势是转变集合在内部迭代并组织那些元素，将来自`客户端的并行代码`转移到`库代码`中。

可是 ，为了让客户端代码在这里取得优势，需要一个简单方法给集合函数提供一个函数。当前标准的方式是建立一个`匿名类`实现对应的接口。但定义`内部匿名类`的语法太笨拙了

举个例子，在`forEach`函数集合上将获取Block接口的一个实例并调用它的apply函数为任何元素。

    interface Block<T> { void apply(T t); } 

假设我们想使用`forEach`在`List`中的`Point`元素(`Java.awt.Point`)上调换x和y的坐标。使用内部匿名类实现Block我们通过调换函数，像这样：

    pointList.forEach(new Block() { 
        public void apply(Point p) { 
            p.move(p.y, p.x);
        } 
    });

可是，使用Lambda，同样的效果可以用更简介的形式来写：

    pointList.forEach(p -> p.move(p.y, p.x)); 
