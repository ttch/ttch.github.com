#java趣味短码-for的逻辑操作对比


前面介绍了三元表达式和三元表达式的用法，当然还有迭代器。下面就是一个比较特殊的问题，for的写法长度比较和优劣。当然这也是一个和童鞋讨论思考了很久的问题。

首先说明一下里面的做法参考的stackoverflow中的一篇讨论贴子中的[关于each的做法](http://stackoverflow.com/questions/8556628/how-do-i-implement-rubys-each-method-in-java/8556644#8556644)。


###首先我们准备一下相关函数

>建立一个接口，用来实现each操作用的

	interface Function<T>{
		public void func(T Item);
	}

>实现一个each函数。

	@SuppressWarnings("unchecked")
	public static <T> void each(Collection<T> s, Function f){
		for ( T a : s){
			f.func(a);
		}
	}

>实现一个集合增加元素的三元表达式逻辑操作函数。

	public static <T> int add_(Collection<T> s, T item){
		s.add(item);
		return 0;
		
	}



>我们的需求如下：


###***需求1***：在指定的List中去掉小于等于2的元素，大于2的元素放到目标列表d中，并打印d中所有的元素，我们只针对过滤元素的程序部分进行优化。

	List <Integer> l = Arrays.asList(1,2,3,4,5,6,7);
	
	final List <Integer> d = new ArrayList<Integer>();
	
	for ( Integer a : l){
		if (a > 2){ d.add(a); }
	}

> 我们需要优化的代码如下：

	for ( Integer a : l){
		if (a > 2){ d.add(a); }
	}

下面我们看看，有2种写法：

	//first
	test03.each(l, new Function<Integer>(){	
		@Override
		public void func(Integer Item) { if ( Item > 2) { d.add(Item); } }
	});

***优点***：去掉了for，把他封装到了函数里，更专注元素的处理，且逻辑更鲜明，代码行数的可预料性大。

***缺点***：可扩展的难度十分大，比如需要2个元素对比等，需要开发不同的需求的each版本，不过实际上这个缺点也算是优点，因为会使代码规范化，程序更能公式化。

	
	for ( Integer a : l ){ int b = ( a >2 ? add_(d,a) : 0  ) ; }

***优点***：仅仅从代码行数和代码文字列数来说，这样写确实精简了。

***缺点***：几乎不适合作为client-code的典范，不推荐这样写。

> 总结： 从上面看，如果刚开始就需要对代码进行统计和规范化建议first写法，并且可以开发出来一套这样的函数式框架提供给程序员，代码的统计和代码的规范化更易于预测和思考（因为基本都可以通过公式化的开销来计算）


###***需求2***：在指定的List中 小于等于2的元素增加1并存放在目标列表中，大于2的元素直接放到目标列表中。

源代码如下：

	for ( Integer a : l){ if (a > 2){ d.add(a); } else { d.add( a + 1); } }

>写法 1

	//first
	test03.each(l, new Function<Integer>(){	
		@Override
		public void func(Integer I) {
			if ( I > 2) { d.add(I); } else { d.add(I+1); }
		}
	});


***优点***：同上。

***缺点***：同上。

***补充*** : 这时候已经能够凸显`固定模式`的`函数式编程`的特点了。


>写法2

	//second
	for ( Integer a : l ){ int b=( a >2 ? add_(d,a) : add_(d,a+1) ); }


***优点***：比标准写法短了不少！。

***缺点***：对更多的if elseif else这样的结构，这种写法直接就被pass了，所以经证明这种写法在if else这样的条件结构的时候，还蛮不错。

###***总结***:

> 需求1，不优化是最简洁的，但第1种优化的扩展和模式化编程较好。

> 需求2，第2种优化最短，可读性也不错，但扩展性为0

>***结论***：第一种优化确实不错的，在Java中android平台被这种写法是被广泛应用。


