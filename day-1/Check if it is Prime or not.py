def my_func(a):
    for i in range(2,a):
        if (a%i)==0:
                print("The given number is not a prime : ")
                break
    else:
        print("The given number is Prime : ")
my_func(5)
my_func(2)
my_func(10)
