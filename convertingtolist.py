def reverse_sorted_nums():
    nums = input("enter  6: numbers")
    listed_nums=nums.split()  
    if len(listed_nums) == 6:
        for nums in listed_nums:
            if nums<=-10000 and nums >10000:
             listed_nums.sort()
             listed_nums.reverse()
            for i in listed_nums:
                print(i ,end=" ")
         
    while len(listed_nums) != 6:
        nums = input("Enter exact 6 numbers:")
        listed_nums =nums.split()
        if len(listed_nums) == 6:
            listed_nums.sort()
            listed_nums.reverse()
            for i in listed_nums:
                print(i ,end=" ")
            
            
reverse_sorted_nums()

    
    
    

    
    
    
    
 
   
    
    
            


    

