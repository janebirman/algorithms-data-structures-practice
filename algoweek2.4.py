#python3
import sys

def calc_GCD(n,m):
    top = n if (n>=m) else m
    bottom = n if (n<=m) else m

    while bottom != 0:
        remainder = top % bottom
        top = bottom
        bottom = remainder
    return top

def calc_LCM(n,m):
    multiple = n * m
    return (multiple // calc_GCD(n,m))

n,m = map(int, input().split())
print(calc_LCM(n,m))
