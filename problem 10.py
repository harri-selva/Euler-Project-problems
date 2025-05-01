import sympy
counter = 0
prime = 0
while counter < 2000000:
    counter +=1
    if sympy.isprime(counter) == True:
        prime += counter

print(prime)
