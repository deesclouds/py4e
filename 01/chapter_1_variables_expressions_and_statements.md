# Variables, expressions, and statements

## Values and types

A value is one of the basic things a program works with, like a letter or a number.
Examples: 1, 2, and "Hello, World!"

These values belong to different types:
2 is an integer, "Hello, World!" is a string.

python command starts the interpreter. 
print statement works for integers. 
type command find what type of value something is.

str = string (something surrounded in quotation marks)
int = integer
float = number with decimals (floating point)

a number with commas is not a legal integer in Python but it is still legal

print(1,000,000)
1 0 0 

## Variables

The most powerful feature of a programming language is the ability to manipulate variables. 

A variable is a name that refers to a value.
An assignment statement creates new variables and gives them values:
>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415926535897931

The first assigns a new string to a new variable named message; the second assigns the integer 17 to n; the third assigns the approx value of π to pi.
>>> print(n)
17
>>> print(pi)
3.141592653589793

To display the value we use the print statement. 
To find the type of the variable we use the type command. 
>>> type(message)
<class 'str'>
>>> type(n)
<class 'int'>
>>> type(pi)
<class 'float'>

## Variable names and keywords
Programmers generally choose names for their variables that are meaningful and document what the variable is used for. 

Variable names can be arbitrarily long. They can contain both letters and numbers, but they cannot start with a number. It is legal to use uppercase letter, but it is a good idea to begin variable names with a lowercase letter.

The underscore character can appear in a name. Its often used in names with multiple words, ie. my_name or airspeed_of_unladen_swallow. 

Variable names can start with an underscore character, but we generally avoid doing this unless we are writing library code for others to use. 

If you give a variable an illegal name, you get a syntax error:
>>> 76trombones = 'big parade'
SyntaxError: invalid syntax
>>> more@ = 1000000
SyntaxError: invalid syntax
>>> class = 'Advanced Theoretical Zymurgy'
SyntaxError: invalid syntax

76trombones is illegal because it begins with a number, more@ has an illegal character, class is a reserved word. 

The interpreter uses keywords to recognize the structure of the program, and cannot be used as variable names.

## Python 35 reserved keywords:

and       del       from      None      True
as        elif      global    nonlocal  try
assert    else      if        not       while
break     except    import    or        with
class     False     in        pass      yield
continue  finally   is        raise     async
def       for       lambda    return    await

## Statements

A statement is a unit of code that the Python interpreter can execute. Two kinds of statements: print being an expression statement and assignment. 
Whe a statement is typed in interactive mode, the interpreter executes it and displays the result, if there is one. 

A script usually contains a sequence of statements. If there is more than one statement, the results appear one at a time as the statements execute.

For example, the script

print(1)
x = 2
print(x)

produces the output

1
2

The assignment statement produces no output. 

## Operators and operands

Operators are special symbols that represent mathematical computations. The values the operator is applied to are called operands. 

The operators +, -, *, / and ** perform addition, subtraction, multiplication, division, and exponentiation.

## Expressions

An expression is a combination of values, variables, and operators. A value all by itself is considered an expression, and so is a variable, so the following are all legal expressions (assuming that the variable x has been assigned a value):

17
x
x + 17

If you type an expression in interactive mode, the interpreter evaluates it and displays the result:
>>> 1 + 1
2

But in a script, an expression all by itself doesn't do anything! This is a common source of confusion for beginners. 

The interpreters only displays what has been evaluated and not what has been stored into memory without asking for the interpreter specifically with the print statement. 

## Order of operations

When more than one operator appears in an expression, the order of evaluation depends on the rules of precedence. PEMDAS (parentheses(), exponents(**), multiplication(*), division (//), addition(+), subtraction(-))

## Modulus operator

The modulus operator works on integers and yields the remainder when the first operand is divided by the second. In Python, the modulus operator is a percent sign (%). 

## String operations

The + operator works with strings, but it is not addition in the mathematical sense. It performs concatenation, which means joining the strings by linking them end to end. 

example:
>>> first = 10
>>> second = 15
>>> print(first+second)
25
>>> first = '100'
>>> second = '150'
>>> print(first + second)
100150

The * operator also works with strings by multiplying the content of a string by an integer.

example: 
>>> first = 'Test '
>>> second = 3
>>> print(first * second)
Test Test Test

## Asking the user for input

input is a built-in function that gets input from the keyboard. 
When the function is called, the program stops and waits for the user to type something. When the user presses Return or Enter, the program resumes and input returns what the user typed as a string. 

Before getting input from the user, it is a good idea to print a prompt telling the user what to input. You can pass a string to input to be displayed to the user before pausing for input. 

>>> name = input('What is your name?\n')
What is your name?
Chuck
>>> print(name)
Chuck

The \n at the end of the prompt represents a newline. Thats why the user's input appears below the prompt.

If we need the user to input an integer, you can convert the return value to int using the int() function:

>>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
17
>>> int(speed)
17
>>> int(speed) + 5
22

But if the user types something other than a string of digits, you get an error.

>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
What do you mean, an African or a European swallow?
>>> int(speed)
ValueError: invalid literal for int() with base 10:

## Comments
As programs get bigger and more complicated, they get more difficult to read. Formal languages are dense, and it is often difficult to look at a piece of code and figure out what it is doing, or why.

For this reason, it is a good idea to add notes to your programs to explain in natural language what the program is doing. These notes are called comments, and in Python they start with the # symbol:

Comments can appear on a line by itself, or at the end of a line.
Everything from the # and to the end of the line is ignored and has no effect on the program. 

Comments are most useful when they document non-obvious features of the code. It is reasonable to assume that the reader can figure out what the code does; it is much more useful to explain why. 

This comment is redundant with the code and useless:
v = 5  # assign 5 to v
This comment contains useful information that is not code.
v = 5  # velocity in meter/second. 

Good variable names can reduce the need for comments, but long names can make complex expressions hard to read, so there is a trade-off.

## Choosing mnemonic variable names

As long as following the simple rules of variable naming, avoid reserved words, you have a lot of choice when you name variables. In the beginning, this choice can be both when you read a program and when you write your own programs. 

These programs are identical but very different when read and trying to understand them.

a = 35.0
b = 12.50
c = a * b
print(c)

hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

x1q3z9ahd = 35.0
x1q3z9afd = 12.50
x1q3p9afd = x1q3z9ahd * x1q3z9afd
print(x1q3p9afd)

The Python interpreter sees all three of these programs as exactly the same but humans see and understand these programs quite differently. Humans will most quickly understand the intent of the second program because the programmer has chosen variable names that reflect their intent regarding what data will be stored in each variable.

We call these wisely chosen variable names "mnemonic variable names". The word mnemonic means "memory aid". We choose mnemonic variable names to help us remember why we created the variable in the first place. 

While this all sounds great, and it is a very good idea to use mnemonic variable names, mnemonic variable names can get in the way of a beginning programmer's ability to parse and understand code. This is beacuse beginning programmers have not yet memorized the reserved words and sometimes variables with names that are too descriptive start to look like part of the language and not just well-choosen variable names.

Take a quick look at the following Python sample code which loops through some data. We will cover loops soon, but for now try to just puzzle through what this means:

for word in words:
    print(word)

Whats happening here? Which of the tokens (for, word, in, etc) are reserved words and which are just variable names? Does Python understand at a fundamental level the notion of words? Beginning programmers have trouble seperating what parts of the code must be the same as this example and what parts of the code are simply choices made by the programmer. 

The following code is equivalent to the above code:
for slice in pizza:
    print(slice)

It is easier for the beginning programmer to look at this code and know which parts are reserved words defined by Python and which parts are simply variable names chosen by the programmer. It is pretty clear that Python has no fundamental understanding of pizza and slices and the fact that a pizza consists of a set of one or more slices. 

But if our program is truly about reading data and looking for words in the data, pizza and slice are very un-mnemonic variable names. Choosing them as variable names distracts from the meaning of the program. 

After a pretty short period of time, you will know the most common reserved words and you will start to see the reserved words jumping out at you:
for word in words:
    print(word)

The parts of the code that are defined by Python (for, in, print, and :) and the programmer-choosen variables word and words. 

Many text editors are aware of Python syntax and will color reserved words differently to give you clues to keep you variables and reserved-words seperate. After a while you will begin to read Python and quickly determine what is a variable and what is a reserved word.

## Debugging

The syntax error most likely to make illegal are class and yield, which are keywords or odd~job and US$, which contain illegal characters.

If theres a space in a variable name, Python think its two operands without an operator. 

>>> bad name = 5
SyntaxError: invalid syntax

>>> month = 09
  File "<stdin>", line 1
    month = 09
             ^
SyntaxError: invalid token


For syntax errors the messages don't help much. The most common messages are SyntaxError: invalid syntax and SyntaxError: invalid token, neither of which is very informative.

The runtime error you are most likely to make is a "use before def;" that is trying to use a variable before you have assigned a value, This can happen if you spell a variable name wrong:

>>> principal = 327.68
>>> interest = principle * rate
NameError: name 'principle' is not defined

Variable names are case sensitive, so LaTex is not the same as latex.
At this point, the most likely cause of a semantic error is the order of operations. For example, to evaluate 1/2π, you might be tempted to write:

>>> 1.0 / 2.0 * pi

But the division happens first, so you would get π/2, which is not the same thing!! There is no way for Python to know what you meant to write, so in this case you don't get an error message; you just get the wrong answer. 

