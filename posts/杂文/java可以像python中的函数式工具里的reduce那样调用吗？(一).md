#函数式工具(一) - java可以像python中的函数式工具里的reduce那样调用吗？




python 里这样写，在java里是否也能这样写吗？

    reduce(add, range(1, 11))
	reduce(max,[11,-25])

能！

> 首先我们实现reduce这个函数。当然不可能事先全，因为java全处理的话，需要很长的代码，我们这里暂时只举3个例子。


	class ob{
		@SuppressWarnings("unchecked")
		
		public static <T> T reduce(Class c , String m , T ... objects  ) {
			for ( Method tm :c.getDeclaredMethods() ){
				if( m.equals(tm.getName() ) ){
					if (tm.getParameterTypes().length == 1){
						if ( tm.getParameterTypes()[0].isArray() == true){
							tm.setAccessible(true);
							try {
								T [] a = (T[]) new Object[1]; 
								a[0] = (T) Arrays.asList(objects).toArray();
								return (T) tm.invoke(null, a);
							} catch (IllegalArgumentException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							} catch (IllegalAccessException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							} catch (InvocationTargetException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
						}
					}
					if ( objects.length ==  tm.getParameterTypes().length ){
						
						/*个别参数查找**/
						for (int i = 0 ; i<tm.getParameterTypes().length;i++){
							if (tm.getParameterTypes()[i]
								.getSimpleName().toLowerCase().equals(

								objects[i].getClass().
								getSimpleName().toLowerCase() ) )
							{
								tm.setAccessible(true);
								try {
									return (T) tm.invoke(null, objects);
								} catch (IllegalArgumentException e) {
									// TODO Auto-generated catch block
									e.printStackTrace();
								} catch (IllegalAccessException e) {
									// TODO Auto-generated catch block
									e.printStackTrace();
								} catch (InvocationTargetException e) {
									// TODO Auto-generated catch block
									e.printStackTrace();
								}
							}
						}
						
						
					}
				}
			}
			return null;
		}
	}



首先一点，上面的类实现的不是非常完美，会在以后的文章中慢慢的重构和优化他。

因为Math对象中没有add类，那么我们自己建立以个MyMath对象

	class myMath{
		public static Integer add(Integer[] is){
			Integer result = 0;
			for (Integer a : is ){
				result += a;
			}
			return result;
		}
		
	}

我们的建立一个试验函数吧！！。。激动人心的时刻到了

	List<Integer> x = Arrays.asList(1,2,3,4,5,6,7);
	
	Integer c = (Integer) ob.reduce(myMath.class, "add", x.toArray());
	System.out.println(c);

打印的结果为

	28


OY! 我们成功了。


那么我们建立的reduce函数也支持math中的大部分操作


	double b = ob.reduce(Math.class,"max",1.2,3.2);
	System.out.println(b);
	
	Double a = ob.reduce(Math.class,"abs",-2.2);
	System.out.println(a);


例子代码如上。分别会打印出来 3.2和 2.2

这样看起来我们的java程序是不是更加函数化了呢？当然对于xrange和range很好实现，这里就不给出现了。

以下是使用range或者xrange的样例代码。

    Integer c = (Integer) ob.reduce(myMath.class, "add", range(1,7);

是不是有点函数式编程的味道了？

哈哈





