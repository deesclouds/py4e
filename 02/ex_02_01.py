# write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above
# 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)
# input to read a string and float() to convert the string to a number
# No need to saniztize user data

# exercise 03_01
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
# print(h, r)
if h > 40 :
    # print("Overtime Hours")
    standard = r * h
    overtime = (h - 40.0) * (r * 0.5)
    # print(standard plus overtime)
    gross_pay = standard + overtime
else:
    # print("Standard Hours")
    gross_pay = h * r
print("Pay:$" ,gross_pay)
