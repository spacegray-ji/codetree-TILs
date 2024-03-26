import sys

a, b = map(int, sys.stdin.readline().split())

buf = a

a = b
b = buf
print(a, b)