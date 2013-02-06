# *.* coding=utf8 *.*
import hashlib
import sys, os,stat

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

import markdown

import utils
from _topic import topic
from _updobj import updObj

work_dir = u"..\\posts\\"
index_html = u"..\\index.html"


configs = {
	"updall" : True	#is update all
}

# post all
update_list = []
#topic dir
topics = {}


def walk_(path,subpath=None):	
	for item in os.listdir(path):
		subpath = os.path.join( path, item )
		mode = os.stat(subpath)[stat.ST_MODE]
		dtime = utils.stampToTime( os.stat(subpath)[stat.ST_CTIME] )
		if stat.S_ISDIR(mode):
			walk_(subpath,item)
			if subpath != None:
				name = item
				hashID = getHASHID( item.encode("utf-8") )
				topics[item] = topic(item,hashID )
		else:
			fname = os.path.splitext(item)
			if fname[1] == '.md':
				o = updObj(( fname[0] ),getHASHID( fname[0].encode("utf-8") ),subpath,path+"\\"+item,dtime)
				update_list.append( o )
				#print os.stat(item.encode("utf-8"))


def getHASHID( s ):
	""" get a hash ID , param : s -> is a source string . return : hashString  """
	return hashlib.sha224( s ).hexdigest()

if __name__ == "__main__":

	topics = {}
	walk_(work_dir)

	# write index.html
	utils.writeFileC(	\
		utils.reader	\
		(utils.getFileC(u".\\_template\\index.html").decode("utf-8"),\
		{
			"title" : "天天吃好的BLOG".decode("utf-8"),
			"topics" : topics,
			"docs_ns" : update_list
		}	\
		).encode("utf-8") , index_html )
	
	#to-do write topic.html
	for x in topics:
		utils.writeFileC(	\
			utils.reader	\
			(utils.getFileC(u".\\_template\\topics.html").decode("utf-8"),\
			{
				"title" : topics[x].name,
				"topics" : topics,
				"docs_ns" : update_list
			}	\
			).encode("utf-8") , "..\\topics\\"+topics[x].hashID+".html" )  
	# write _post.html
	md = markdown.Markdown()
	for a in update_list:
		c = markdown.markdown(	\
		utils.getFileC(a.fullpath).decode("utf-8"),[
			'codehilite(	\
			force_linenos=True,	\
			guess_lang=True,	\
			css_class=colorful,	\
			pygments_style=native,	\
			noclasses=True)'	\
		])

		utils.writeFileC (	utils.reader(	\
				utils.getFileC(u".\\_template\\_post.html").decode("utf-8"),\
				{
						"c" : c,
						"title" : a.name
				}).encode("utf-8")	\
				,"..\\article\\"+a.hashID+".html" )

