
----------
 
***本文仅供学习和交流使用，如果您发现我已经侵犯到原作者的版权，请邮件我ttchgm@gmail.com。以便我及时删除和处理。如果翻译有错误或者交流可以随时mail我。或者在sina微博 @天天吃好，私信与我。 本文拒绝任何形式转载。***

----------

#Can lambda expressions be used to define recursive functions?
#lambda表达式能被使用定义递归函数吗？

Yes, provided that the recursive call uses a name defined in the enclosing environment of the lambda. This means that recursive definitions can only be made in the context of variable assignment and, in fact—given the asssignment-before-use rule for local variables—only of instance or static variable assignment. So, in the following example, factorial must be declared as an instance or static variable.

是的，可以认为递归调用使用一个名字定义在一个封闭的lambda环境中。这里的意思是递归定义能仅在变量赋值的上下文中和事实上在赋值之前使用的规则为：本地变量仅为实例或者静态变量赋值。所以，在下面的例子中，factorial 必须被声明成一个实例或者静态变量。
Example
例子

    interface FactInt { int invoke(int i); }
    FactInt factorial = i -> { return i == 0 ? 1 : i * factorial.invoke(i - 1); };