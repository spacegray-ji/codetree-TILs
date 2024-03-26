a = 5
b = 6
c = 7

buf1 = b
buf2 = c

b = a
c = buf1
a = buf2

print(a)
print(b)
print(c)