adder = 1
counter = 1
divisors = 0
while divisors < 500:
    divisors = 0
    adder += 1
    counter += adder
    for i in range(1,counter+1):
        if counter % i == 0:
            divisors +=1
        

print(counter)
    
     
