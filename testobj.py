class MyClass(object):
	def __init__(self,foo="foo1",bar="bar1"):
		self.foo = foo
		self.bar = bar
	
	# __repr__ is intended to allow you to describe this class for logging etc
	def __repr__(self):
		return "MyClass(foo=%r,bar=%r)" % (self.foo,self.bar)



a = MyClass("foo2","bar2")
print(a)
