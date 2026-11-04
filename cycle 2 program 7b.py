list1 = [1, 2, 4, 3, 8]
list2 = [1, 2, 4, 3, 5]

print('The first list is: ' + str(list1))
print('The second list is: ' + str(list2))

sum1 =0
sum2 = 0
for x  in range(len(list1)):
    sum1 = sum1 + list1[x]
print("sum of all element id given list1 :",sum1)
for x in range (0,len(list2)):
    sum2 = sum2 + list2[x]
print("sum of all element id given list2 :",sum2)
if(sum1 == sum2):
    print("list sum of same value")
else:
    print("list are different sum")

