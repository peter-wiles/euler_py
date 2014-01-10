def primes_upto(n):
	p = [x for x in range(n+1)]
	p[1] = 0
	for i in range(0,n+1):
		if p[i] == 0:  continue
		for j in range(2*i,n+1,i):
			p[j] = 0
	return [x for x in p if x > 0]

print(sum(primes_upto(2000000)))