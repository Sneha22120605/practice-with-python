#define a function to generate the fibonacci series
def fibonacci(n):
    # base case : the first two numbers in the code are 0 and 1 
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    # recursive case : the next number is the sum of the previous two 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#prompt the user for the number of terms to generate 
num_terms = int(input("Enter the number of terms to generate: "))

#generate and print the fibonaaci series
for i in range(num_terms):
    print(fibonacci(i), end=" ")
