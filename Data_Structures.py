############ List  ################
'''1. Lists are used to store multiple items in a single variable.
   2. List items are  changeable(Mutable), and allow duplicate values.
   3. List items are indexed, the first item has index [0], the second item has index [1] and so on...
   4. Lists are written with square brackets.
   5. list can have any datatype in it.'''


mylist = [2,'hello',[2,['hi',4.5],4],True]
mylist2 = [0,'world']

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

# mytuple = (2,  2, 3.4,3.4,   'tuple',  True,  [2,3]  ,  ('hi',6.7) )

# print(mytuple[0:4])

# mytuple.append(2)

# mylist4 =  [2,  2, 3.4,   'tuple',  True,  [2,3]  ,  ('hi',6.7) ]

# mylist4[3][2] = 'v'

# print(mylist4)


###### Type Conversion ###############

# x = int(2.3)

# mylist3 = list(mytuple)
# mylist3.append(80)
# mytuple = tuple(mylist3)


# print(mytuple)

mytuple = (3.4,2,  2, 3.4,3.4,   'tuple',  True ,  ('hi',6.7) )
mylist =  [3.4,2,  2, 3.4,3.4,   'tuple',  True ,  ('hi',6.7) ]
myset = set(mylist)
mylist = tuple(myset)
print(mylist)


########### Set ##################
''' 1. Set items are unchangeable(Immutable), and do not allow duplicate values.
    2. Sets are written with curly brackets.. '''

# myset = { 2, 2, 3.4,   'tuple',  True ,  ('hi',6.7)}
# myset[2] = 4
# print(myset)



########### Dictonary ############
''' 1. Dictionaries are used to store data values in key:value pairs.
    2. A dictionary is a collection which is changeable and does not allow duplicates.
    3. Dictionaries are written with curly brackets, and have keys and values. '''