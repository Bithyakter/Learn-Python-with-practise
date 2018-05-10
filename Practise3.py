Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: D:/Programming Tutorial/Python/p.3.py ===============
>>> 
=============== RESTART: D:/Programming Tutorial/Python/p.3.py ===============
>>> 
>>> if a<0:
	    print('a negative')
else:
	print('a not negative')

	
a not negative
>>> i=1
>>> while i<=10:
	    print i
	    
SyntaxError: Missing parentheses in call to 'print'
>>> i=1
>>> while i<=10:
	    print ('i')
	    i=i+1

	    
i
i
i
i
i
i
i
i
i
i
>>> i=1
>>> while i<=10:
	    print(' i ')
	    i= i+1

	    
 i 
 i 
 i 
 i 
 i 
 i 
 i 
 i 
 i 
 i 
>>> i = 1
>>> while i<=10:
	    print('i')
	        i = i + 1
	        
SyntaxError: unexpected indent
>>> i=1
>>> while i<=10:
	    print('i')
	    i=i+1

	    
i
i
i
i
i
i
i
i
i
i
>>> fib_1=0
>>> fib_2=1
>>> while fib_2<20:
	    print('fib_2')
	    fib_1,fib_2=fib_2,fib_1+fib_2

	    
fib_2
fib_2
fib_2
fib_2
fib_2
fib_2
fib_2
>>> i=1
>>> while i<=10:
	    print('i')
	    i = i + 1

	    
i
i
i
i
i
i
i
i
i
i
>>> i=1
>>> while i<=10:
	    print ('i')
	    i+=1

	    
i
i
i
i
i
i
i
i
i
i
>>> i=1
>>> while i<=10:
	    print(i)
	    i=i+1

	    
1
2
3
4
5
6
7
8
9
10
>>> fib_1=0
>>> fib_2=1
>>> while fib_2<20:
	    print (fib_2)
	    fib_1,fib_2=fib_2,fib_1+fib_2

	    
1
1
2
3
5
8
13
>>> while fib_2<20:
	    print (fib_2)
	    fib_1, fib_2 = fib_2, fib_1+fib_2

	    
>>> 
>>> 
>>> fib_1,fib_2=0,1
>>> while fib_2<20:
	    print (fib_2)
	    fib_1, fib_2 =fib_2, fib_1+fib_2

	    
1
1
2
3
5
8
13
>>> while fib_2<20:
	    print(fib_2),
	    fib_1,fib_2=fib_2,fib_1+fib_2

	    
>>> 
>>> fib1,fib2=0,1
>>> while fib2<20:
	    print(fib2),
	    fib1,fib2=fib2,fib1+fib2

	    
1
(None,)
1
(None,)
2
(None,)
3
(None,)
5
(None,)
8
(None,)
13
(None,)
>>> fib_1,fib_2=0,1
>>> while fib_2<20:
	    print(fib_2),
	    fib_1,fib_2=fib_2,fib_1+fib_2

	    
1
(None,)
1
(None,)
2
(None,)
3
(None,)
5
(None,)
8
(None,)
13
(None,)
>>> fib_1=0
>>> fib_2=1
>>> while fib_2<20:
	    print fib_2,
	    
SyntaxError: Missing parentheses in call to 'print'
>>> fib_1=0
>>> fib_2=1
>>> while fib_2<20:
	    print(' fib_2'),
	    fib_1,fib_2=fib_2,fib_1+fib_2

	    
 fib_2
(None,)
 fib_2
(None,)
 fib_2
(None,)
 fib_2
(None,)
 fib_2
(None,)
 fib_2
(None,)
 fib_2
(None,)
>>> fib_1=0
>>> fib_2=1
>>> while fib_2<20:
	    print (fib_2) ,
	    fib_1,fib_2=fib_2,fib_1+fib_2

	    
1
(None,)
1
(None,)
2
(None,)
3
(None,)
5
(None,)
8
(None,)
13
(None,)
>>> fib_1=0
>>> fib_2=1
>>> while fib_2<20:
	    print(fib_2,)
	    fib_1,fib_2=fib_2,fib_1+fib_2

	    
1
1
2
3
5
8
13
>>> fib1,fib2=0,1
>>> while fib2<20:
	    print(fib2,)
	    fib1,fib2=fib2,fib1+fib2

	    
1
1
2
3
5
8
13
>>> fib1,fib2=0,1
>>> while fib2<20:
	    print (fib2),
	    fib1,fib2=fib2,fib1+fib2

	    
1
(None,)
1
(None,)
2
(None,)
3
(None,)
5
(None,)
8
(None,)
13
(None,)
>>> for i in range(10):
	    print(i)

	    
0
1
2
3
4
5
6
7
8
9
>>> for i in range(50,2):
	    print(i)

	    
>>> 
>>> for i in range(50):
	    print(i)

	    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
>>> for i in range(10):
	    print(i)
	    if i>5:
		    break

		
0
1
2
3
4
5
6
>>> stack=[]
>>> 
>>> stack.append (2)
>>> stack.append (3)
>>> stack.append (5)
>>> 
>>> stack.pop()
5
>>> 
>>> 
