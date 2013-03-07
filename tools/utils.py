from jinja2 import Template

def stampToTime(t):
	from datetime import datetime, date, time
	return datetime.fromtimestamp(t)

def getFileC(f):
	r = ""
	for x in open(f).readlines():
		r += x
	return r
def writeFileC(c,f):
	print f
	wf = open(f,"w")
	wf.write(c)
	wf.close()

def reader(s,d):
	return Template(s).render(d)

