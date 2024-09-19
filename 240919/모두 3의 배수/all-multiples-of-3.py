import sys


flag = 1

for _ in range(5):
    if int(sys.stdin.readline()) % 3 != 0:
        flag = 0

print(flag)