def isRecursivePalindrome(s, low, high):
    if(low==high):
        # For mid point
        return True
    
    if(s[low]!=s[high]):
        # unequal   
        return False
        
    if(low<=high):      
        return isRecursivePalindrome(s, low+1, high-1)
    
    return True


# initializing string
s = str(input("Enter string:"))
print("The palindrome checked recursively: ",isRecursivePalindrome(s, 0, len(s)-1))





def isIterativelyPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        print(len(str)-i-1)
        if str[i] != str[len(str)-i-1]:
            
            return False
    return True
 
# main function
s = str(input("Enter string:"))
print("The palindrome checked recursively: ",isIterativelyPalindrome(s))
 


