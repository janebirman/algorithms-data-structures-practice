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


def fib_last_digit(n):
    if n<=1:
        return n
    first=0
    second=1

    for _ in range(n-1):
        first,second=second%10, (first+second)%10
    return second


def fib_sum_partial(m,n):
    if m == n:
        return fib_last_digit(m%60)
    else:
        m%=60
        n%=60
        m2=fib_huge(m+1,10)-1
        n2=fib_huge(n+2,10)-1
    return (n2-m2)%10


m,n = map(int, input().split())
print(fib_sum_partial(m,n))
