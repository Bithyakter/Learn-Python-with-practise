Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Bithy=" T o u h i d "
>>> print(Bithy)
 T o u h i d 
>>> Bithy.upper()
' T O U H I D '
>>> Bithy.lower()
' t o u h i d '
>>> Bithy.strip()
'T o u h i d'
>>> Bithy.rstrip()
' T o u h i d'
>>> Bithy.ltrip()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Bithy.ltrip()
AttributeError: 'str' object has no attribute 'ltrip'
>>> Bithy.lstrip()
'T o u h i d '
>>> Bithy="Touhid"
>>> Bithy2="Shuvo"
>>> Bithy,Bithy2=Bithy2,Bithy
>>> print(Bithy)
Shuvo
>>> printBithy2)
SyntaxError: invalid syntax
>>> print(Bithy2)
Touhid
>>> 
