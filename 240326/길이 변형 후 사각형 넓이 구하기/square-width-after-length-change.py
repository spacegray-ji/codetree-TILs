import sys

a, b = map(int, sys.stdin.readline().split('-'))

a = a + 8
b = b * 3

print(a)
print(b)
print(a*b)