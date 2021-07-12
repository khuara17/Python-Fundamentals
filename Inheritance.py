###################### Inheritance #####################
'''
Inheritance is the capability of one class to derive or inherit the properties from another class. 

The benefits of inheritance are: 
1. It represents real-world relationships well.
2. It provides reusability of a code. We don’t have to write the same code again and again. 
Also, it allows us to add more features to a class without modifying it.

Syntax:-

class BaseClass:    --- Parent class
    Body of base class

class DerivedClass(BaseClass):   --- Child Class.
    Body of derived class
'''

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        # print (self.roll)
        print(self.age)
        # if self.marks != None:
        #     print(self.marks)

    def setAge(self,age):
        self.age = age
        self.lastName = 'ghg'

    def setMarks(self,marks):
        self.marks = marks

class Student(Person):
    def __init__(self,name,age,rollno) -> None:
        # Person.__init__(self,name,age)
        super().__init__(name,age)
        self.rollno = rollno

    def setAge(self,age):
        self.name = 'as'
        

p1 = Person('Anmol',34)

s1 = Student('messi',3,34)
s1.lastName = 'ronald'
# print(s1.setAge())
# print(s1.rollno)
# p1.display()

# class School()

print(issubclass(Student,Person))







































######################### Different forms of Inheritance ##################'

'''
Base Cases:-

class A():
    pass
class B():
    pass

1. Single inheritance:- 

When a child class inherits from only one parent class, it is called single inheritance.

Example:    
    class c(A):
        pass

2. Multiple inheritance:- 

When a child class inherits from multiple parent classes, it is called multiple inheritance. 


Example:    
    class c(A,B):
        pass

3. Multilevel inheritance: 

When we have a child and grandchild relationship. 

Example:    
    class c(B):
        pass

    class B(A):
        pass


4.  Hybrid inheritance: 

This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.    

Example:    
    class c(B,D):
        pass

    class B(A):
        pass
'''



















##################Question 1 ######################

# class Dog:
#     def walk(self):
#          return "*walking*"

#     def speak(self):
#          return "Woof!"

# class Bulldog(Dog):
#     def speak(self):
#          return "Arff!"

# bobo = Bulldog()
# bobo.speak()





###################### Question 2 ##################33

# class Dog:
#     def walk(self):
#         return "*walking*"

#     def speak(self):
#         return "Woof!"

# class Bulldog(Dog):
#     def speak(self):
#         return super().speak()

# bobo = Bulldog()
# bobo.speak()







##################### Question 3 ###################33

