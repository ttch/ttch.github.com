
----------
 
***本文仅供学习和交流使用，如果您发现我已经侵犯到原作者的版权，请邮件我ttchgm@gmail.com。以便我及时删除和处理。如果翻译有错误或者交流可以随时mail我。或者在sina微博 @天天吃好，私信与我。 本文拒绝任何形式转载。***

----------


#Can lambda expressions use variables from their environment?

#lambda表达式能使用来自他们环境的变量吗？

Yes. This is called variable capture. Instance and static variables may be used and changed without restriction in the body of a lambda.The use of local variables, however, is more restricted: capture of local variables is not allowed unless they are effectively final, a concept introduced in Java 7.Informally, a local variable is effectively final if its initial value is never changed (including within the body of a lambda expression)—in other words, declaring it final would not cause a compilation failure. The concept of effective finality does not introduce any new semantics to Java; it is simply a slightly less verbose way of defining final variables. The rationale for requiring captured local variables to be effectively final is explained here.

是的。这是调用变量捕获。实例和静态变量可以被使用，并且在lambda主体内改变这些变量没有任何限制。使用本地变量，无论如何，是更多限制：本地变量捕获并不允许，除非他们实际上是`final`，这是在java 7中引进的一个概念。非正式地，一个本地变量实际上是`final`的，如果他的初始化值是永远不会改变在其他地方（包括在lambda表达式主体内)，声明他为final并不会引起一个compilation failure。最终的决定是：并没有为Java引入任何新的语义；他只是一个在定义final变量上有细小改变的版本。本地变量捕获请求的基本原理是最终解释在这 [戳进][1]。


  [1]: http://www.lambdafaq.org/what-are-the-reasons-for-the-restriction-to-effective-immutability/