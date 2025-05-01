total = 0
total1 = 0
for i in range (1,101):
    total += i **2

for i in range (1,101):
    total1 += i

total1 = total1**2

difference = total1 - total
print(difference)
