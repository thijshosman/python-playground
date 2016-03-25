
# demo of coroutines

def match(pattern):
	print 'looking for ' + pattern
	try: 
		while True: 
			s=(yield)
			if pattern in s: 
				print s
	except GeneratorExit:
		print "=== Done ==="

m = match("jabberwock")
# need to start execution by calling next()
m.next()

m.send("the jabberwock with eyes of flage")
m.send("came whiffing through the tulgey wood")
m.send("yes said the jabberwock")
m.send("and burbled as it came")
m.close()

#create pipelines by sending to next coroutine
def read(text, next_coroutine):
	for line in text.split():
		next_coroutine.send(line)
	next_coroutine.close()

text = 'commending spending is offending to people pending lending'

matcher = match('ending')
matcher.next()
read(text,matcher)

# producer uses send(), not (yield)
# filter uses (yield) and then (send) to next step
# consumer uses (yield) but not send()

def match_filter(pattern, next_coroutine):
	'''just looks for a pattern in the incoming strings and sends the matching strings on to the next coroutine'''
	print 'looking for ' + pattern

	try:
		while True: 
			s = (yield)
			if pattern in s: 
				next_coroutine.send(s)
	except GeneratorExit:
		next_coroutine.close()

def print_consumer():
	print 'preparing to print'
	try: 
		while True: 
			line = (yield)
			print line
	except GeneratorExit:
		print "=== Done ==="

printer = print_consumer()
printer.next()

matcher = match_filter('pend', printer)
matcher.next()

read(text,matcher)

# or send directly to printer
#read(text,printer)

def count_letters(next_coroutine):
	try: 
		while True: 
			s = (yield)
			counts = {letter:s.count(letter) for letter in set(s)}
			next_coroutine.send(counts)
	except GeneratorExit as a: 
		next_coroutine.close()

def sum_dictionaries(): 
	total = {}
	try: 
		while True: 
			counts = (yield)
			for letter, count in counts.items():
				total[letter] = count + total.get(letter, 0)
	except GeneratorExit: 
		max_letter = max(total.items(), key = lambda t: t[1])[0]
		print "most frequent letter: " + max_letter


s = sum_dictionaries()
s.next()
c = count_letters(s)
c.next()
read(text,c)

def read_to_many(text, coroutines): 
	for word in text.split():
		for coroutine in coroutines: 
			coroutine.send(word)
	for coroutine in coroutines:
		coroutine.close()

m = match("mend")
m.next()

p = match("pe")
p.next()

colist = [m,p]

read_to_many(text, colist)
#read(text, p)




