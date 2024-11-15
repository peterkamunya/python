def gcdnumber(a,b):
    if b==0:
        return a
    else: 
        return gcdnumber(b,a%b)
num1 =int(input("Enter the fist number:"))
num2 =int(input("Enter the second number:"))
    
    
    
print(gcdnumber(num1,num2))
