#checking the frequency
name = input("Enter along text to be converted to  be a string:  ")
print(name)

words= name.split()
print(words)

frequency =[word.count(word) for word in words]
print(frequency)

frequency = dict(zip(words,frequency))
print(frequency, end=" ")

         
      





    
    

    
 
        
    
    
    
    
    



    
        
    