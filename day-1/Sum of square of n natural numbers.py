def squarenumber(n):
    sum=0
    for i in range(1, n+1):
        sum=sum+(i*i)
        return sum
    
print(squarenumber(5))
