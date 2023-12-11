def gcdIterative(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcdIterative(b, a % b)
# gcdIterative = lambda a, b: abs(a) if b == 0 else gcdIterative(b, a % b) 
a = 60
b = 48
 
# prints 12
print("The gcd of 60 and 48 calculated recursively is : ", end="")
print(gcdIterative(60, 48))


def gcdIterative(x, y):
    # return max([i for i in range(1, min(x, y) + 1) if x % i == 0 and y % i == 0])
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd
 
a = 60
b = 48
 
# prints 12
print ("The gcd of 60 and 48 calculated iteratively is : ", end="")
print (gcdIterative(60,48))