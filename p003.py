def prime_factors(n):
    f = 2
    while n > 1:
        while n % f == 0:
            yield f
            n = n / f
        f += 1

print(max(set(prime_factors(600851475143))))

