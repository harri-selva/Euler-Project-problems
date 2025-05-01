import sympy
count = 0
i = 0
while count < 10001:
    i += 1
    if (sympy.isprime(i)) == True:
        count += 1

print(i)
