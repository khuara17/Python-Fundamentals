'''
A university wants to automate their admission process. Students are admitted based on marks scored 
in a qualifying exam.

A student is identified by student id, age and marks in qualifying exam. 

Data are valid, if:
Age is greater than 20
Marks is between 0 and 100 (both inclusive)


A student qualifies for admission, if
Age and marks are valid and Marks is 65 or more


Write a python program to represent the students seeking admission in the university.

The details of student class are given below.

Class name: Student

Attributes :
student_id
marks
age

 
Methods
__init__() :- Create and initialize all instance variables to None

validate_marks():- If data is valid, return true. Else, return false

validate_age() , 


check_qualification() :- 

Validate marks and age.
If valid, check if marks is 65 or more.
    If so return true
    Else return false
Else return false
 

setter methods
Include setter methods for all instance variables to set its values

getter methods
Include getter methods for all instance variables to get its values
'''

class Student:
    def __init__(self,id,marks,age) -> None:
        self.id = id
        self.marks = marks
        self.age = age

    def validate_marks(self):
        if self.marks >= 0 and self.marks <= 100:
            return True
        # else:
        return False
    
    def validate_age(self):
        if self.age > 20:
            return True
        else:
            return False
    
    # 4 > 5
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.marks > 65:
                return True
            else:
                return False
        else:
            return -1    




# s1=Student(2,67,21)
# print(s1.validate_marks())
# print(s1.validate_age())
# print(s1.check_qualification())


# s2 = Student(2,36,28)
# print(s2.validate_marks())
# print(s2.validate_age())
# print(s2.check_qualification())


# id = int(input("Enter Student Id"))
# name = str(input("Enter Student Name"))
# age=int(input("Enter Student age"))
# marks=int(input("Enter Student Marks"))

# class Student:
#  def __init__(self,id,age,name,marks):
#   self.id = id
#   self.age = age
#   self.name = name
#   self.marks = marks

#  def constraints(self,age,marks):
#   if age >= 20:
#    if marks >= 0 & marks <= 100:
#     return "Valid score"
#    else:
#     return "Invalid marks"
#   else:
#    return "Invalid age"

#  def validate_marks(self,marks) -> str:
#   if marks >= 65:
#    return "Student Eligible"
#   else:
#    return "Not eligible"


# s1 =  Student(id,name,age,marks)
# print(s1.constraints(age,marks))
# print(s1.validate_marks(marks))



############ Problem 2 #####################

'''Create a Student class and initialize it with name,age and roll number. 
Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.

Create another class called School, Pass 3 objects of student class and
Create a method RollId and in that Print all the student id from school.

'''

class Student:
    def __init__(self,name,age,roll) -> None:
        self.name = name
        self.age = age
        self.roll = roll

    def display(self):
        print(self.name)
        print (self.roll)
        print(self.age)
        # if self.marks != None:
        #     print(self.marks)

    def setAge(self,age):
        self.age = age

    def setMarks(self,marks):
        self.marks = marks


# s1 = Student('Ria',20,3)
# s1.display()
# s1.setAge(50)
# s1.setMarks(89)
# print("After changing")
# s1.display()
# print(s1.marks)


###################### 

'''
1. Which of the following keywords mark the beginning of the class definition?
CLASS

2.Which of the following statements is most accurate for the declaration x = Circle() ?
x contains a reference to a Circle object.

3.  Which of the following can be used to invoke the __init__ method in B from A, 
    where A is a subclass of B? (Multiple Choice)

super().__init__()  -C
super().__init__(self)
B.__init__()
B.__init__(self)  -C


4. Object and class attributes are accessed using ___ notation in Python.
.

5.  In Python, a function within a class definition is called a:
Method

6.Given the above code snippet, which of the following outputs are correct? (Multiple Choice)



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

-------------- : Options :----
isinstance(jack, Dog)   False

isinstance(miles, Bulldog) False     - C

isinstance(miles, Dog) False

isinstance(buddy, Bulldog) False    -C

isinstance(miles, Dog) False

isinstance(jack, Dachshund)  False    -C


7. Which of the following statements is true?
A class is blueprint for the object

8. What does the __init__() the function do in Python?
This function is called when a new object is instantiated.

9. If you a class is derived from two different classes, it's called ______
Multiple Inheritance

10. An instance of a class.
Object
'''
