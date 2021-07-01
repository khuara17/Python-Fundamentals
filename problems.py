# Write a program to find the maximum element in the list without using inbuilt function

myls = [3,5,6,7,8]
# print(max(myls))
# max=-1


myls.sort()
# print(myls[-1])
# for i in ls:
#     if i>max:
#         max=i
# print(max)

# for i in range(len(myls)):
#     if myls[i] > max:
#         max= myls[i]
# print(max)

# ls = [3,5,6,9,7,8]
# x = 0
# y = 0
# while y < len(ls):
#     if x >= ls[y]:
#         pass
#     else:
#         x = ls[y]
#     y+=1
# print(x)

# Suppose x is defined as follows: 

x = [ 'a','b', 
    {
        'foo': 1,
        'bar': {
                'x' : 10,
                'y' : 20,
                'z' : 30 },
        'baz': 3 },
        'c','d'] 

# Is the following statement True or False? 
#  x[2] = {
#         'foo': 1,
#         'bar': {
#                 'x' : 10,
#                 'y' : 20,
#                 'z' : 30 },
#         'baz': 3 }

# print('z' in x[2])



############### Function#################


'''
Write a function to check  string is palinrome.

palindrome :-  nitin
'''

def palindrome(word):
    temp=word[::-1]
    if temp==word:
        print("IT IS A PALINDROME")
    else:
        print("IT IS NOT A PALINDROME")

# word=input("Enter a string:")
# palindrome(word)

# p=input("Enter a string:")

# def palindrome(p):
#     return p==p[::-1]

# if palindrome(p):
#     print("Palindrome")
# else:
#     print("Not palindrome")



# def palindrome(word):



'''
Write a python program to find and display the product of three positive integer 
values based on the rule mentioned below:

1. It should display the product of the three values except when one of the integer value is 7. 
2. In that case, 7 should not be included in the product and the values to its left also should 
not be included.
3. If there is only one value to be considered, display that value itself. 
4. If no values can be included in the product, display -1.

Note: Assume that if 7 is one of the positive integer values, then it will occur only once. 
Refer the sample I/O given below.

Sample Input    Expected Output

1, 5, 3                 15
3, 7, 8                 8
7, 4, 3                 12
1, 5, 7                 -1

'''
# def find_product(num1,num2,num3,num4):
#     args = []
#     # args = args + [num1,num2,num3]
#     args.extend([num1,num2,num3,num4])
#     product = 1
#     if 7 in args:
#         j = args.index(7)
#         if j is len(args)-1:
#             return -1
#     else:
#         j = -1

#     for i in range(j+1,len(args)):
#         product *= args[i]

#     return product
    # print(args)

def find_product(*args):
    # args = []
    # args = args + [num1,num2,num3]
    # args.extend([num1,num2,num3,num4])
    product = 1
    if 7 in args:
        j = args.index(7)
        if j is len(args)-1:
            return -1
    else:
        j = -1

    for i in range(j+1,len(args)):
        product *= args[i]

    return product
product = find_product(7,1,5,9,2)
print("The result is:",product)
# ls = [1,4,7]
# def find_product(num1,num2,num3):
#     product= 0
#     if (num1 != 7 and num2 != 7 and num3 != 7):
#         product = num1 * num2 * num3
#     elif (num1 == 7):
#         product = num2 * num3
#     elif(num2 == 7):
#         product = num3
#     elif(num3 == 7):
#         product = -1
#     return product

# product=find_product(1,5,7)
# print("The result is:",product)

# def productFunction(ls):
#     if ls[0]==7:
#         print(ls[1]*ls[2])
#     elif ls[1]==7:
#         print(ls[2])
#     elif ls[2]==7:
#         print("-1")
#     else:
#         print(ls[0]*ls[1]*ls[2])

# ls=[]
# print("Enter the 3 numbers:")
# for i in range(3):
#     n=int(input())
#     ls.append(n)

# productFunction(ls)
