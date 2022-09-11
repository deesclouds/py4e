# Exercise 6

# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    #print("In computepay", hours, rate)  
    if hours > 40 :
    # print("Calculates overtime hours")
        standard = rate * hours
        overtime = (hours - 40.0) * (rate * 0.5)
    # print(standard plus overtime)
        gross_pay = standard + overtime
    else:
    # print("calculates standard hours")
        gross_pay = hours * rate
    #print("Returns", gross_pay)
    return gross_pay

# takes hours and rate from user
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
# print(h, r)

gross_pay = computepay(h, r)

print("Pay:$" ,gross_pay)