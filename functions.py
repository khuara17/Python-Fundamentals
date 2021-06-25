########## Function Defination (Function Declaration) ###########

def myfunction(x,y=4): 
    '''
    This function does addition operation
    '''
    # print(x + y)
    # print("Hi")
    return x + y

t,v = 4,5 
######## Function Call ########
# myfunction(t) # When function is returning nothing
x = myfunction(t) # When function is returning Some values
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

MyFunction(ls,MyTuple)

