#4.	Write a Python program to print the number of prime numbers which are less than or equal to a given integer.thutisnumber
lower = int(input("Enter a lower number"))
upper =int(input("Enter an upper number"))
prime =True
for num in range(lower,upper+1):
    for j in range(lower,num):
        if num % j == 0:
            prime = False
            break
        else:
            prime = True
    if prime == True:
            print(num )
            
    

         


  
            