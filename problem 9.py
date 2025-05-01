from math import sqrt

for a in range (1,1000):
    for b in range (1,1000):
        c = sqrt(a**2 + b**2)
        if c % 1 == 0 and a!=b :
            if a + b + c == 1000:
                result = a*b*c

print(result)
