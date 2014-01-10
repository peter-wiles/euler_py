def nat(n):
	i = 1
	while i < n:
		yield i
		i+=1

def triplets_with_sum(n):
	return ((a,b,n-(a+b)) 
		for a in range(2,int(n/3)) 
		for b in range(3,int(n/2)) 
		if b>a 
		if n-(a+b)>b)

def is_pythagorean(triplet):
	a,b,c = triplet
	return a**2+b**2==c**2
	
a,b,c = list(filter(is_pythagorean, triplets_with_sum(1000)))[0]
print(a*b*c)