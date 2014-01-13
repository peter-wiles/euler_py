import itertools

def fib():
    yield 1
    yield 2
    a = 1
    b = 2
    while True:
        nxt = a+b
        a = b
        b = nxt
        yield b

def even_fib():
    return (x for x in fib() if x%2 == 0)

def limit(lim, g):
    return itertools.takewhile(lambda x: x<= lim, g)

print(sum(limit(4000000, even_fib())))

