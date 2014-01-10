def primes_upto(n):
	x = list(range(n+1))
	x[1] = 0
	for i in range(0,n+1):
		if x[i] == 0:  continue
		for j in range(2*i,n+1,i):
			x[j] = 0
	return list(filter(lambda y:y>0,x))
	
print(primes_upto(500000)[10000])
