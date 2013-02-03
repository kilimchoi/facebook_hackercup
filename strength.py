import itertools
import math
#Result will be a[0]*(n-1)C(k-1) + a[1]*(n-2)C(k-1).. till n=k 
#Here problem is with large numbers, so we use binomial with modulus and reduce the number 
#by computing the remainder at every step, to make sure we avoid handling large numbers
def strength(arr, n, k):
	arr = sorted(arr)
	result = 0
	for i in range(n-1, 0, -1):
		result += arr[i] * binom(i, k-1, 1000000007)
		if result > 1000000007:
			result = result % 1000000007
		if i == (k - 1):
			break
	return result

def binom(n, k, modular):
	numer = 1
	denom = 1
	for i in range(0, k):
		numer = (numer * (n-i)) % modular
	for i in range(1, k+1):
		denom = (denom * i) % modular
	return (numer * mod_inverse(denom, modular)) % modular

def mod_inverse(a, modular):
	return pow(a, modular-2, modular)

 
linestring = open('strength.txt').read()
line_arr = linestring.split('\n')
limit = line_arr[0]
limit = int(limit)
case_num = 1
import itertools as it
items = it.izip(it.islice(line_arr, 1, None, 2), it.islice(line_arr, 2, None, 2))
for line1, line2 in items:
	result = 0
	n, k = line1.split(' ')
	k = int(k)
	n = int(n)
	line2 = line2.split(' ')
	line2 = filter(None, line2)
	arr = [int(i) for i in line2]
	print 'Case #%d: %d' %(case_num, strength(arr, n, k))
	case_num += 1
	limit -= 1
	if limit == 0:
		break


	
