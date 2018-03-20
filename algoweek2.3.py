#python3
import sys
#import unittest

def calc_GCD(n,m):
    top = n if (n>=m) else m
    bottom = n if (n<=m) else m

    while bottom != 0:
        remainder = top % bottom
        top = bottom
        bottom = remainder
    return top

n,m = map(int, input().split())
# map(int, input.split())
print(calc_GCD(n,m))
