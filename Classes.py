'''Syntax'''
# class ClassName:
#     Body

# class point:
#     '''This is a Doctstring for my class'''
#     x = 4
#     y = 5

# class Graph:


# x = point() #x == Object of class , point() == Class Initialization.
# print(x.__doc__)
# x.y

# def __str___

# Variable :- Local Variables
# Attributes  :- We define these with self.
class Person:
    def __init__(self,age,gender):
        self.personAge = age
        # print("I got executed first")
        # age = 45
    # print("I am after init..")    
    age = 56
    # name = 'Dhruv'

    def greet(self,name):
        print("Good afternoon Student....")

person1 = Person(34,'Male')

person1.age = 5
person1.personAge = 45

# print(person1.age)
# print(person1.personAge)
# print(person1.greet('rohit'))


class Myclass:
    def __init__(self,ls,dict,floatv):
        self.ls = ls
        self.dict = dict
        self.flt = floatv
        y = 30

    x = 60
    def newfunct(self):
        print(self.ls)
        # print(x)
        # print(y)

    
        
    # print(self.ls)


ls = [2,34,4]
dict = {
    2:4,
    4:'hi'
}
x = 4.5
# myobj = Myclass(ls,dict,x)
# myobj2 = Myclass([2,3],dict,7.8)
# myobj.newfunct()
# myobj2.newfunct()
# del myobj
# print(myobj.flt)

################ Example one ##############

# 3 + 5i
# 3 + 5j

class ComplexNumber:
    def __init__(self,real,img) -> None:
        self.real = real
        self.img = img  
        # print(real)     

    def CreateComplex(self) -> str:
        return f"{self.real} + {self.img}j"

# first = ComplexNumber(4,5)
# second = ComplexNumber(70,6)
# print(second.CreateComplex()) 


######### Problem 1 ################

'''
Create a class names Mobile

Take Input as brand name, price and ram

create a function with name WillItWork in the class that will tell whether phone can be used for gaming
ram less than 3 gb -- It wont work
ram is between 3 to 4 -- It will work fine
ram is greater than 4 --  It will Work perfectly.
'''
# class Mobile:
#     def WillItWork

class Mobile:
    def __init__(self,brand,price,ram):
        self.brand=brand
        self.price=price
        self.ram=ram
        
    def WillItWork(self):
        # x = 5
        if self.ram<3:
            return 'It wont work'
        elif self.ram>=3 and self.ram<4:
            return 'It will work fine'
        else:
            return 'It will work perfectly'

Iphone = Mobile('Apple',50000,5)
print(type(Iphone))
# print(Iphone.WillItWork())
############## Everything in python is an object of a class ############
x = 'hello'
print(type(x))


