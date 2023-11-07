import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
c=0
n, m = [int(i) for i in input().split()]
for i in range(n):
    row = input()
    c+=row.count('M')
print(c)
