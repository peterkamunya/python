#3.	Write a Python program to find the digits which are absent in a given mobile number.
mobile_number = input("Enter your mobile number to find which numbers are not there:: ")
print(mobile_number)
all_digit = set("0123456789")
print("\n All digit are 0 1 23456789")
present_digit = set(mobile_number)
print("\npresent digit are" + mobile_number)
absent_number = all_digit-present_digit
print("Absent digit are", sorted(absent_number))
present_digit.
