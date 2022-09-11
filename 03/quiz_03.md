# Chapter 3 Quiz

1. Which Python keyword indicates the start of a function definition?
- def

2. In Python, how do you indicate the end of the block of code that makes up the function?
- We de-indent a line of code to the same indent level as the def keyword

3. In Python what is the input() feature best described as?
- a built-in function

4. What does the following code print out?
def thing():
      print('Hello')
  print('There')

- prints There

5. In the following Python code, which of the following is an "argument" to a function?

x = 'banana'
y = max(x)
print(y)

- x

6. What will the following Python code print out?

def func(x):
    print(x)
func(10)
func(20)

- 1020

7. Which line of the following Python program will never execute?

def stuff():
    print('Hello')
    return
    print('World')
stuff()

- print('World')

8. What will the following Python program print out?

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('fr'), 'Michael')

- Bonjour Michael

9. What is the most important benefit of writing your own functions?

- Avoiding writing the same non-trivial code more than once in your program