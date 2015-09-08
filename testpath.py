#import lib.foo1 as f
#f.foo()

#from lib import foo1
#from lib import bar1
import lib

foo()

abar = foo1.fooclass()

class foosubclass(foo1.fooclass):
	def test(self):
		print 'test foosubclass'

