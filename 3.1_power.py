   

def perfect_s(x):
    r = 0
    while x > 1 and x & 1 == 0:
        x >>= 1
        r += 1
    return r

def answer(n):
    steps = 0
    n = long(n)
    if n<1:
        return 0
    while n > 1:
        if n == 3:
            n = n - 1
            steps = steps + 1
        elif n %2 == 1:
            b = perfect_s(n+1)
            c = perfect_s(n-1)
            if b > c:
                n = n + 1
            else:
                n = n - 1
            steps = steps + 1
        else:
            n = n/2
            steps = steps + 1

    return steps

