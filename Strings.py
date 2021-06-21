##### Multingle Strings #########

mystring = ''' this is my first program
 I love programming 
 I love python ''' 

m = "I love python" 

# print(m[7])

##### len()   ########
 
# x = len(m)
# print(x)

######### String Slicing ###########

# If accessing single index and out of range :- error
# If accessing range(slicing) and out of range :- It will go till last index and stop.
p = "banana"

x = p[1:8]

# print(x)

######## String Formatting #######

# Method 1
age = 28
friendage = 24
myage = "My age is {} and my friend age is {}".format(12,34)
# x = myage.

# print(myage)


# Method 2
quantity = 3
itemno = 567
price = 49.95
# myorder = "I want to pay {1} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price)) 

# Method 3

# x = 

# print(f"I want to pay {'mystr****'} dollars for {itemno} pieces of item {price}")

###### Functions for string ###############

a = "hello world!"

print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("o","P"))
print(a.split("o"))
print(a.capitalize())
print(a.count('l'))
print(a.islower())
