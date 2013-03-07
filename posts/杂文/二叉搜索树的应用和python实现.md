
#二叉搜索树的应用和python实现

----

##二叉搜索树的应用：

- 给出一段报文和每个字符出现的频率，对其进行haffman编码和解码。


二叉树的结构：
> 一个节点包含的内容有：key,value,left,right,parent


*节点存储定理：*

    left.key <= key
    right.key >= key

**定理 1：**
> 如果x是一棵有n个结点子树的根，那么中序遍历x需要O(n)时间。

**定理2：**
> 在一棵高度为h的二叉搜索树上，动态集合上的操作 SEARCH,MINIMUM,MAXIMUM,SUCCESSOR和PREDECESSOR可以在O(h)时间内完成。 h为树高。

**定理3：**
> 在一棵高度为h的二叉搜索树上,实现动态集合操作 INSERT,DELETE的运行时间均为O(h)。h为树高。

##python实现


结点类结构:

    class node:
	    def node(self,key,val,r=None,l=None,p=None):
		    self.l = None
		    self.r = None
		    self.key = None
		    self.val = None
		    self.p = None

建立以个结点：

    def createnode(key,val,r=None,l=None,p=None):
	    return node(key,val,r,l,p)

插入一个结点(INSERT):

    def put(p,key,val):
		y = None
		x = p.root
		z = createnode(key,val)
	
		while x != None:
			y = x
			x = ( x.l if z.key<x.key else x.r)
		z.p = y
		if y == None:
			p.root = z
		elif z.key < y.key :
			y.l = z
		else: y.r = z

迁移一个结点(transplant)

	def transplant(t,u,v):
		if u.p == None:
			t.root = p
		elif u == u.p.left:
			u.p.left = v
		else: u.p.right = v
		if u != None:
			v.p = u.p














