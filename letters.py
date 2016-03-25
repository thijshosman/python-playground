class letters (object):

	def __init__(self):
		self.current = 'a'
	def __next__(self):
		if self.current > 'd':
				raise StopIteration
		result = self.current
		self.current = chr(ord(result)+1)
		return result
	def __iter__(self):
		return self

aletters = letters()
aletters.__next__()

counts = [1,2,3]

for item in counts:
	print(item)

i=counts.__iter__()

j=0
try:
	while j<10:
		item = i.next()
		print(item)
except StopIteration:
	pass

