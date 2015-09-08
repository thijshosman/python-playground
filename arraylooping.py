import time


class testclass(object):


	def __init__(self):
		self.t = 4
		self.arr = xrange(4)
		print self.t

	def add(self):
		self.t = self.t+1

	def t1(self):
		print self.t
		print len(self.arr)


b=testclass()
b.add()
b.t1()


# get time in seconds
t=time.time()
# now convert it
print time.localtime(t).tm_hour
print time.localtime(t).tm_min

# time now
print time.strftime('%H:%M')

i=-1
print "mod",abs(i)%7
print "mod",i%7

def j():
	return 1

print j()

i=0

colorArray = ['red','green','blue','yellow','cyan','magenta','white']

for i in xrange(10):
	color = colorArray[(i+1)%7]
	print color



