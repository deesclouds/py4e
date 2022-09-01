# write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above
# 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)
# input to read a string and float() to convert the string to a number
# No need to sanitize user data

# exercise 03_01
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input") # shows error to user to fix error 
    quit() # this line stops the code from running 

print(h, r)    
if h > 40 :
  
    standard = r * h
    overtime = (h - 40.0) * (r * 0.5)

    gross_pay = standard + overtime
else:
    gross_pay = h * r
print("Pay:$" ,gross_pay)
