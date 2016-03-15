#testing path of python libraries in subfolders
# there needs to be an __init__.py in a subfolder
#subdir is called lib

# this imports the foo1.py file from the subdir lib
import lib.foo1 as f
f.foo()

#these are alternatives for importing
from lib import foo1
foo1.foo2()

#if lib had subdirs, they could be imported like this as well
#from lib.subdirlib import *

#import everything
# works only when __all__ is defined in the __init__.py in subdir
from lib import *
bar1.barfunction()
abar0 = bar1.bar()

# or this way, but needs full path to call
import lib.bar1
abar1 = lib.bar1.bar()

#import specific function
from lib.bar1 import barfunction
barfunction()


foo1.foo()

afoo = foo1.fooclass()

class foosubclass(foo1.fooclass):
	def test(self):
		print 'test foosubclass'

