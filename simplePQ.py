from abc import ABCMeta, abstractmethod

class simplepq(object):
	'''a simple implementation of a priority queue'''
	def __init__(self):
		'''constructor, creates queue'''
		# we start at index 1, index 0 is unsed
		pq = [0]



	def insert(self, element):
		'''inserts element in queue'''
		pq.append(element)

		# number of element is length of pq -1 since we started at 1
		self.swim(len(pq)-1)

	def max(self):
		'''removes the maximum'''
		
		# take the maximum
		m = pq[1]

		# set first element to last element
		exch(1,len(pq)-1)
		
		# remove last element
		pq.pop()

		self.sink(1)
		return m

	def sink(self, k):
		while 2*k <= len(pq)-1:
			j = 2*k
			if j < len(pq)-1 less()
				j=j+1
			if 


	def swim(self, k):
		while k > 1 & self.less(k/2, k):
			self.exch(k/2,k)
			k=k/2

	def isempty(self):
		return N==0

		#@staticmethod
	def exch(self,i,j):
		'''exchange w array elements'''
		self.pq[i],self.pq[j] = self.pq[j], self.pq[i]

	def less(self,i,j):
		'''compare 2 array elements, return true if i < j'''
		return pq[i]<pq[j]


aPQ = simplepq()

a = [2,3,1,5,4,6]

for element in a:
	aPQ.insert(element)

while !aPQ.isempty():
	print aPQ.max()


