#2.	Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies. 
text =input("Enter a long text in form of a string ")
print("\noriginal word")
print(text)
words = text.split()
print("\nlist words")
print(words)

print("\n the list with its frequency")
frequncy =[words.count(word) for word in words]
print(frequncy)

frequency =dict(zip(words,frequncy))
print("\n the frequency is")
print(frequency)
 




