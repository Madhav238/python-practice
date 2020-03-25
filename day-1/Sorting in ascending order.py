list=[]
num=int(input("Enter how many values you want : "))
print("Enter values")
for k in range(num):
    list.append(int(input()))
print("The unsorted list : ", list )
for j in range (len(list)-1, 0, -1):
        for i in range(j):
            if list[i]>list[i+1]:
                list[i], list[i+1]=list[i+1], list[i]
print("This is the sorted list : ", list)
