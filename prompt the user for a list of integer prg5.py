#check whetehr the numbers are grater then 1oo if is it returns over
x = []
n = int(input("Enter any integer: "))

for i in range(1, n + 1):
    a = int(input("Enter a number: "))
    if a > 100:
        x.append('over')
    else:
        x.append(a)

print("Modified list:", x)

