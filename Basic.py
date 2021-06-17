###### Keywords ##########

# is = 8


######## Operators ###########
# x = 8
# 5 + 8
# c = 6 * 4 + 6 - x

''' Arithmatic Operator '''
a = 7
b = 5
# Operator :- + , - , * , / , ** , // , %   :- Binary Operators.

# print(a**2**3)    #7^2  --- 49 ** 3
# print(a//b)  ## 5/2 = 2.5 == 2 
# print(a % b)  # 7 % 5 = 2 ,  10 % 5 = 0 , 12 % 5 = 2

## x = 3.4  Floor : 3 , ciel = 4

############# Assignment operators ########

x = 6 
x += 4 # x = x +4 = 6+4 = 10
# print(x)

# 1 2 4 8 16 32 64..........


# 64 32 16 8 4 2 1
# 1 + 1 = 10, 1+ 1+1 =11
# 0 + 0 = 0,
# 101             =   4 +  0 + 1 =   5  =   4 + 1   = 101
# |
# 111              = 4 + 2 + 1 = 7
# ----
# 111 = 7     

a = 4    ==  100 
# Right Shift  101 = 010 =   001 = 0+ 0 + 1 = 1

#Left Shift   101   # = 010 = 100 = 4    =    101000
a <<= 1  #  1010
# print(a)  


####### Comparison Operators ######## 

## Comparison Operators :- == , < , > , <= , >= 

a = 4

# print(a == 4)
# print(a!= 4)

# print(a > 6)   # 4 > 6 = False
# print(a < 6)   # 4 < 6 = True , 4 < 4 = False
# print(a <= 4)  # 4<= 4 = True
# print(a >= 4)  # 4 >= 4 = True

############# Logical Operators ######

# Logical Operators :  and
# True = 1 and False = 0 

# 4 < 5 and 5 > 6 =  False  ## If either one of the condition is false the output will be False else True
# 4 < 5 or 5 > 6 =  True   ## Either one of the condtion shoud be true.
# 
print(not(4 < 5 or 5 > 6))