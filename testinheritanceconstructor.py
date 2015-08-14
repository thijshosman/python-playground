class A(object):
    def __init__(self,test):
        print "Constructor A was called with %s" % test

class B(A):
    def __init__(self):
        #super(B,self).__init__("test")
        A.__init__(self,"test")
        print "Constructor B was called"

class C(B):
    def __init__(self):
        super(C,self).__init__()
        print "Constructor C was called"

#c = C()

b=B()
