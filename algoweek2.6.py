#python3

def fib_last_digit(n):
    if n<=1:
        return n
    first=0
    second=1

    for _ in range(n-1):
        first,second=second%10, (first+second)%10
    return second

def fib_sum(n):
    #F[i]=(F[i-1]+F[i-2]) mod 10
    first2=(n+2)%60
    second2=fib_last_digit(first2)
    if second2 ==0:
        return 9
    else:
        return (second2-1)


n = int(input())
print(fib_sum(n))
