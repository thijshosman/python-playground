
temp1 = 1.2221122
temp2 = 1.3

print "%.1fC %.0fF" % (temp1,temp2)

def table_things(**kwargs):
	right_color = [1,2,3]
	for name, value in kwargs.items():
		print '{0} = {1}'.format(name, value)
	if 'color' in kwargs:
		test_color = kwargs['color']
		#print kwargs['color']
		if right_color == test_color:
			print "right"

class kwargs_test(object):

	def __init__(self):
		self.color = [1,1,1]
	def test(self,*args,**kwargs):
		#if 'color' in kwargs: 
		for name,value in kwargs.items():
			print '{0} = {1}'.format(name,value)
		for arg in args:
			print arg
		#	self.color = kwargs['color']
		#print self.color

kt = kwargs_test()
a=1
b='b'
kt.test('hallo',color=[1,2,3],a=a,test2=b)
print kt.color

def a():
	return 1,2,3,4

output = []

outp = a()

for item in outp:
	print item


#for key,value in outp:
#	print '{0} - {1}'.format(key,item)

#table_things(apple = 'fruit', cabbage = 'vegetable', color = [1,2,2])

print "%.1f %.1f" % (temp1,temp1)
print '{0} = {1}'.format(temp1,temp1)

def printT(arg):
	print "%s" % arg

printT("%.1f %.1f" % (temp1,temp1))


