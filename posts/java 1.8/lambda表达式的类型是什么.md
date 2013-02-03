 ***本文仅供学习和交流使用，如果您发现我已经侵犯到原作者的版权，请邮件我ttchgm@gmail.com。以便我及时删除和处理。如果翻译有错误或者交流可以随时mail我。或者在sina微博 @天天吃好，私信与我。 本文拒绝任何形式转载。***

#lambda表达式的类型是什么？

一个lambda表达式是一个功能性接口的实例。但是一个lambda表达式自身并不包含关于哪一个功能性接口是他的实现的信息；这些信息的推断来自上下文的使用处，举个例子，表达式

    :::java
	x -> 2 * x

可以是如下功能性接口的实例
	
	:::java
    interface IntOperation { int operate(int i); }

这样写也合法

    :::java
	IntOperation io = x -> x * 2;

IntOperation右边的赋值预料到类型为表达式。调用的目标类型为lambda表达式。一个清晰的lambda表达式可能是不同的功能性接口的兼容类型，所以他遵照同样的lambda表达式拥有不同的目标类型在不同的上下文中，举个例子，指定一个接口

    :::java
	interface DoubleOperation { double operate(double i); }

这样写也合法

    
	:::java
	DoubleOperation fo = x -> x * 2;

lambda表达式的目标类型必须是一个功能性接口，并且能被目标类型兼容，lambda表达式必须和接口的函数描述一样的参数类型，他的返回类型也必须和函数描述兼容，并且他能抛出的异常也仅限于在函数描述范围中