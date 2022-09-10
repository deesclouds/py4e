# Conditional Execution

## Boolean expressions

A boolean expression is an expression that is either true or false. 
== true when two operands are equal and false if not

True and False are special bool values, they are not strings

the == is the comparison operator

## Comparison operators

x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y
x is y               # x is the same as y
x is not y           # x is not the same as y

A common error is using = instead of ==. 
=                   # assignment operator
==                  # comparison operator (is this equal to)

These two operators do not exist
=< or =>

# Logical operators

and, or, not

and both has to be true or false
or one has to be true or false
not neither true of false

Any nonzero number is interpreted as "True"

## Conditional execution

Writing useful programs, we almost always need to check and change the behavior of the program accordingly. 
Conditional statements gives us this ability. 

The simplest form is the if statement. 
if x > 0 :
    print('x is positive')

The boolean expression after the if statement is called the condition. We end the if statement with a colon ':' and the lines after the if statement are indented.

If the logical condition is true, then the indented statement gets executed. If the logical condition is false, the indented statement is skipped.

if statements have the same structure as function definitions or for loops. 
The statement consists of a header line that ends with the ':' followed by an indented block. 

Statements like this are called compound statements because they stretch across more than one line.

There is no limit on the number of statements that can appear in the body, but there must be at least one. Occasionally, it is useful to have a body with no statements (usually as a place holder for code you haven't written yet.)

In that case we use the pass statement, which does nothing.

if x < 0 :
    pass        #need to handle negative values!

If we enter an if statement in the Python interpreter, the prompt will change from three chevrons to three dots to indicate you are in the middle of a block of statements:

>>> x = 3
>>> if x < 10:
...     print('Small')
...
Small
>>>

When using the Python interpreter, you must leave a blank line at the end of a block, otherwise Python will return an error:
>>> x = 3
>>> if x < 10 :
...     print('Small")
... print('Done')
  File "<stdin>", line 3
    print('Done')
        ^
SyntaxError: invalid syntax

A blank line at the end of a block of statements is not necessary when writing and executing a script, but it may improve readability of your code. 

## Alternative execution

A second form of the if statement is alternative execution, which there are two possibilities and the condition determines which one gets executed. 

if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')

If the remainder when x is divided by 2 is 0, then we know that x is even, and the program displays a message to that effect. If false, the second set of statements are executed. 

If-Then-Else-Logic:

Since the condition must either be true or false, exactly one of the alternatives will be executed. The alternatives are called branches, because they are branches in the flow of execution. 


## Chained conditionals

Sometimes there are more than two possibilities and we need more than two branches. One way to express a computation like that is a chained conditional:

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else: 
    print('x and y are equal')

elif is an abbreviation of else if. Again exactly one branch will be executed.

If-Then-Else-Logic:

Theres no limit to the amount of elif statements. Else has to be at the end but there doesn't have to be one.

if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')

Each condition is checked in order. If the first is false the next is checked. If one is true the corresponding branch executes and the statement ends. Even if more than one condition is true, only the first branch executes.

## Nested conditionals

One conditional can be nested within another.

if x == y :
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

The outer conditional contains two branches. The first branch contains a simple statement. The second branch contains another if statement, which has two branches of its own. Those two branches are both simple statements, although they could have been conditional statements as well.

Nested if statements

Nested conditionals become difficult to read very quickly, Its a good idea to avoid them whe you can.

Logical operators provide a way to simplify nested conditional statements. 
We can rewrite the following code using a single conditional.

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

The print statement is executed only if we make it past both conditionals, so we can get the same effect with the and operator:

if 0 < x and x < 10:
    print('x is a positive single-digit number.')

## Catching exceptions using try and except

>>> prompt = "What is the air velocity of an unladen swallow?\n"
>>> speed = input(prompt)
What is the air velocity of an unladen swallow?
What do you mean, an African or a European swallow?
>>> int(speed)
ValueError: invalid literal for int() with base 10:
>>>

We get a new prompt from the interpreter saying 'oops' and move on to our next statement. 

If we place this code in a Python script and this error occurs, our script immediately stops in its tracks with a traceback. It does not execute the following statement. 

inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

If we execute this code and give it invalid input, it simply fails with an unfriendly error message:

python fahren.py
Enter Fahrenheit Temperature:72
22.22222222222222


python fahren.py
Enter Fahrenheit Temperature:fred
Traceback (most recent call last):
  File "fahren.py", line 2, in <module>
    fahr = float(inp)
ValueError: could not convert string to float: 'fred'

There is a conditional execution structure built into Python to handle these types of expected and unexpected errors called 'try/except'. The idea of try and except is that you know that some sequence of instructions may have a problem and you want to add some statements to be executed if an error occurs. These extra statements (the except block) are ignored if there is no error. 

You can think of the try and except feature in Python as an "insurance policy" on a sequence of statements. 

We can rewrite the temperature converter like this:

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')

Python starts executing the sequence of statements in the try block. If all goes well, it skips the except block and proceeds. If an exception occurs in the try block, Python jumps out the try block and executes the sequence of statements in the except block.

python fahren2.py
Enter Fahrenheit Temperature:72
22.22222222222222

python fahren2.py
Enter Fahrenheit Temperature:fred
Please enter a number

Handling an exception with a try statement is called catching an exception. In this example, the except clause prints an error message. Catching an exception gives you a chance to fix the problem, or try again, or at least end the program gracefully.

## Short-circuit evaluation of logical expressions

When Python is processing a logical expression such as x >= 2 and (x/y) > 2 , it evaluates from left to right. The definition of and, if x is less than 2, the expression x >= 2 is False and the whole expression is False regardless of whether (x/y) > 2 evaluates to True or False.

When Python detects there's nothing to be gained by evaluating the rest of a logical expression, it stops its evaluation and does not do the computations in the rest of the logical expression. When the evaluation of a logical expression stops because the overall value is already know, it is call short-circuiting the evaluation. 

The short-circuit behavior leads to a clever technique called the guardian pattern. 

>>> x = 6
>>> y = 2
>>> x >= 2 and (x/y) > 2
True
>>> x = 1
>>> y = 0
>>> x >= 2 and (x/y) > 2
False
>>> x = 6
>>> y = 0
>>> x >= 2 and (x/y) > 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>

The third calculation failed because Python was evaluating (x/y) and y was zero, which causes a runtime error. But the first and second examples did not fail since the first calculation y was non zero and in the second one the first part of these expressions x >= 2 evaluated to False so (x/y) was never executed due to the short-circuit rule and there was no error. 

We can construct the logical expression to strategically place a guard evaluation just before the evaluation that might cause an error:

>>> x = 1
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x = 6
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x >= 2 and (x/y) > 2 and y != 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>

In the first logical expression, x >= 2 is False so the evaluation stops at the and. In the second logical expression, x >= 2 is True but y != 0 is False so we never reach (x/y)
In the third logical expression, the y != 0 is after the (x/y) calculation so the expression fails with an error. 
In the second expression, we say that y != 0 acts as a guard to insure that we only execute (x/y) if y is non-zero.

## Debugging

The traceback Python displays when an error occurs contains a lot of information, but it can be overwhelming. The most useful parts are usually :
    - what kind of error it was, and
    - where it occurred.

Syntax errors are usually easy to find, but there are a few gotchas. Whitespace errors can be tricky because spaces and tabs are invisible and we are used to ignoring them.

>>> x = 5
>>>  y = 6
  File "<stdin>", line 1
    y = 6
    ^
IndentationError: unexpected indent

In this example, the problem is that the second line is indented by one space. But the error message points to y, which is misleading. In general, error messages indicate where the problem was discovered, but the actual error might be earlier in the code, sometimes on a previous line. 

In general, error messages tell you where the problem was discovered, but that is often not where it is caused. 

