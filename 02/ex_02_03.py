# write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
# You should use input to read a string and float() to convert the string to a number. 
# No need to sanitize user data

# exercise 02_03 
hrs = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
gross_pay = float(hrs * rate)
pay = str(gross_pay)
print("Pay: $" + pay)

