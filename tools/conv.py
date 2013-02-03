# *.* coding=utf8 *.*
import hashlib
import sys, os,stat

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from jinja2 import Template
import markdown

work_dir = u"..\\posts\\"
index_html = u"..\\index.html"

"""
	1 fork work_dir
	2 create hash - name list
	3 create index
"""

update_list = []

ul = {}

def getFileC(f):
	r = ""
	for x in open(f).readlines():
		r += x
	return r
def writeFileC(c,f):
	wf = open(f,"w")
	wf.write(c)
	wf.close()

def reader(s,d):
	return Template(s).render(d)


class updObj:
	def __init__(self,name,hashID,sdpath,fullpath):
		self.name = name
		self.hashID = hashID
		self.sdpath = sdpath
		self.fullpath = fullpath

def walk_(path ,sdpath=None):	
	for item in os.listdir(path):
		subpath = os.path.join( path, item )
		mode = os.stat(subpath)[stat.ST_MODE]
		#print item
		if stat.S_ISDIR(mode):
			walk_(subpath,item)
		else:
			fname = os.path.splitext(item)
			if fname[1] == '.md':
				o = updObj(( fname[0] ),getHASHID( fname[0].encode("utf-8") ),sdpath,path+"\\"+item)
				update_list.append( o )
				ul[sdpath] = ""
			#	print sdpath
			#	print subpath
			#	print fname[1]
			#	print getHASHID( fname[0].encode("utf-8") )	

def getHASHID( s ):
	""" get a hash ID , param : s -> is a source string . return : hashString  """
	return hashlib.sha224( s ).hexdigest()

if __name__ == "__main__":
	#sys.argv[1]
	#print getHASHID( sys.argv[1] )
	walk_(work_dir)
	sd_path = {}

	writeFileC( reader(getFileC(u".\\_template\index.html").decode("utf-8"),\
						{
								"title" : "天天吃好的BLOG".decode("utf-8"),
								"docs_title" : sd_path,
								"docs_ns" : update_list
						}	\
						).encode("utf-8") , index_html )
	
	md = markdown.Markdown()
	for a in update_list:
		c = md.convert( getFileC(a.fullpath).decode("utf-8") )
		writeFileC (	reader(getFileC(u".\\_template\_post.html").decode("utf-8"),\
				{
						"c" : c,
						"title" : a.name
				}	\
				).encode("utf-8"),"..\\_posts\\"+a.hashID+".html" )
	"""	
	code = 'print "hello World"'
	print highlight( code,PythonLexer(), HtmlFormatter() )
	print HtmlFormatter().get_style_defs('.highlight')
	"""
