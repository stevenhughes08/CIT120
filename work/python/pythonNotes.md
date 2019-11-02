##Python Notes

>In python everything you create is an object. 

>*Creating a variable* in Python, case matters all variables must be lower case in python. Use Snake case

>first _name = "Ada"
>print(first_name)
>print("These", "will be", "joined together by spaces")


print("Hello Criag")
print(hello Ada)


PS C:\Users\srhug\source\repos\CIT120\work> cd python
PS C:\Users\srhug\source\repos\CIT120\work\python> echo > pythonNotes.md

cmdlet Write-Output at command pipeline position 1
Supply values for the following parameters:
InputObject[0]:
PS C:\Users\srhug\source\repos\CIT120\work\python>
InputObject[0]:
PS C:\Users\srhug\source\repos\CIT120\work\python> pythonLearn.py
pythonLearn.py : The term 'pythonLearn.py' is not recognized as the name of a cm

Suggestion [3,General]: The command pythonLearn.py was not found, but does exist in the current location. Windowsd, instead type: ".\pythonLearn.py". See "get-help about_Command_Precedence" for more details.
PS C:\Users\srhug\source\repos\CIT120\work\python> .\pythonLearn.py
PS C:\Users\srhug\source\repos\CIT120\work\python> .\pythonLearn.py
PS C:\Users\srhug\source\repos\CIT120\work\python>


>>> str (42)
'42'
>>> subject_template = "Thanks for clowning {} with us {}!"
>>> subject_template.format("Python", "Charles")
'Thanks for clowning Python with us Charles!'
>>> "ham" in "hamster"

#A method is a function that is owned by an object. You can access these by using dot notation.

##Booleans
>>Boolians are all tests run by computers. True or False

>>> "ham" in "hamster"
True
>>> bool("")
False
>>> bool(42)
True
>>> Truthy or falsie

#Boolian discicion making


SyntaxError: invalid syntax
>>> is_smoker = True
>>> has_kids = True
>>> has_kids and not is_smoker
False
>>> fruit = "apples"
>>> fruit == "apples"
True
>>> fruit == "apples 
  File "<stdin>", line 1
    fruit == "apples
                   ^
SyntaxError: EOL while scanning string literal
>>> fruit == "apples"
True
>>> fruit == "oranges"
False
>>>






                                                   cd ..


    Directory: C:\Users\srhug\source\repos\CIT120\work


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       10/28/2019  12:00 AM                python
d-----       10/26/2019   8:22 PM                python-Tutorial
d-----       10/29/2019   7:31 PM                unit1


PS C:\Users\srhug\source\repos\CIT120\work> cd unit1
PS C:\Users\srhug\source\repos\CIT120\work\unit1> echo > psudocode1.html

cmdlet Write-Output at command pipeline position 1
Supply values for the following parameters:
InputObject[0]:
Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 01:31:54) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> input ("What is your favorite color?")
What is your favorite color?
''
>>> help str
  File "<stdin>", line 1
    help str
           ^
SyntaxError: invalid syntax
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> ^Z

PS C:\Users\srhug\source\repos\CIT120\work\unit1> python
Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 01:31:54) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quote = "I like cats."
>>> quote.title()
'I Like Cats.'
>>> quote.upper()
'I LIKE CATS.'
>>> quote.lower()
'i like cats.'


##DATA in Python

>Two types:
>1. Numbers
>>>A. Floats in normal speak desmal points
>>>B. int  or integer or whole number
>2. String

##Order of OPERATIONS in PYTHON
>>"PEMDAS - Please Excuse My Dear Aunt Sally"
>>'PEMDAS - Please Excuse My Dear Aunt Sally'
>>>1. Presedence of Multiplication
>>>2. Division
>>>3. Addition 
>>>4. Subtraction


>>> print(_)
I can't...
\even
>>> round(4.6)
5
>>> round(5.2)
5
>>> 10 - 3 * 5 + 8
3
>>> (10 -3) * (5 + 8)
91
>>> "apple" + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> num("11") + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'num' is not defined
>>> int("11")
11
>>> float("11")
11.0
>>> int(11.9)
11
>>> 23 / 3
7.666666666666667
>>> 23 % 3
2
>>>


##Booleans are either true or false. All tests run by computers are either True or false. 

>>Empty booleans are false. 
>>>Truthy > Falsie
>>>>>> bool(42)
True
>>> bool("burrito")
True
>>> bool("")
False

###You can string together booleans and it goes from left to right. 
>>> True and True
True
>>> True and True and True
True
>>> True and True and False
False

>>> True and True and False
False
>>> False or True
True
>>> False or False
False
>>> True or False
True

>>>To return true all both sides to be true. False returns false. 
>>>In the event you have code like this: True or False or False 
>>>><i>The first two booleans become True, because "or" requries either to be True. Then you compare the True or FAlse and follow the same rules!</i>

>>Example think of a dating app. 

###HEDI has kids and she wants to find someone who has kids too, but she hates smoking. 

####What would this code look like?

>>> is_smoker = True
>>> has_kids = True
>>> has_kids and not is_smoker
False

>The above code would not return the man who is a smoker. 

##CONDITIONAL BRACHING



