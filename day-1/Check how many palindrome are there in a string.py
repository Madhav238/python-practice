l=[]
string=str(input("Enter a string : "))
for word in string.split():
    if word[::-1]==word:
        l.append(word)
        print("The number of palindromes",len(l))
        break
    else:
        print("The following word is not Palindrome : ")


