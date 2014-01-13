def evenly_divisible_up_to(n):
    x = n
    while not is_divisible_up_to(n, x): x += n
    return x

def is_divisible_up_to(n, x):
    for i in reversed(range(2, n)):
        if x % i != 0: return False
    return True


print(evenly_divisible_up_to(20))
