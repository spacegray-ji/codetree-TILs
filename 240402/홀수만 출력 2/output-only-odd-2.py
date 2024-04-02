import sys


b, a = map(int, sys.stdin.readline().split())

for i in range(b, a-1, -1):
    if i % 2 != 0:
        print(i, end=' ')