import sys

n = int(sys.stdin.readline())

cnt1 = 1
cnt2 = 1

while n//cnt1 > 1:
    n = n//cnt1
    cnt1 += 1
    cnt2 += 1


print(cnt2)