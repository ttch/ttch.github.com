About the Lambda FAQ(关于Lambda的问答集)

原文地址：http://www.lambdafaq.org/

 ***本文仅供学习和交流使用，如果您发现我已经侵犯到原作者的版权，请邮件我ttchgm@gmail.com。以便我及时删除和处理。如果翻译有错误或者交流可以随时mail我。或者在sina微博 @天天吃好，私信与我。 本文拒绝任何形式转载。***

  关于如何在java中引入lambda表达式的长期讨论中(aka closures)，我们接近了一个重要的时刻：lambdas的实现和虚函数扩展是计划在2012年1月底[完成的特性][1]，紧随其后9月份会在发布JDK8中正式加入其中。这是在Java 5开始后的做的最大的变化，发布日期离我们并不遥远。 

> ***aka closures***的完整叙述，一个闭包是一个lambda表达式对，在表达式对内的环境绑定所有自由变量到一个值。在Java中，Lambda表达式将实现的意义为闭包，所以两个关系可以使用在区间内交换使用。

>关于aka closures可以参考这个链接 http://lists.cs.uiuc.edu/pipermail/cfe-dev/2008-August/002670.html

我开始思考关于这些新特性，所以Phil Wadler 和我认为应该有一本新版本的<<[Java Generics and Collections][2]>>的书。这里特别重要，尤其重要的是关于集合，我们需要做出大量的修改保持当前这本书中的例子适应lambda表达式以及lambda表达式更广泛的使用。

新的特性并不是在第一时间都能消化的，所以这个FAQ有益于让你在我的劳动成果中学习到他们。我希望她对你有帮助，无论你是否已经熟悉了lambda表达式或者第一时间早已接触到了lambda表达式。我高兴接受任何您的评论和贡献。


  [1]: http://openjdk.java.net/jeps/126
  [2]: http://shop.oreilly.com/product/9780596527754.do