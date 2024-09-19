import sys


a, b = map(int, sys.stdin.readline().split())

data = []

for i in range(1, 1920 + 1):
    if (1920 % i == 0) & (2880 % i == 0):
        data.append(i)

flag = 0

for i in data:
    if i > a-1 and i < b+1:
        flag = 1
        break

print(flag)