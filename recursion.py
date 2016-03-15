
# just some recursion files, not all really useful since python does not support tail recursion

#not tail call
def recsum(x):
	print 'recsum called with argument %d' % x
	if x == 1:
  		return x
 	else:
  		y = recsum(x - 1)
  		print 'recsum %d' % y
  		return y + x

#print recsum(5)

#tail call
def tailrecsum(x, running_total=0):
	print 'tailrecsum called with arguments (%d,%d)' % (x,running_total)
	if x == 0:
		return running_total
	else:
		return tailrecsum(x - 1, running_total + x)


#print tailrecsum(5)


# naive fibo
def fibo(n):
	new = 1
	cur = 1
	i=1
	while i<n:
		i+=1
		cur = cur * i
		print cur,i
	return cur

fibo(6)

# recur fibo
def fiborn(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return fiborn(n-1)+fiborn(n-2)

print fiborn(9)

#recur fibo with remembering
table = {}
def fibor(n):
	if n==0 or n == 1:
		return 1
	else:
		if n not in table:
			table[n] = fiborn(n-1)+fiborn(n-2)
			return table[n]
		else:
			return table[n]

print 'fibor: recursive with remembering: %d' % fibor(10)



# recur fibo with lookuptable

def memo1(fn,arg):
	memo = {}
	if arg not in memo:
		memo[arg] = fn(arg)
	print 'memo for arg %d is %d' % (arg,memo[arg])
	return memo[arg]

fibm = memo1(fiborn,9)
print fibm


