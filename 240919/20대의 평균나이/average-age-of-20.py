import sys

age = []

while True:
    buf = int(sys.stdin.readline())
    if buf < 30:
        age.append(buf)
    else:
        break

print("{:.2f}".format(sum(age)/len(age)))