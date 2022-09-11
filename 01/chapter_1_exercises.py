# Exercises:

# 1. Write a program that uses input to prompt a user for their name and then welcomes them.

name = input("Enter your name: ")
print("Hello " + name)

# 2. Write a program to prompt the user for hours and rae per hour to compute gross pay.

hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate "))
pay = hours * rate 
print("Pay: " + str(pay))

#built-in round function helps to properly round the resulting pay to two decimal places

# 3. assume that we execute the following assignment statements.
width = 17
height = 12.0

# For each of the following expressions, write the value of the expression and the type (of the value of the expression).

# 1. width//2 = 8 = int
# 2. width/2.0 = 8.5 = float
# 3. height/3 = 4.0 = float
# 4. 1 + 2 * 5 = 11 = int

# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

celsius = int(input("Enter Temperature in Celsius: "))
fahrenheit = celsius * 9 // 5 + 32
print("This is the temperature in Fahrenheit: " + str(fahrenheit))


# In Python 2.0, this function was named raw_input.
# See https://en.wikipedia.org/wiki/Mnemonic for an extended description of the word "mnemonic".
