Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for /row in range(6):
	for col in range(7):
		if(row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col)==8:
			
SyntaxError: invalid syntax
>>> 
>>> for row in range(6):
	for col in range(7):
		if(row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col)==8:
			print("*",end="")
		else:
			print(end=" ")
			print()
