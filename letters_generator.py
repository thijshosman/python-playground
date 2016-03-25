def letters_generator():
	current='a'
	while current <= 'd':
		yield current
		current = chr(ord(current)+1)

# chr() gives character corresponding to given number
# ord() gives number of corresponding character

for letter in letters_generator():
	print(letter)

# letters_generator returns a generator
lett = letters_generator()

lett.next() # used to be lett.__next__()

def all_pairs(s):
	for item1 in s:
		for item2 in s:
			yield (item1, item2)

print(list(all_pairs([1,2,3])))


class LetterIterable(object):
	def __iter__(self):
		current = 'a'
		while current <= 'd':
			yield current
			current = chr(ord(current)+1)

letters1 = LetterIterable()

a = all_pairs(letters1)
print(a.next())



