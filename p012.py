import itertools
from operator import mul
from functools import reduce
from itertools import groupby
import math

def calc_primes_upto(n):
	p = [x for x in range(n+1)]
	p[1] = 0
	for i in range(0,n+1):
		if p[i] == 0:  continue
		for j in range(2*i,n+1,i):
			p[j] = 0
	return [x for x in p if x > 0]

def triangle():
	i = 1
	n = 1
	while True:
		yield n
		i += 1
		n += i

primes = calc_primes_upto(66000)

def prime_factors(n):
	max_factor = int(math.sqrt(n))
	for i in itertools.takewhile(lambda x: x<max_factor, primes):
		while n % i == 0:
			yield i
			n = n / i

def divisors(n):
	p = list(prime_factors(n))
	all = [n]
	for r in range(1,len(p)):
		for c in itertools.combinations(p,r):
			all.append(reduce(mul, c))
	return set(all)
	
def num_divisors(n):
	p = list(prime_factors(n))
	total = 1
	print(p)
	for k,g in groupby(p):
		total *= len(list(g))+1
	return total

t = triangle()
n = next(t)
while len(divisors(n)) < 500: 
	n = next(t)
	
print(n)