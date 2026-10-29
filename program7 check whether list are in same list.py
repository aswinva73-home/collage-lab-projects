#for checking the 2 lists length are same or not
list1 = [1, 2, 3, 8]
list2 = [1, 2, 3, 5]

print('The first list is: ' + str(list1))
print('The second list is: ' + str(list2))

l1 = len(list1)
l2 = len(list2)

print("Length of list1:", l1, "and length of list2:", l2)

if l1 == l2:
    print("Lists are the same length")
else:
    print("Lists are not the same length")
