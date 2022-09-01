- [Who should learn Python?](#who-should-learn-python)
- [Where are your programs stored when they are running?](#where-are-your-programs-stored-when-they-are-running)
- [PY4E Chapter 2](#py4e-chapter-2)
- [Why Program?](#why-program)
    - [We learn why one might want to learn to program, and look at the basic issues with learning to program.](#we-learn-why-one-might-want-to-learn-to-program-and-look-at-the-basic-issues-with-learning-to-program)
- [Chapter 1: Introduction](#chapter-1-introduction)
  - [Computer Hardware Architecture](#computer-hardware-architecture)
  - [Understanding **programming**](#understanding-programming)
  - [Words and sentences](#words-and-sentences)
  - [Conversing with Python](#conversing-with-python)
  - [Terminology: Interpreter and compiler](#terminology-interpreter-and-compiler)
- [What is an interpreter?](#what-is-an-interpreter)
- [What is a variable?](#what-is-a-variable)
- [What is a compiler?](#what-is-a-compiler)
- [Writing a program](#writing-a-program)
- [What is a program?](#what-is-a-program)
- [The building blocks of programs](#the-building-blocks-of-programs)
- [What could possibly go wrong?](#what-could-possibly-go-wrong)
- [Debugging](#debugging)
- [Glossary](#glossary)
  - [Exercises:](#exercises)


## FreeCodeCamp Questions 

# Who should learn Python?
Everyone

# Where are your programs stored when they are running?
Harddrive


# PY4E Chapter 2
# Why Program?

### We learn why one might want to learn to program, and look at the basic issues with learning to program.

Why program 
What happens when the CPU cooler is removed?
Inside of Hard Drive
Writing 'hello world' in the Autograder.

# Chapter 1: Introduction

## Computer Hardware Architecture

- CPU: Central Processing Unit: the part that is obsessed with 'what's next'? 3.0 Ghz = 3billion times per sec cpu will ask "What's next?"

- Main Memory: store information that the CPU needs quick. It's nearly as fast as the CPU. Info stored here is temporary. 

- Secondary Memory: used to store info much slower than main memory. The advantage of the second memory can store info wehn there's no power to the computer. (disk drives, usb, mp3s)

- Input & Output Devices: peripherials. How we interact w/ computer

- Network Connection: retrieve info over a network. Very slow place to store & retrieve data thats not always 'up'. Network is slower & unreliable form of Secondary Memory. 

- Internet: a wire where we send and receive data.

As a programer, my job is to use & orchestrate each of these resources to solve a problem and analyze the data from the solution. Mostly will be working with the CPU and telling it what to do next. Sometimes will tell the CPU to use the main memory, secondary memory, network or peripherals.

## Understanding **programming**
- know the language: spell words and construct well-formed sentences
- tell a story: combine words and sentences to convey an idea to the reader
    - theres a skill in constructing the story, and skill in story writing is improved by doing some writing and getting some feedback. 

## Words and sentences

**Reserved words** - cannot be used to name variables
- and
- as
- assert
- break
- class
- continue
- def
- del
- elif
- else
- except
- finally
- for
- from
- global
- if
- import
- in 
- is
- lambda
- nonlocal
- not
- or
- pass
- raise
- return
- try
- while
- with
- yield

print('Hello world!'): 
The print statement is telling Python to speak.

## Conversing with Python

Python interpreter is where you can start execusting in interactive mode.
The >>> prompt is the interpreter asking "What do you want me to do next?"
The way to say good-bye to python is quit()

## Terminology: Interpreter and compiler

Python is a high-level language straighforward for humans to read and write and for computers to read and process. Other high-level languages are:
- Java
- C++
- PHP
- Ruby
- Basic
- Perl
- Javascript
- many more.

The CPU understands machine language: 0's and 1's.

Machine language is tied to the computer hardware, machine language is not protable across different types of hardware. Programs written in high-level languages can be moved between different computers by using a different interpreter on the new machine or recompiling the code to create a machine language version of the program for the new machine. 

Programming language translators are:
- interpreters
- compilers

# What is an interpreter?

Interpreter reads the source code of the program written by the programmer, parses the source code and interprets the instructions on the fly. 

# What is a variable?

A label we use to refer to data stored in memory.

# What is a compiler?

Needs the entire program in a file, then runs a process to translate the high-level source code into machine language and then the compiler puts the resulting machine language into a file for later execution. 

The python interpreter is written in a high-level language called 'C'.
Python is a program itself and is compiled into machine code. 

# Writing a program

- What is a script?
a list of Python instructions saved into a file (.py)
to execute the script, python needs the name of the file.

`$ cat hello.py
print('Hello world!')
 $ python hello.py
Hello world!`

The '$' what we call bling is the operating system prompt. 
the cat hello.py is showing us that the fie "hello.py" has a one-line Python program to print a string
We call Python interpreter and tell it to read its source code from the file 'hello.py' instead of prompting us for lines of Python code interactively. 
Theres no need to quit at the end of the Python program since python is reading your source code and it knows to stop when it reaches the end of the file. 

# What is a program?

 A program is a sequence of Python statements thats crafted to do something. 

 A program to find the most common words in a text file. 

 `
 name = input('Enter file:')
 handle = open(name, 'r')
 counts = dict()

 for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
    bigword = word
    bigcount = count

print(bigword, bigcount)
 `

 # The building blocks of programs

 - **Input**: get data from the 'outside world' - reading a file, sensor, microphone, gps. user inputs, etc.
 - **Output**: display results of the program on screen or store them in a file or write to a device like a speaker to play music or speak text.
 - **Sequential execution**: performs statements one after another in the order encountered in the script.
 - **Conditional execution**: checks for certain conditions then executes or skips a sequence of statements.
 - **Repeated execution**: performs some set of statements repeatedly, usually with some variation.
 - **Reuse**: writes a set of instructions once and gives them a name and then reuse those instructions as needed throughout your program. 

 # What could possibly go wrong?
 - **Syntax errors**: easiest to fix 
 means grammar issue. Python does its best to point right at the line but issue could be earlier in the program.
 - **Logic errors**: good syntax but theres a mistake in the order of statements or how the statements relate to one another. 
 - **Semantic errors**: steps are syntactically perfect and in the right order, but there is a mistake in the program. The program is perfectly correct but doesnt do what's intended. 

# Debugging
 is the process of finding the cause of the error in your code. 
 - reading: examine your code, read it back to yourself and check that is says what you meant to say
 - running: experiment by making changes and running different versions. often if you display the right thing at the right place in the program, the problem becomes obviousm but sometimes you have to spend some time building scaffolding
 - ruminating: take some time to think! That kind of error is it? syntax, runtime, semantic? What information can you get from the error messages, or from the output of the program? What kind of error could cause the problem you're seeing? What did you change last, befor the problem appeared?
 - retreating: at some point, the best thing to do is back off, undoing recent changes, until you get back to a program that works and that oyu understand. The rebuild.

# Glossary

bug:
An error in a program.

central processing unit:
The heart of any computer. It is what runs the software that we write; also called “CPU” or “the processor”.

compile:
To translate a program written in a high-level language into a low-level language all at once, in preparation for later execution.

high-level language:
A programming language like Python that is designed to be easy for humans to read and write.

interactive mode:
A way of using the Python interpreter by typing commands and expressions at the prompt.

interpret:
To execute a program in a high-level language by translating it one line at a time.

low-level language:
A programming language that is designed to be easy for a computer to execute; also called “machine code” or “assembly language”.

machine code:
The lowest-level language for software, which is the language that is directly executed by the central processing unit (CPU).

main memory:
Stores programs and data. Main memory loses its information when the power is turned off.

parse:
To examine a program and analyze the syntactic structure.

portability:
A property of a program that can run on more than one kind of computer.

print function:
An instruction that causes the Python interpreter to display a value on the screen.

problem solving:
The process of formulating a problem, finding a solution, and expressing the solution.

program:
A set of instructions that specifies a computation.

prompt:
When a program displays a message and pauses for the user to type some input to the program.

secondary memory:
Stores programs and data and retains its information even when the power is turned off. Generally slower than main memory. Examples of secondary memory include disk drives and flash memory in USB sticks.

semantics:
The meaning of a program.

semantic error:
An error in a program that makes it do something other than what the programmer intended.

source code:
A program in a high-level language.

## Exercises:
1. What is the function of the secondary memory in a computer? c) store information for the long term, even beyond power cycle
2. What is a program? a list of instructions that tells the computer what to do
3. What is the difference between a compiler and an interpreter? a compiler executes script for computer.   interpreter translates program into machine language for the computer to understand
4. Which of the following contains 'machine code'? b) the keyboard 
5. What is wrong with the following code? Has a syntax error. the print statement is misspelled and the string is not wrapped in parentheses
6. Where in the computer is a variable such as 'x' stored after the following python line finishes? x = 123  b) main memory
7. What will the following program print out? b) 44
8. Explain eacg of the following using an example of a human capability:
   1. central processing unit - a toddler asking what's next 
   2. main memory - remembers today forgets when they wake up
   3. secondary memory - long term memory that can be carried to other parts of their life
   4. input device - eating food
   5. output device - singing or using the bathroom 
9. How do you fix a 'syntax error'? by making sure to follow the grammar rules of python 