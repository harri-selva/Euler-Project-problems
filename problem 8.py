num = int(input("hi?"))
digits = [int(i) for i in str(num)]
maximum = 0
for i in range (0,986):
    result = digits[i] * digits[i+1] * digits[i+2] * digits[i+3] * digits[i+4] * digits[i+5] * digits[i+6] * digits[i+7] * digits[i+8] * digits[i+9] * digits[i+10] * digits[i+11] * digits[i+12]
    if result > maximum:
        maximum = result

print(maximum)
