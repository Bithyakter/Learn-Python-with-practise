# print("Bithy")
#
# #Variable
#
# x=12
# print(x+3)
#
# x= "Hi world..."
# print(x + " I Love Apple")

#user_input = input("Enter your Birth Year: ")
#age = 2018 - int(user_input)
#print ("You are " + str(age) + " years old !")

#inpleis operator

# a=5
# a *= 3
# print(a)
#
# Language = "Python"
# Language += " Java"
#
# print(Language)


#Control_structural


# x = 12
# if x > 5:
#     print("Greater than 5")
#     if x <= 47:
#         print ("Between 6 and 47")
#
#
#
# x = 4
# if x == 5:
#     print("It's 5")
# else:
#     print("It's not 5")
#
#
# num = 7
# if num == 5:
#     print("Number is 5")
# else:
#     if num == 11:
#         print("Number is 11")
#     else:
#         if num == 7:
#             print("Number is 7")
#         else:
#             print("Number isn't 5, 11 or 7")
#
#
# status = 5
# msg = "Logout" if status == 5 else "Login"
# print(msg)
#
# for i in range (12):
#     print(i)
# else:
#     print("Done")

#
# i = 1
# while i <= 20:
#     print (i)
#     i = i + 2
#
#     while 1 == 1:
#         print("In the Loop")
#
#

# i = 1
# while 1 == 1:
#     print(i)
#     i = i+1
#     if i>=5:
#         print("Breaking")
#         break
#
#         print("Finished")


    # i = 0
    # while True:
    #     i = i + 1
    #     if i == 2:
    #         print("Skipping 2")
    #         continue
    #
    #         if i == 5:
    #             print("Breaking")
    #             break
    #         print(i)
    #
    #     print ("Finished")
    #

#LIST

# words = ["Shammi","Nitu","Monisha","!"]
#
# print(words[0])
# print(words[1])
# print(words[2])
# print(words[3])
#
# Number = 1
# My_numbers = [Number,2,3]
#
# things = ["Numbers", 0, My_numbers, 4.56 ]
#
# print(things[0])
# print(things[1])
# print(things[2])
# print(things[2][2])
#
#
# str = "Hello world !"
# print(str[8])
#

# my_numbers = [1,2,4,4,5]
# my_numbers[2] = 3
#
# print (my_numbers)
#
#
# list = [1, 2, 3]
# print (list + [4, 5, 6])
# print (list * 3)
#
# Fruits = ["apple", "orange", "pineappe", "grape"]
# print("orange" in Fruits)
# print("rice" in Fruits)
# print("apple" not in Fruits)

# num = [1, 2, 3, 4]
# num.append(5)
# print(num)
#
#
# words = ["A", "C"]
# index = 1
# words.insert(index, "B")
# print(words)
#
# letters = ['p', 'q', 'r', 's', 'p', 'u']
# print(letters.index('r'))
# print(letters.index('p'))
# print(letters.index('z'))

###note = help(list.METHOD_NAME)
  ###dir(list)

# nums = [1, 2, 4, 20, 50, 3, 4]
# max(nums)
#
#
# my_numbers = list(range(10))
#
# print(my_numbers)


# fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# # Lets make juice with these fruits
# start_index = 0
# max_index = len(fruits) - 1
# while start_index <= max_index: # Work until this condition is True
#     fruit = fruits[start_index]
# print(fruit + " Juice!")
# start_index = start_index + 1

#
# fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# # Lets make juice with these fruits
# for fruit in fruits:
#     print(fruit + " Juice!")


# #for letter in 'Python':
#     #print(letter)
#
# for letter in 'Trisha' + ' Touhid':
#
#    print (letter)


# for i in range(20):
#     if i == 5:
#         continue
#         if i > 9:
#             break
#         print(i)
#     print ("Printed first 10 numbers except 5!")

#
# def my_func(x=None):
#     if x:
#         return x * x
#     else:
#         return 0

# print(my_func())
# print(my_func(5))

#"Dictionary"

# my_marks = {"Bengali": 80, "English": 85, "Math": 90}
# print(my_marks ["Math"])
#
# my_marks = {"Bengali" : [30, 35, 32], "English" : [45, 52, 33], "Math": [60, 74, 58]}
# print(my_marks["Math"])


# my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : "What?"}
# my_nums[4] = 16
# print(my_nums)

#"Tuple"

# permissions = (("Admin", "Operator", "Customer"), ("Developer", "Tester"), [1, 2, 3], {
#     "Stage": "Development"})
# print(permissions[3]["Stage"])


##....Function

# def hello():
#    print("Hello World !")


# def show_double(x):
#     print(x*2)
#
# show_double(2)
# show_double(100)
#
#
# def make_sum(x,y):
#    z = x+y
#    print(z)
#
# make_sum(5,10)
# make_sum(500,500)
#
# def print_dict(**kwargs):
#    for args in kwargs:
#       print("{0} : {1}". format(args, kwargs[args]))
#
# print_dict(a=1, b=2, c=3)

# def print_all(a, *args, **kwargs):
#    print(a)
#    print(args)
#    print(kwargs)
#
# print_all(10,20,30,50, b=5, c=10)



# def get_larger(x, y):
#    if x > y:
#       return x
#    else:
#       return y
#
# value = get_larger(23, 32)
#
# print(value)


# def larger(x, y):
#
#     if x > y:
#         return x
#     else:
#         return y
#
# value = larger(50, 40)
#
# print(value)


# def beautify(text):
#     return text + '!!!'
#
# def make_line(func, words):
#     return "Hello " + func(words)
#
# print (make_line(beautify, "word"))

#
# import random
#
# value = random.randint(1, 100)
# print(value)







































































































