import sys


a, b = map(int, sys.stdin.readline().split())


cnt = 0
for i in range(a, b+1):
    if i % 6 == 0 and i % 8 != 0:
        cnt += i

print(cnt)