#python3
def calc_fib(n):
    if (n <= 1):
        return n
    first = 0
    second = 1
    for _ in range (n-1):
        first, second = second, first + second

    return second

n = int(input())
print(calc_fib(n))
