a=20
b=58

if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b
print(a)