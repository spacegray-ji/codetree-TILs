import sys

a, b, c = map(int, sys.stdin.readline().split())

if b > a and b < c:
    print(1)
else:
    print(0)