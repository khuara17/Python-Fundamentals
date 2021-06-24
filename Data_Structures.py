############ List  ################
'''1. Lists are used to store multiple items in a single variable.
   2. List items are  changeable(Mutable), and allow duplicate values.
   3. List items are indexed, the first item has index [0], the second item has index [1] and so on...
   4. Lists are written with square brackets.
   5. list can have any datatype in it.'''

   ############# List Methods ###############
'''
     Method	    Description

    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list
'''

############## Special Methods #############

mylist2 = [5,2,80,0,2.4]
mylist3 = ['v','p','hello','hi']
# x = mylist2.copy()
# print(mylist2.count(0))
# print(mylist2.index(0))
# mylist2.reverse()
# print(mylist2[::-1])
mylist3.sort(reverse=True)
# print(mylist3)
############ Defination ##########

mylist = [2,'hello',[2,['hi',4.5],4],True,(2,0)]

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


'''

Method	        Description
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
'''

mytuple = (2,  2, 3.4,3.4,   'tuple',  True,  [2,3]  ,  ('hi',6.7) )

# print(mytuple[0:4])

# mytuple.append(2)

# mylist4 =  [2,  2, 3.4,   'tuple',  True,  [2,3]  ,  ('hi',6.7) ]

# mylist4[3][2] = 'v'

# print(mylist4)

######## Unpacking ############
# mytuple = (2,3,4,5)

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
''' 1. Set items are unchangeable(Immutable), and do not allow duplicate values and unordered.
    2. Sets are written with curly brackets.. '''


'''
Method	        Description
add()	    Adds an element to the set
clear()	    Removes all the elements from the set
copy()	    Returns a copy of the set
discard()	Remove the specified item
pop()	    Removes an element from the set
remove()	Removes the specified element
update()	Update the set with the union of this set and others
'''
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


'''
Method	            Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''

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

mydict = {
    1 : 'hello',
    'hello' : 4,
    3.4 : [2,3,[4,5],(2,3)],
    'key' : True,
    'key' : 4,
    'dict' : {
        1 : 'word',
        2 : {
            3 : 'foo'
        }
    }
}
# print(mydict['dict'][2])
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
# x = ('key1','key2','key3')
# y = (0,0,0)
# mydict = dict.fromkeys(x,y)
mylist = [2,3,4]
# for i in mylist:
#     print(mydict[i])
print(mydict.get(2))


############### Applying Loops on data stuctures #############

ls = [2,3,'hello','naruto']

# print(ls)
sum = 0
# for i in mydict.values():
#     print(i)

# while i in ls:
#     print(i)