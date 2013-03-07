#Java趣味短码 - 能像 python的 enumerate一样吗？


昨天和童鞋讨论过关于IF，然后童鞋的朋友是个pythoner，也在一起讨论，当时提出一个问题，java没有像python里的enumerate这个东西吧？其实java里没有的东西还慢多的。不过我们可以让他有。


下面是python的代码

	for index,var in enumerate(a):
		tl = tl + [ var-n+index , var , var+n-index ]

enumerate(a)

假设
	
	a = ["test","hello","test"]

能根据a的结构生成如下结构：

 	a = (0,"test"),(1,"hello"),(2,"test")

---

在java中如何实现呢？

如果你去搜索stackoverflow 找到这样一篇[文章,戳进](http://stackoverflow.com/questions/7167253/is-there-a-java-equivalent-of-pythons-enumerate-function)

里面的方法是这样
	
	List<String> numbers = Arrays.asList("zero", "one", "two");
	ListIterator<String> it = numbers.listIterator();
	while (it.hasNext()) {
    	System.out.println(it.nextIndex() + " " + it.next());
	}


如上的方法虽然实现了基本需求，但不美观。

那么我们怎么实现呢？

思路如下：
	
- 实现迭代器
- 建立一个替代对象，增加一个索引和一个对象。

首先定义一个迭代对象

	@SuppressWarnings("unused")
	class Enum{	
		public int I;
		public Object Obj;
		public Enum( Object Obj , Integer I){
			this.I = I;
			this.Obj = Obj;
		}
	}

然后我们定义enumerate对象


	@SuppressWarnings("unchecked")
	class Enumerate<T>  implements Iterator<Enum> , Iterable<Enum>{
		private Iterator it ;
		private int current;
	
		public Enumerate(Collection<T> t){
			it = t.iterator();
		}
	
		@Override
		public boolean hasNext() {
			return it.hasNext();
		}
	
		@Override
		public Enum next() {
			return new Enum(it.next(),++current);
		}
	
		@Override
		public void remove() {
			it.remove();
			
		}
	
		@Override
		public Iterator<Enum> iterator() {
			return this;
		}
	}


这个对象我们增加了一个current计数器。用来返回index的

这里要说明为什么不用stackoverflow帖子中的方法，缺点就是当list或者set这种集合过大的时候。那么你的算法周期就要*2。这是很难让人接受的事情。

所以使用迭代的话，会逐条记录返回，这样不会改变原来的代码时间。

SO!我们可以看到如下代码了。


	for ( Enum a : new Enumerate<Integer>(l)){
		System.out.println(a.Obj);
		System.out.println(a.I);
	}

是不是感觉很酷！


下面的代码是一份完整的代码样例。


	package tPackge;
	
	import java.util.AbstractList;
	import java.util.ArrayList;
	import java.util.Arrays;
	import java.util.Collection;
	import java.util.Iterator;
	import java.util.List;
	import java.util.ListIterator;
	import java.util.NoSuchElementException;
	
	
	@SuppressWarnings("unused")
	class Enum{	
		public int I;
		public Object Obj;
		public Enum( Object Obj , Integer I){
			this.I = I;
			this.Obj = Obj;
		}
	}
	
	@SuppressWarnings("unchecked")
	class Enumerate<T>  implements Iterator<Enum> , Iterable<Enum>{
		private Iterator it ;
		private int current;
	
		public Enumerate(Collection<T> t){
			it = t.iterator();
		}
	
		@Override
		public boolean hasNext() {
			return it.hasNext();
		}
	
		@Override
		public Enum next() {
			return new Enum(it.next(),++current);
		}
	
		@Override
		public void remove() {
			it.remove();
			
		}
	
		@Override
		public Iterator<Enum> iterator() {
			return this;
		}
	}
	
	public class test02 {
	
		/**
		 * @param args
		 */
		public static void main(String[] args) {
			List <Integer>  l = Arrays.asList(1,2,3,4,5,5);
	
			int i = 0;
			for ( Integer a : l){
				System.out.println(i);
				System.out.println(a);
				i++;
			}
	
			for ( Enum a : new Enumerate<Integer>(l)){
				System.out.println(a.Obj);
				System.out.println(a.I);
			}
		}
	
	}
	
