result = 0
list1 = []
list2 = []
palindrome = []
for i in range (100, 1000):
    list1.append(i) 
for z in range (100, 1000):
    list2.append(z)
    
for i in list1:
    for z in list2:
        result = i * z
        result = str(result)
        list3 = list(result)
        length = len (list3)
        if length == 6: 
            if list3[0] == list3[5] and list3[1]==list3 S[4] and list3[2]== list3[3]:
                palindrome.append(result)
                  

print(max(palindrome))

