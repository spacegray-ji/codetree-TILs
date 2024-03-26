import sys

h, w = map(int, sys.stdin.readline().split())

b = int(w/(h/100)**2)

print(b)
if b >24:
    print("Obesity")