#python3
import sys
n=int(input())
m=[int(x) for x in input().split()]
index1=-1
index2=-1
product = 0
for i in range(n):
    if index1==-1 or m[i]>m[index1]:
        index1=i
for i in range(n):
    if (i != index1 and (index2 == -1 or (m[i]>m[index2]))):
        index2=i

product = m[index1]*m[index2]
print(product)
