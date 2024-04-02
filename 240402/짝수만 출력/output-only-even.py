import sys


a, b = map(int, sys.stdin.readline().split())

for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end=' ')