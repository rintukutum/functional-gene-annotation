def factorial (n):         # Defining a function called factorial with argument n
    f = 1                  # Set a variable f is equals to 1
    while (n >0 ):         # Set a while loop which will be true till input number is grater than zero
        f = f * n          # set f = f * n
        n = n - 1          # Decrease n by 1
    return f               # Returns the value of f to the function whereever it will be called
print("Input your number") # Prints the arguments
n = int(input())           # Takes the input from user convert it to integer and store in to vaiable n
print ("factorial of your input number:", factorial(n)) # Prints the arguments
