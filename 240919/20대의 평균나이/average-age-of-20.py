import sys

t_age = 0
cnt = 0

while True:
    buf = int(sys.stdin.readline())
    if buf < 30:
        t_age += buf
        cnt += 1
    else:
        break

print("{:.2f}".format(t_age/cnt))