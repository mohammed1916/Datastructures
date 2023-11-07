def reverseIteratively(s):
    reversedString = ""
    for i in s:
        reversedString = i + reversedString
    return reversedString




def reverseRecursively(s):
    if len(s) == 0:
        return s
     
    else:
        return reverseRecursively(s[1:]) + s[0]
 
s = str(input("Enter string:"))
print(reverseIteratively(s)) 
print(reverseRecursively(s))