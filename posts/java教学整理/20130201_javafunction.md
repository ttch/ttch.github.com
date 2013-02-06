#function

大家强烈说一下java里的`function`，可惜java里没有`纯粹意义`上的`function`

java因为是面向对象语言所以只有method

无论如何！他都是围绕method基础上进行的。

那么我们来看一下function的概念：


-  call调用。

- BackCall调用。


那么我们先看一下载java中如何实现上面概念的。

function声明（严格意义上这个叫interface method 如果声明我觉得应该叫 interface function Signature )

    interface a {
    	public void test();
	}
	
	class b{
		public void test( interface a){
			a.test();
		}
	}
	
调用如下：

	new a(){
		@override
		public void test(){
			System.out.println("hello");
		}
	}.test();


回调如下：

	new b().test(new a(){
		@override
		public void test(){
			System.out.println("hello");
		}
	}
    


习题：

习题1 请写出 interface instance  function ,interface function 两种的调用和回调方法。
习题2 写一个插入排序 并在其中考虑如何使用function
习题3 思考一下什么情况会这么用，什么情况不适合这么用？这么用的好处是什么？


