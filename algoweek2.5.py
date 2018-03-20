#python3
def calc_fib(n):
    if (n <= 1):
        return n
    first = 0
    second = 1
    for _ in range (n-1):
        first, second = second, first + second
    return second

def period(m):
    first = 0
    second = 1
    for i in range(m * m + 1):
        first, second = second, (first + second) % m
        if first == 0 and second == 1:
            return i + 1


def fib_huge(n, m):
    remainder = n % period(m)
    return calc_fib(remainder) % m

n,m = map(int, input().split())
print(fib_huge(n,m))
