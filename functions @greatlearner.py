'''functions: a function is a reusable block of code that is used tp perform a specific action
@it is mostly a part of a larger piece of code that solves the problem
@using functions will "make your life very easy" in terms of program
it is one part of program

here is how:
code modularization  program organization(optional) increased manageability

"how to define a function in python"
the "def" method is used in python for this
@ any input arguments need to be placed inside the parenthesis while defining function
@ 'the code block within every function:
1.start with a colon {:}
follow indentation

"there are two parts to this "
#DEFINING THE FUNCTION:consists of function name,operation and the parameters
#CALLING THE FUNCTION:process of invoking and /or passing values to the defined function
'''
'''

def first_function():#function definition
    print("hello, dear learners")

first_function #function call
'''
'''
TYPES OF FUNCTION
1.Bulit in function    2.user-defined function

1.bulit in function
.int()
.print()
.list()
.sum()
.there are 68 built in  function in python
'''
'''
def first_function():#function definition
    print("hello, dear learners")

first_function()
hello, dear learner
'''
'''
def greet_function(name):
    print("hey," + name + ". Good afternoon")


greet_function('jyoshna')
hey,jyoshna. Good afternoon
'''
'''
def jyo_function():
    a=10
    print("the value inside the function is:",a)
    print("\n")
a=5
jyo_function()
print(" the value outside of the function is:",a)
print("\n")
'''
#string functions in python
'''
name="jyoshna"
print(len(name))

7
'''
'''
sample_text="jyoshna is a python programmer"
if "manasa" in sample_text:
    print("the keyword is not present")
print("the keyword is present")

the keyword is present

'''
          
#sorting a list
'''
vowels=['i','u','a','o','e']
vowels.sort(reverse=True)
print(vowels)

['u', 'o', 'i', 'e', 'a']
'''
'''
flowers=['rose','lilly']
flowers.append('lotus')
print(flowers)
['rose', 'lilly', 'lotus']
'''
#nested function
'''
def outer_function():
    print("this is the outer function")
    def inner_function():
        print("this is inner function")
    inner_function()
outer_function()
this is the outer function
this is inner function
'''
#lambda function
'''
triple=lambda x: x*3
print(triple(5))

15
'''
'''
x=3
def triple_fun(x):
    return x*3
print(triple_fun(x))

9
'''
#math function
'''
import math
pow(2,3)
'''
#recursion function
'''
def factorial(a):
    if a==1:
        return 1
    else:
        return(a*factorial(a-1))
input_number=5
print(factorial(input_number))

120
'''
'''
def crop_func(z):
    del z[0]
    return z
def print_val():
    a=[1,2,3]
    b=crop_func(a)
    print(b)
    print(a)
print_val()

[2, 3]
[2, 3]

'''
'''
def crop_func(z):
    return z[1:]
def print_val():
    a=[1,2,3]
    b=crop_func(a)
    print(b)
    print(a)
print_val()
[2, 3]
[1, 2, 3]
'''
#boolean function
'''
print(15>10)
print(15==10)
print(15<10)
True
False
False
'''

a="hello"
b=15
c=0
sample_list=[]
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(sample_list))
True
True
False
False
