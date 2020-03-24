#!/usr/bin/env python
# coding: utf-8

# In[1]:



a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
sum=a+b
print("The sum of the two given numbers is : " , sum)


# In[27]:


a=float(input("Enter a number:"))
b=float(input("Enter a number:"))
diff=a-b
print("The difference of the two given numbers is : " , diff)


# In[28]:


import math
a=int(input("Enter a number : "))
print("The square root of the given number is : " , math.sqrt(a))


# In[25]:



a=int(input("Enter a number : "))
print("The cube root of a number is : " ,a**(1/3))


# In[29]:


a=int(input("Enter a number : "))
count=float(a)
print(count)


# In[1]:


a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=a*b
print(c)


# In[ ]:


p=int(input("Enter_principal_amount : "))
t=int(input("Enter_time_period : "))
r=int(input("Enter_a_rate_of_interest : "))
result=(p*t*r/100)
print(result)


# In[ ]:


b=int(input("Enter_base_of_the_Triangle")
h=int(input("Enter_height_of_the_Triangle"))
result=(1/2*b*h)
print(result)


# In[ ]:


l=int(input("Enter_length_of_the_Rectangle : "))
b=int(input("Enter_breadth_of_the_Rectangle : "))
result=(l*b)
print(result)


# In[ ]:


r=int(input("Enter_radius_of_the_circle : "))
Area=(3.14*r*r)
print(Area)


# In[ ]:


s=int(input("Enter_side_of_the_Square"))
Area=(s*s)
print(Area)


# In[17]:



i=int(input("Enter a number"))
if i%2==0:
    print("The given number is Even")
else:
    print("The given number is not a even number")


# In[27]:


if num>1:
    num=int(input("Enter a number : "))
for i in range(2, num):
    if (num%i)==0 :
        print("The given number is not a Prime number : ")
        break
else:
    print("The given number is prime : ")


# In[60]:


for n in range(2, 31):
    for j in range(2, n):
        if n%j==0:
            break
    else:
        print(n)
            


# In[61]:


for i in range(2, 30):
    if i%2!=0:
        print(i)


# In[75]:


def add_num(x, y):
    sum=x+y
    return sum
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
print("The sum of the two numbers is : ", add_num(a, b))


# In[76]:


def diff_num(x, y):
    diff=x-y
    return diff
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
print("The difference of two numbers is :  ", diff_num(a, b))


# In[77]:


def square(num):
    return num*num
a=int(input("Enter a number : "))
print("The sqrt of the number is : ", square(a))


# In[78]:


def cube(num):
    return num*num*num
a=int(input("Enter a number : "))
print("The cube of the number is : ", cube(a))


# In[89]:


def my_func(a):
    return (float(a))
print(my_func(5))
print(my_func(3))


# In[93]:


def my_multiplication(a, b):
    return a*b
print(my_multiplication(2, 5))
print(my_multiplication(100, 100))


# In[95]:


def my_func(p, t, r):
    return p*t*r/100
print("The value of simple interest : ", my_func(500, 10, 5))


# In[101]:


def my_Area(b, h):
    return 1/2*b*h
print("The Area of the Triangle is : ", my_Area(100, 50))


# In[103]:


def my_Area(l, b):
    return l*b
print("The Area of the Rectangle is : ", my_Area(50, 10))


# In[111]:


def my_Area(r):
    return 3.14*r*r
print("The Area of the Circle is : ", my_Area(4.0))


# In[112]:


def my_Area(s):
    return s*s
print("The Area of the Square is : ", my_Area(6))


# In[ ]:


def my_func(a):
    if a%2==0:
        print()


# In[ ]:




