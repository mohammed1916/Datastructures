# Iterative
def factorialIterative(n):
    result = 1
    for i in range(n,1,-1):
        result = result * i
    return result


# Recursive
def factorialRecursive(n):
    result = 0
    if (n == 1):
    # base case: n==1
        result = 1
    #recursive case
    else:
        result = n * factorialRecursive(n - 1)

    return result
    
n = int(input("Enter number:"))
print("Factorial computed Recursively :",factorialRecursive(n))
print("Factorial computed Iteratively:",factorialIterative(n))





