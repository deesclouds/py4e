# Chapter 3 Exercises

# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hours > 40:
    reg_pay = hours * rate 
    over_pay = (hours - 40.0) * (rate * 0.5)

    gross_pay = reg_pay + over_pay
else:
    gross_pay = hours * rate
print('Pay:$' ,gross_pay)