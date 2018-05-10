# def sum(x, y):
#     z = x + y
#     print(z)
#
# sum(5, 6)

# x = (1, 2, 3, 4, 5)
# y = [1, 2, 3, 4, 5]
# z = 1, 2, 3, 4, 5
# print(x, y, z, type(x), type(y), type(z))
#
#
# def make_twice(func, arg):
#     return func(func(arg))
#
# def add_five(x):
#     return x + 5
#
# print(make_twice(add_five, 10))
#
#
#
# def	my_pure_function(a, b):
#     c = ( 2 * a ) + ( 2 * b )
#     return c
#
# my_pure_function(5, 10)

# my_list = []
# def my_impure_function(arg):
#     my_list.append(arg)
#
#     my_impure_function(10)
#     print(my_list)


# def make_double(x):
#     return x * 2
# my_marks = [10, 12, 20, 30]
# result = map(make_double, my_marks)
# print(list(result))
#
#
# def my_list(x):
#     return x * 3
# marks = [2, 3, 5, 4]
# result = map(my_list, marks)
# print(list(result))
#
#
# nums = [11, 22, 33, 44, 55]
# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res)

#
# def my_iterable():
#     i = 5
#     while i > 0:
#        yield i
#        i -= 1
#
# for i in my_iterable():
#          print(i)
#
#
# def my_decorator(func):
#     def decorate():
#         print("------------")
#         func()
#         print("------------")
#     return decorate
#
# def print_raw():
#         print("Clear Text")
#
# decorated_function = my_decorator(print_raw)
# decorated_function()
#
#
#
# def my(x):
#     def decorate():
#
#         print("------------")
#         x()
#         print("------------")
#
#     return decorate
#
# def print_raw():
#         print("Touhid")
#
# decorated_function = my(print_raw)
# decorated_function()
#
#
# @my_decorator
# def print_text():
#     print("Hello World")

#
# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col)==8:
#             print("*",end="")
#         else:
#             print(end=" ")
#             print()

#
# for row in range(7):
#     for col in range(5):
#         if col==2 or (row==0 and col !=2):
#             print("*",end="")
#         else:
#             print(end=" ")
#             print()
#
# userInput = int(input("Please input side length of diamond: "))
#
# if userInput > 0:
#     for i in range(userInput):
#         for s in range(userInput -3, -2, -1):
#             print(" ", end="")
#         for j in range(i * 2 -1):
#             print("*", end="")
#         print()
#     for i in range(userInput, -1, -1):
#         for j in range(i * 2 -1):
#             print("*", end="")
#         print()