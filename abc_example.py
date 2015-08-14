
class Base(object):
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return "foo() called"

    # Oh no, we forgot to override `bar()`.
    # def bar(self):
    #     return "bar() called"

from abc import ABCMeta, abstractmethod

class Base1(metaclass=ABCMeta):
	@abstractmethod
	def foo(self):
		pass

	@abstractmethod
	def bar(self):
		pass

class Concrete(Base1):
	def foo(self):
		pass

	# def bar(self):
	# 	pass

    # We forget to declare `bar`() again.

assert issubclass(Concrete, Base1)
c = Concrete()

# need to implement all classes of abstractclass in order to not raise error
# NB: needs python 3
