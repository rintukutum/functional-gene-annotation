def factorial (n):
    f = 1
    while (n >0 ):
        f = f * n
        n = n - 1
    return f
print("Input your number")
n= int(input())
print ("factorial of your input number:", factorial(n))
