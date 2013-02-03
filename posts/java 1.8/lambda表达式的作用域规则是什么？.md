
----------
 
***本文仅供学习和交流使用，如果您发现我已经侵犯到原作者的版权，请邮件我ttchgm@gmail.com。以便我及时删除和处理。如果翻译有错误或者交流可以随时mail我。或者在sina微博 @天天吃好，私信与我。 本文拒绝任何形式转载。***

----------

#What are the scoping rules for lambda expressions?

#lambda表达式的作用域规则是什么？

Lambda expressions do not introduce any new naming environment. Names in the body of a lambda are interpreted exactly as in the enclosing environment, except for the addition of new names for the lambda expression’s formal parameters. The keywords this and super also have the same meaning as immediately outside the lambda expression—that is, they refer to the enclosing class. Formal parameters follow the same rules as method parameters for shadowing class and instance variables. For example, the declaration of Bar:

lambda表达式并不引入任何新命名环境。名字在一个lambda块内可以被理解为像在封闭的环境中，除了增加新的名字在lambda表达式的正式参数里。关键字`this`和`super`也有同样的意思像lambda表达式外边，他们参考自封闭类。正式参数遵循像遮蔽类中类方法参数和实例变量这样的规则。举个例子，bar的声明:

    class Bar { int i; Foo foo = i -> i * 2; };

is legal because the lambda parameter i shadows the instance variable, whereas for local variables the usual rule of assignment before use applies, so that the method declaration
合法的原因是因为lambda参数i遮蔽了实例变量（int i)，然而本地变量赋值之前的规则通常是使用申请，所以类方法声明

    void bar() { int i; Foo foo = i -> i * 2; };	// Illegal: variable i is already defined
	错误，变量i已经定义

does not compile.

没有成功编译。