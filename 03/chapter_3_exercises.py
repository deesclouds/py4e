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

# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:


name = input('Please enter your full name: ')
try: 
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input.')
    if hours > 40:
        reg_pay = hours * rate 
        over_pay = (hours - 40.0) * (rate * 0.5)
        gross_pay = reg_pay + over_pay
    else:
        gross_pay = hours * rate
        print('Pay:$' ,gross_pay)

# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table.

#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
# < 0.6      F

try: 
    score = input('Enter score: ')
    score == float or score > 1.0 or score < 0.0
except:
    print('Bad score')
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')
