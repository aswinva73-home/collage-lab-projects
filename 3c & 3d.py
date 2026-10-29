#vowals cames in a sentence which is given by the user
word = input("Enter a word: ")
vowels = ["a","e","i","o","u"]
list=[]
for x in word:
    if( x in vowels and x not in list):
      list.append(x)
    print("vowel present in the given word is : ",list)


#3d
a= input("Enter a word: ")
for i in range(len(a)):
    print("ascii value is ",a[i],"is",ord(a[i]))
