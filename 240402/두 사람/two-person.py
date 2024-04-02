import sys

hum1 = sys.stdin.readline().split()
hum2 = sys.stdin.readline().split()

if (int(hum1[0]) > 18 and hum1[1] == 'M') or (int(hum2[0]) > 18 and hum2[1] == 'M'):
    print(1)
else:
    print(0)