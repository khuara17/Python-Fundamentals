'''
Write a python program to display all the common characters between two strings. 

Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Sample Input                                Expected output

"I like Python"
"Java is a very popular language"               lieyon
'''

def find_common_characters(msg1,msg2):
    pass #Remove pass and write your logic here

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
# common_characters=find_common_characters(msg1,msg2)
# print(common_characters)




############## Lamda Function ########
'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax :- 

lambda arguments : expression
'''
# def x(a,b):
#     return a+b

x = lambda a,b : a + b

# print(x(5,6))

# y = lambda a,b,c : a * b + c - 6 % 3 

# print(y(2,3,4))

############## Function that doules the passed value #############

def myfunct(n):
    return lambda a : a * n


mytripler = myfunct(3)
mydoubler = myfunct(2)  # lambda a : a * 2
# print(mydoubler)
# m = mydoubler(5)
# print( mydoubler(5) )
# print( mytripler(5) )

################# Min, Max, Sum ##########

# print(min(3,4))
# print(max(3,4))
# x = (2,3,4)
# print(sum(x))


# x = ['ravi','ram','vishal']
# print(min(3,4,5,6))
# print(max(x))

# print(sum(x))

############### Round #############
# 4 4.5 5
# print(round(4.5628,2))
# print(round(4.3678))

############# enumerate ###############

x = ['ravi','ram','vishal',78,7.7]

y = enumerate(x,10)

# print(type(y))

# e,r,t=(3,4,5)

# for i,j in enumerate(x):
#     print(i,j)


############## Eval ##################
a = 4
# print(eval('a+5'))

############ split #########

mytxt = "Naruto is# the best, Anime."

x = mytxt.split('t')

# print(x)


############# Slice ##############

# slice(start,end,steps)

myls = ['a','b','c','d','e','t','i']
# mtls[0:2]
x = slice(1,7,3)

# print(myls[x])


############### Sorted #################
'''
The sorted() function returns a sorted list of the specified iterable object.

You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

Note: You cannot sort a list that contains BOTH string values AND numeric values.
'''

# Syntax
# sorted(iterable, key=key, reverse=reverse)
def example(tup):
    return tup[0]
# a = ("h", "b", "a", "c", "f", "d", "e", "g")
# x = sorted(a, reverse=False)

x = [(2,3),(89,5),(9,0)]
# x = sorted(x, key=lambda tup:tup[0] , reverse=False)
# print(x)

# x.sort()
############### Strip ##############
'''
Remove spaces at the beginning and at the end of the string:

'''
# txt = "     banana     "

# x = txt.strip()

# print("of all fruits", x, "is my favorite")

################### getattr ################3
'''
The getattr() method returns the value of the named attribute of an object.
If not found, it returns the default value provided to the function.'''
'''
The syntax of getattr() method is:
getattr(object, name)


The above syntax is equivalent to:
object.name
'''

class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)
