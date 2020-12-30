# TypeConversion from decimal with base 10
# to hexadecimal form with base 16
# to binary form with the base 2

# Taking input from user an integer with base 10
number = int(input("Enter a number with base 10\n"))

print("Hexadecimal form of " + str(number) + " is " + hex(number).lstrip("0x").rstrip("L"))

print("Binary form of " + str(number) + " is " + bin(number).lstrip("0b").rstrip("L"))
