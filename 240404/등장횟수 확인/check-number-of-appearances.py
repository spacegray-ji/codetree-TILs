lst = [int(input()) for _ in range(5)]

cnt = 0

for j in lst:
    if j%2 == 0:
        cnt += 1

print(cnt)