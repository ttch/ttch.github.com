 ***本文仅供学习和交流使用，如果您发现我已经侵犯到原作者的版权，请邮件我ttchgm@gmail.com。以便我及时删除和处理。如果翻译有错误或者交流可以随时mail我。或者在sina微博 @天天吃好，私信与我。 本文拒绝任何形式转载。***


#Where can lambda expressions be used?

#lambda表达式能在哪里使用?

Lambda expressions can be written in any context that has a target type. The contexts that have target types are:

lambda表达式能被写在任何有目标类型的上下文中。哪些上下文可以有目标类型：


 - Variable declarations and assignments and array initializers, for which the target type is the type (or the array type) being assigned to;

 - 变量声明和赋值和数组初始化，针对这种目标类型赋值为一个类型（或者数组类型）；

 - Return statements, for which the target type is the return type of the method;

 - 返回段，针对这种目标类型，是函数的返回类型。

 - Method or constructor arguments, for which the target type is the type of the appropriate parameter. If the method or constructor is overloaded, the usual mechanisms of overload resolution are used before the lambda expression is matched to the target type. (After overload resolution, there may still be more than one matching method or constructor signature accepting different functional interfaces with identical functional descriptors. In this case, the lambda expression must be cast to the type of one of these functional interfaces);

 - 类方法或者构造类方法的参数，针对这些目标类型是对应的参数类型。如果类方法或者构造类方法被重载，通常重载解析机制是使用在lambda表达式匹配目标对象之前。(在重载解析之前，他们可以仍跟不止一个类方法签名或者构造类方法签名，接受不同的函数式接口但相同的函数式描述符。在这个例子中，lambda表达式必须转换一个对应签名的函数式接口的类型。）；

 - Lambda expression bodies, for which the target type is the type expected for the body, which is derived in turn from the outer target type. Consider

 - lambda表达式主体，目标类型是根据预期的主体类型，且预期的主体类型在目标类型之外的衍生体。认为


    Callable<Runnable> c = () -> () -> { System.out.println("hi"); };

The outer target type here is Callable<Runnable>, which has the function descriptor
外层目标类型在这里是Callable<Runnable>,他的函数描述是

     Runnable call() throws Exception;

so the target type of the lambda body is the function descriptor of Runnable, namely the run method. This takes no arguments and returns no values, so matches the inner lambda above;

所以lambda主体的目标类型是Runnable的函数描述，也就是运行类方法。这里没有接受任何参数并且没有返回任何返回值，所以匹配如上内部lambda；

Tertiary conditional expressions (?:), for which the target type for both arms is provided by the context. For example:

三段条件表达式(?:)，目标类型,根据后两个表达式的上下文。如下例子：

     Callable<Integer> c = flag ? (() -> 23) : (() -> 42);

Cast expressions, which provide the target type explicitly. For example:

转换表达式明确的提供是哪一个目标类型。如下例子：

    Object o = () -> { System.out.println("hi"); };
    // Illegal: could be Runnable or Callable
    // 非法:不能是Runnable或者Callable
    Object o = (Runnable) () -> { System.out.println("hi"); };
    // Legal because disambiguated
    //合法原因是消除歧义



