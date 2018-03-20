#python3
def calc_lastfib(n):
    if (n <= 1):
        return n
    first = 0
    second = 1
    for _ in range (n-1):
        first, second = second%10, (first + second)%10

    return second

n = int(input())
print(calc_lastfib(n))
