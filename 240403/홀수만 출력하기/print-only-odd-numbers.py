n = int(input())

lst = [int(input()) for _ in range(n)]

for i in lst:
    if i % 3 == 0 :
        print(i)