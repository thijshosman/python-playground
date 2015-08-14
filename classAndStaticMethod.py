class A(object):
    def __init__(self,value = 1):
        self.val = value
        print "A instantiated with %s"%(value)

    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    def bar(self):
        print 'bar'

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @classmethod
    def factory(cls,y):
        print "product is %s"%y 
        return cls(y)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x    

a=A()

# class methods
# class is first argument of function
# call from class
A.class_foo(1)

# can be used for alternative constructor
A.factory(2)






