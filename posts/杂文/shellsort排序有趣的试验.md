#shellsort排序有趣的试验

今天和同事讨论关于一个shell排序的问题。

原因是在[<算法>](http://www.amazon.cn/%E7%AE%97%E6%B3%95-%E5%A1%9E%E5%A5%87%E5%A8%81%E5%85%8B/dp/B009OCFQ0O/ref=sr_1_1?ie=UTF8&qid=1359129831&sr=8-1)这本书上看到的方法，其中代码就不贴出来了，因为效率不是十分高。那么同事给我演示的是`23秒`多。我当时用python写了半天也没逾越这个数！我们机器是一样的配置一样的型号，几乎没有不同，除了密码！处理器是i5 2450 4核心，使用的是同样的数据样本。我用的是python2.5，他使用的是python2.7。因为程序是在同一个机器上跑的，跑完到另一个机器跑。

[wiki版本](http://en.wikibooks.org/wiki/Algorithm_implementation/Sorting/Shell_sort)（不少网站都会贴着个代码）


	def shellSort(array):
		"Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
		gap = len(array) // 2
		# loop over the gaps
		while gap > 0:
		# do the insertion sort
			for i in range(gap, len(array)):
				val = array[i]
				j = i
				while j >= gap and array[j - gap] > val:
					array[j] = array[j - gap]
					j -= gap
				array[j] = val
			gap //= 2
	


然后我发现我代码的中间变量和冗余代码十分多，我尝试砍掉中间变量。我们就用中间修改差不多的原始版本吧，我们这里做为第一版本！


	def sort(a):
		n = len(a)
		h = n // 2
		while h > 0:
			#print h
			for i in xrange(h , n):
				val = a[i] #注意这个地方
				for j in xrange(i,h-2,-h):
					if a[j-h] > val : temp = a[j-h] ; a[j-h] = a[j] ; a[j] = temp
					else: break
			h //= 2

第1次修改
>这个版本我修改掉了交换值，这个小小的增加一个开销pack和unpack的时候，总体会增加不到0.01秒。但代码的可读性很高！


	def sort(a):
		n = len(a)
		h = n // 2
		while h > 0:
			#print h
			for i in xrange(h , n):
				val = a[i]
				for j in xrange(i,h-2,-h):
					if a[j-h] > val : a[j],a[j-h] = a[j-h],a[j]
					else: break
			h //= 2

第2次修改：

> 这里很重要，我修改掉了else。这里用了一个测试中看到的`情况1`。`就是如果子条件内进行for循环时，如果发现需要交换的变量，那么循环可以结束！`这个直接减少了大概10秒左右的开销，也就是接近，有的时候会快过wiki版本的平均值。


	def sort(a):
		n = len(a)
		h = n // 2
		while h > 0:
			#print h
			for i in xrange(h , n):
				val = a[i]
				for j in xrange(i,h-2,-h):
					if a[j-h] > val : a[j],a[j-h] = a[j-h],a[j] ; break
			h //= 2



最终版本：

>这里我去掉了临时变量，这里很关键，秒杀wiki版本的另一个重要 `情况2`:`情况1` `发生的前置条件中的被对比值必然是要交换的值。`根据这个直接改掉程序，秒杀接近4个秒单位！


	def sort(a):
		n = len(a)
		h = n // 2
		while h > 0:
			for i in xrange(h , n):	
				for j in xrange(i,h-2,-h):
					if a[j-h] > a[j] : a[j],a[j-h] = a[j-h],a[j] ; break
			h //= 2

这里为什么说是情况，而不是说定理？因为我证明不了。。哈哈。这个过程太复杂。
至此，算是7行解决了这个问题，从时间开销和代码行数都完爆wiki版本的程序。

总结：感谢图灵能够出版[<算法>](http://www.amazon.cn/%E7%AE%97%E6%B3%95-%E5%A1%9E%E5%A5%87%E5%A8%81%E5%85%8B/dp/B009OCFQ0O/ref=sr_1_1?ie=UTF8&qid=1359129831&sr=8-1)这本书的翻译版本，更感谢[@一盆花](http://weibo.com/hellmage) 谢大给我们带来这么好的书。只有思考才会发现，只有发现才能改变，改变错了，再思考，呵呵。