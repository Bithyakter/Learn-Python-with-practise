Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> from tkinter import *
>>> a=TK()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a=TK()
NameError: name 'TK' is not defined
>>> from tkinter import *
>>> a = tk()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = tk()
NameError: name 'tk' is not defined
>>> from tkinter import *
>>> a = Tk()
>>> a.title ("My First window")
''
>>> 
>>> import tkinter
>>> root = tkinter.Tk()
>>> root.title("My second window")
''
>>> 
