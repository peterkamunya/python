
data =[10,20,30,20,30,40,50,50,10,60,70,45,55,55]

def duplicate_list(duplist):
    noduplicate = []
    for element in duplist:
        if element not in noduplicate:
            noduplicate.append(element)
            
    return  noduplicate
print(duplicate_list(data))
    