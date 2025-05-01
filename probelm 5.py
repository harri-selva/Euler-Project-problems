counter = 0
found = False
while found == False:
    counter += 1
    i = 1
    total = 0
    while counter % i == 0 and i <= 20:
        i += 1
        total += 1
        if total == 20:
            num = counter
            found = True
        
print(num)
