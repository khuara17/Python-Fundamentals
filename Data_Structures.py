############ List  ################
'''1. Lists are used to store multiple items in a single variable.
   2. List items are  changeable(Mutable), and allow duplicate values.
   3. List items are indexed, the first item has index [0], the second item has index [1] and so on...
   4. Lists are written with square brackets.
   5. list can have any datatype in it.'''


mylist = [2,'hello',[2,['hi',4.5],4],True,(2,0)]
mylist2 = [0,'world']

# print(len(mylist[2]))

### Removing List items ############

# mylist.remove([2,['hi',4.5],4])
# mylist.pop()   ## Deletes the last element from list 
# del mylist
# mylist.clear()

# print(mylist)

##### Change the element of the list

# mylist[0] = 45
# mylist[1:3] = [90,'hello']
# mylist[1:4] = [90] # 1 = 90 , 2: [4,5]
# print(mylist)

# mylist.insert(2,'string')

####### Accessing Elements of list #######
# print(mylist[-2])
# print(mylist[6][1][1])  # = 4.5


###### Adding an element ######
# mylist.append(8)
# mylist.extend(mylist2)

# print(mylist)
# print(mylist2)


########### Tuple ##################
''' 1. Tuples are used to store multiple items in a single variable.
    2. Tuple items are unchangeable(Immutable), and allow duplicate values.
    3. Tuples are written with round brackets. '''

mytuple = (2,  2, 3.4,3.4,   'tuple',  True,  [2,3]  ,  ('hi',6.7) )

# print(mytuple[0:4])

# mytuple.append(2)

# mylist4 =  [2,  2, 3.4,   'tuple',  True,  [2,3]  ,  ('hi',6.7) ]

# mylist4[3][2] = 'v'

# print(mylist4)

######## Unpacking ############
# mytuple = (2,3,4)

(first,*second,third) = mytuple
# print(first,second,third)

###### Type Conversion ###############

# x = int(2.3)

# mylist3 = list(mytuple)
# mylist3.append(80)
# mytuple = tuple(mylist3)


# print(mytuple)

# mytuple = (3.4,2,  2, 3.4,3.4,   'tuple',  True ,  ('hi',6.7) )
# mylist =  [3.4,2,  2, 3.4,3.4,   'tuple',  True ,  ('hi',6.7) ]
# myset = set(mylist)
# mylist = tuple(myset)
# print(mylist)




########### Set ##################
''' 1. Set items are unchangeable(Immutable), and do not allow duplicate values.
    2. Sets are written with curly brackets.. '''

myset = { 2, 2, 3.4,   'tuple',  True ,  ('hi',6.7)}
myset2  =  { 8,9}
# myset[2] = 4
# print(myset)


########### Add items to the set  ##########

# myset.add('newvalue')
# myset.update(myset2)
# print(myset)

###### Remove Item from the set ######

# myset.remove(8)
myset.discard(8)
myset.pop()
# del myset
# print(myset)

########### Dictonary ############
''' 1. Dictionaries are used to store data values in key:value pairs.
    2. A dictionary is a collection which is changeable(mutable) and does not allow duplicate Keys.
    3. Dictionaries are written with curly brackets, and have keys and values.
    4. For keys we can have only non-iterable data types
    5. For values we can have any data type. '''

# mylist[1] = [3,4]

# int , x= 6
# c = [3,4,5]

# rollno = {
#     1: 'ramesh',
#     2 : 'sita'
# }

# store = {
#     'soap' : 30,
#     'rice' : 50
# }

# mydict = {
#     1 : 'hello',
#     'hello' : 4,
#     3.4 : [2,3,[4,5],(2,3)],
#     'key' : True,
#     'key' : 4
# }

########## Accessing an element of dict ############
# mydict[3.4]  = 
# temp = [2,3,[4,5]]

# print(mydict[3.4][3][0]) 

######## Updating valuess ##########
# mydict[3.4][3][1] = [3,4]
# mydict.update({'keyss':False})

###### Adding an item to dict #####

# mydict[7] = 85
# print(mydict)

############# Removing an item from dict #######

mydict = {
    1 : 'hello',
    'hello' : 4,
    3.4 : [2,3,[4,5],(2,3)],
    'key' : True,
    'key' : 4
}

# mydict.pop('hello')
# mydict.popitem()
# del mydict
# mydict.clear()
# print(len(mydict))

######### Special Methods ########

# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())
# for i in mydict.items():
#     m,n = i
#     print(m,n)


############### Applying Loops on data stuctures #############

ls = [2,3,'hello','naruto']

# print(ls)
sum = 0
# for i in mydict.values():
#     print(i)

# while i in ls:
#     print(i)

# Write a program to find the maximum element in the list without using inbuilt function

myls = [3,5,6,7,8]
print(max(myls))
max=-1
# for i in ls:
#     if i>max:
#         max=i
# print(max)

for i in range(len(myls)):
    if myls[i] > max:
        max= myls[i]
print(max)

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