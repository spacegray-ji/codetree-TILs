lst = [i for i=int(input()) in range(5)]

cnt = 0

for j in lst:
    if j%2 == 0:
        cnt += 1

print(cnt)