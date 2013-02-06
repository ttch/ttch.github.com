

#Java趣味短码 - (第一节)

今天跟公司的童鞋聊天的时候，谈到了关于短码和代码的精简的方式，所以整理出来。

需求很简单。

首先定义一个类

    class Item{
		public int key;
		public int l;
		public int r;
    };


然后主函数的场景大概是这样

	public static void main(String[] args) {
		Item x;
		x = new Item();
		x.key = 1;
		x.l = 10;
		x.r = 20;
		
		int i = 0;

		if (x.key > i){
			i = x.l;
		}else{
			i = x.r;
		}

		i = 0；
		if ( x.key > i){
			x.l = i;
		}else{
			x.r = i;
		}
	}

这里面有两个子场景，就是接下来要讨论的。

子场景1

		if (x.key > i){
			i = x.l;
		}else{
			i = x.r;
		}

子场景2

		if ( x.key > i){
			x.l = i;
		}else{
			x.r = i;
		}

- 子场景1 的规律是 左面的值都是一样的，都是赋值给i

- 子场景2 的规律是 右面的值都是一样的，都是用i赋给别的变量。

>那么我们如何来简化实现这两类场景呢？

第一个场景很简单，可以如下优化：

    i = ( x.key >i ? x.l : x.r);

第二个场景比较棘手！

因为表达式不能被赋值。

所以我们增加一个函数：

	public static  boolean to_(Object s ){
		return true;
	}

有了如上函数我们就可以这样写

    ( x.key >i ? to_( x.l = i ): to_(x.r = i) )

这里的含义就是先复制给x.l或者x.r根据x.key>i的真假值。然后传给to_函数，至于to_不会考虑传过来的值是多少。反正x.key>i都会判断。直接暴力返回true。这样就完美的解决了左赋值的问题。也解决了Integer和int无法passbyValue的问题。

如下是完整的代码。
	
	package tPackge;
	
	
	class Item{
		public Integer key;
		public Integer l;
		public Integer r;
	};
	
	public class test01 {
		public static  boolean to_(Object s ){
			return true;
		}
		/**
		 * @param args
		 */
		public static void main(String[] args) {
			Item x;
			x = new Item();
			x.key = 1;
			x.l = 10;
			x.r = 20;
			
			Integer i = 0;
			
			if (x.key > i){
				i = x.l;
			}else{
				i = x.r;
			}
			System.out.println(x.l);
			System.out.println(x.r);
			System.out.println(i);
			System.out.println("--------------------------");		
			i = ( x.key >i ? x.l : x.r);
			System.out.println(x.l);
			System.out.println(x.r);
			System.out.println(i);
			/*
			if ( x.key > i){
				x.l = i;
			}else{
				x.r = i;
			}
			*/
			System.out.println("--------------------------");
			i = 0;
			//if ( x.key > i ) { x.l = i; } else { x.r = i; } 
			
			//if ( ( x.key >i ? ( ( x.l = i ) == i ): ( (x.r = i) == i ) ) ){ System.out.println(i); }
			if ( ( x.key >i ? to_( x.l = i ): to_ (x.r = i) ) ){ System.out.println(i); }
			System.out.println(x.l);
			System.out.println(x.r);
		}
	
	}
	
	
	