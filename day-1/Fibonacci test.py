def isperfectsquare(x):
    s=int(x**(1/2))
    return s*s==x
def isfibonacci(n):
    return isperfectsquare(5*n*n+4) or isperfectsquare(5*n*n-4)
for i in range(1, 50):
    if(isfibonacci(i)==True):
        print("It is a Fibonacci number : ", i)
    else:
        print("It is not a Fibonacci number : ", i)
