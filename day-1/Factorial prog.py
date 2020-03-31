num=int(input("Enter a number : "))
if num<0:
    print("The factorial of a number does not exist : ")

elif num==0:
    print("The factorial of the number is 1")

else:
    n=1
    for n in range(1, num):

        num=num*(n)
print("The factorial of a number is : ", num)
