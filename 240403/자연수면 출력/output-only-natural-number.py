import sys

a, b = map(int, sys.stdin.readline().split())

if a > 0:
    for i in range(b):
        print(a, end='')