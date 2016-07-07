def factorial (n):             # Defining a function called factorial with argument n
    if n >=0 :                 # if n is an postive numer or zero go inside if condition
        f = 1                  # Set a variable f is equals to 1
        while ( n > 0 ):       # Set a while loop which will be true till input number is grater than zero
            f = f * n          # set f = f * n
            n = n - 1          # Decrease n by 1
        return f               # Returns the value of f to the function whereever it will be called
    else:                      # if n is negative numer go inside else condition
        i = 1                  # Set a variable i is equals to 1
        j = -n-1               # Set a variable j is equals to -n-1
        a = -1 ** j            #-1 to power j and assign this value to variable a   
        while ( j > 0 ):       # Set a while loop which will be true till input number is grater than zero 
            i = i * j          # multiplication of i and j variable and store the value in to i variable
            j = j - 1          # Decrease j by 1
        return a/i             # Returns the value of a/i to the function whereever it will be called
print("Input your number")     # Prints the arguments
n = int(input())               # Takes the input from user convert it to integer and store in to vaiable n
print ("factorial of your input number:", factorial(n)) # Prints the arguments
