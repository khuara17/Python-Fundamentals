########## Function Defination (Function Declaration) ###########

def myfunction(x,y=5):
    '''
    This function does addition operation
    '''
    # print(x + y)
    print("Hi")
    # return x + y

t,v = 4,5 
######## Function Call ########
# myfunction(t) # When function is returning nothing
# x = myfunction(t,v) # When function is returning Some values
# print(x)
############### DocString ########
# print(myfunction.__doc__)


############ Calculator #############


# Input(Consider Datatypes) --> Logic --> Output Formatting

# 2 + 3 

# Input :- 2 Operands(Int,Float) and 1 Operator 
# Output :- Int , Float


############ Input ##################

# x = int(input("Enter The first Number: "))
# y = int(input("Enter the second number: "))
# z = input("Enter the operator: ")
# print(type(x))

######## Logic Part ###########
def calculator(a,b,c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a * b
    elif c == '/':
        return a/b
    else:
        return "Wrong Operator entered..."

# res = calculator(x,y,z)

########## Output #######

# print(f"Output of Operaion is: {res}. ")



############# Problem 1 ################
''' Write a function that stutters a word as if someone is struggling to read it. 
The first two letters are repeated twice with an ellipsis ... and space after each, and 
then the word is pronounced with a question mark ?.

Examples
stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"

Notes
Assume all input is in lower case and at least two characters long. '''

# word = input("Enter the word: ")

def stutter(word):
#    res = 
   return f"{word[:2]}... {word[:2]}... {word}?" 

# res = stutter(word)
# print(res)

# MyStore = 

########## Passing list or other datatype as an input ############

ls = [2,3,4,5]
MyTuple = (3,4,0)

def MyFunction(mylist,mytuple):
    for i in mylist:
        print(i)

# MyFunction(ls,MyTuple)

################# Problem 2 ################

'''In this challenge, a farmer is asking you to tell him how many legs can be counted among all his 
animals.
The farmer breeds three species:
chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species.
 You have to implement a function that returns the total number of legs of all the animals.
(chickens,cows,pigs)
Examples
animals(2, 3, 5) ➞ 36
animals(1, 2, 3) ➞ 22
animals(5, 2, 8) ➞ 50
'''

# def animals(chicken,cows,pigs):
#     ## Code
#     return No_of_legs
# def animals(chickens,cows,pigs):
#     legs=chickens*2+cows*4+pigs*4
#     return legs

# chickens=int(input("Enter no of chickens:"))
# cows=int(input("Enter no of cows:"))
# pigs=int(input("Enter no of pigs:"))
# print(animals(chickens,cows,pigs))

# chicleg=2
# cowleg=4
# pigleg=4
# print("Enter the no of chickens:")
# chic=int(input())
# print("Enter the no of cows:")
# cow=int(input())
# print("Enter the no of pigs:")
# pig=int(input())

# def animals(chic,cow,pig):
#     return chicleg*chic+cowleg*cow+pigleg*pig
# print("The total number of legs:",animals(chic,cow,pig))

# def animals(chickens,cows,pigs):
#     legs = chickens*2+cows*4+pigs*4
#     return legs

# chickens=int(input("Enter no of chickens:"))
# cows=int(input("Enter no of cows:"))
# pigs=int(input("Enter no of pigs:"))
# print(animals(chickens,cows,pigs))


# 4 + 16 + 20

###################### Problem 3 ##############

'''

ARS Gems Store sells different varieties of gems to its customers.

Write a Python program to calculate the bill amount to be paid by a customer 

based on the list of gems and quantity purchased.

Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount.
 
 If any gem required by the customer is not available in the store, 
 
 then consider total bill amount to be -1.

Assume that quantity required by the customer for any gem will always be greater than 0.

Perform case-sensitive comparison wherever applicable.

'''
# discount amount = total amount - (total amout * (discount/100))

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    for i in reqd_gems:
        if i in gems_list:
            i1 = gems_list.index(i)
            i2 = reqd_gems.index(i)
            bill_amount = bill_amount + (price_list[i1]*reqd_quantity[i2])
            print("Before",bill_amount)
            if bill_amount > 30000:
                bill_amount = bill_amount - (bill_amount * (5/100))
            print("After disc.",bill_amount)
        else:
            return -1

    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

# bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
# print(bill_amount)

# 2119*3 + 1760 * 10 + 12* 3999


######## Scope (Local and Global Variables) ###########
# global : y = 40, x = 90
# local :  

# y = 40
# x = 90
# y = 00

def myfunction():
    global y 
    y = 30
    # def myinsidefunction():
        # z = 20
        # print(x) 
    # myinsidefunction()
    
    # x = x + y
    print(y)

myfunction()
print(y)
# print(x)