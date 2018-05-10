Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> List=['Laptop','pc','mobile','phone','pen']
>>> type(List)
<class 'list'>
>>> len(List)
5
>>> List[4]
'pen'
>>> List[o:5]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    List[o:5]
NameError: name 'o' is not defined
>>> List[0:5]
['Laptop', 'pc', 'mobile', 'phone', 'pen']
>>> List[0:4:2]
['Laptop', 'mobile']
>>> List[::-1]
['pen', 'phone', 'mobile', 'pc', 'Laptop']
>>> List[2]='Disk'
>>> List
['Laptop', 'pc', 'Disk', 'phone', 'pen']
>>> List=List
>>> 
>>> List=List+['pencil']
>>> List
['Laptop', 'pc', 'Disk', 'phone', 'pen', 'pencil']
>>> 
