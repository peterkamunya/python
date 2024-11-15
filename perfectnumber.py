num =int(input("Enter the number"))
result = 0
for i in range (1,num):
    if(num%i)==0:
        result=result+i
if result == num:
    print(num,"is perfect number")
else:
    print(num,"is not a perfecr number")            

        