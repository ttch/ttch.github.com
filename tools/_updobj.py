# *.* coding=utf-8 *.*
class updObj:
	def __init__(self,name,hashID,sdpath,fullpath,dtime):
		self.name = name
		self.hashID = hashID
		self.sdpath = sdpath
		self.fullpath = fullpath
		self.dtime = dtime


def isort(alist):
	h = len(alist)
	for i in range(h):
		if i == 0: continue
		value = alist[i]
		j = i-1
		while j >=0  and alist[j].dtime<=value.dtime:
			alist[j+1] = alist[j]
			
			j = j-1
		alist[j+1] = value
	return alist
#没搞定，对比上好像有些问题，上班时间不看了，先挖个坑
def msort(a):
	n = len(a)
	h = n // 2
	while h > 0:
		for i in xrange(h , n): 
			for j in xrange(i,h-2,-h):
				print a[j-h].dtime , " < " , a[j].dtime, " 结果 " , ( a[j-h].dtime < a[j].dtime )
				if a[j-h].dtime < a[j].dtime : a[j],a[j-h] = a[j-h],a[j] ; break
		h //= 2
	return a
	
