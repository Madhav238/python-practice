num=int(input("Enter a number"))
sum=0
temp=num
while num>0:
    digit=num%10
    sum=sum+digit**3
    num=num//10
    if temp==sum:
        print("The number is Armstrong ")
        break
    
else:
    print("The number is not Armstrong")
        
    
