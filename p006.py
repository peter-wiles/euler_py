def sq_of_sum(n):
    return sum(range(1, n+1))**2

def sum_of_sq(n):
    return sum(map(lambda x:x**2, range(1, n+1)))

print(sq_of_sum(100)-sum_of_sq(100))
