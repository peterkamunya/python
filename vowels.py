9#checking if a word cointain a vowel
def isvowel(word):
    word= word.upper()
    vowels =('A','E','I','O','U')
    for vowel in vowels:
        if vowel not in word:
            return False
        
        return True
    #determining the vowel in word
    word =input("Enter any word of your choice")
    
    if isvowel(word):
        print(word,"cointaining no vowel word")
    else:
        print(word,"does not cointain vowel word in it")
    
    
