

#num = int (input("Enter the number of rows:"))
#
# num = [5]
# for n in num:
#     for i in range(0,n):
#         for j in range(0,n-i-1):
#              print(end=" ")
#         for j in range(0,i+1):
#              print("*",end=" ")
#         print()


# num = int(input("Enter the number of rows:"))
# for i in range(0, num):
#     for j in range(0, num - i - 1):
#         print(end=" ")
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print()



for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row + col==8):
         print("*", end=" ")
        else:
            print(end=" ")
    print()