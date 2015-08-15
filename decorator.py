
def logger(func):
	def wrapper(*args, **kwargs): #1
		print "Arguments were: %s, %s" % (args, kwargs)
		return func(*args, **kwargs) #2
	return wrapper

# this
def foo3():
	return 3
foo3 = logger(foo3)

# can also be written as
@logger
def foo1(x, y=1):
	return x * y

@logger
def foo2():
	return 2

print foo1(5, 4)

print foo1(1)

print foo2()
	
print foo3()