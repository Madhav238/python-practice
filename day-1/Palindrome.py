string=str(input("Enter your string: "))
for i in range(len(string)-1):
    if string[::-1]==string:
        print("The following word is Palindrome : ")
        break
else:
    print("The following word is not Palindrome : ")
