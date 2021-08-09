# '''question 1'''
# '''Create a function that takes a number as its parameter and returns another function. The returned function must take a list of numbers as its parameter, and return a list of the numbers divided by the number that was passed into the first function.
# Examples
# first = factory(15)
# # returns a function first.

# lst = [30, 45, 60]—sub_factory
# # 30 / 15 = 2, 45 / 15 = 3, 60 / 15 = 4

# first(lst) ➞ [2, 3, 4]'''

# lst=[]
# n = int(input("Enter number of elements : "))
 
# for i in range(0, n):
#     ele = int(input())
 
#     lst.append(ele)
# print(lst)

# def factory(n):
#     def sub_factory(lst):
#         return [i//n for i in lst]
#     return sub_factory

# x= factory(n)
# print(x(lst))


# '''question 2'''
# '''Create a function that takes a list of dictionaries like [{ "name": "John", "notes": [3, 5, 4]}, { "name": "Mich", "notes": [1, 3, 5]}] and 
# returns a list of dictionaries like [{ "name": "John", "top_note": 5 }, {"name": "Mich", "top_note": 5}].
# If a student has no notes (an empty list), return top_note: 0.'''

# def get_name_and_top_note(students):
#     for s in students:
#         s['top_note'] = max(s['notes'] + [0])
#         s.pop('notes')
#     return students
# x=[{ "name": "John", "notes": [2, 4, 5]}, { "name": "Mich", "notes": [1, 3, 5]}]
# print(get_name_and_top_note(x))


# '''question 3'''
# '''Create a function that multiplies two matrices (n x n each).
# Examples
# matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]'''

# def matrix_mult(m1, m2):
#     [[e, f],[g, h]], [[a, b], [c, d]] = m1, m2
#     return [[a*e + c*f, b*e + d*f], [a*g + c*h, b*g + d*h]]
# x=matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]])
# print(x)


# '''question 4'''
# '''Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).
# Examples
# char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# # 4 & 8 occupy the 2nd & 4th positions

# char_at_pos("EDABIT", "odd") ➞ "EAI"
# # "E", "A" and "I" occupy the 1st, 3rd and 5th positions'''

# def char_at_pos(r, s):
#     lst = []
#     for i in range(len(r)):
#         if s == 'even':
#             lst.append(r[i+1::2])
#         elif s == 'odd':
#             lst.append(r[i::2])
#     return lst[0]

# print(char_at_pos([2,4,6],"even"))

# '''if you are taking string then print() will be  print(char_at_pos("PYTHON","even"))'''


# '''Create a function that takes a "base number" as an argument. This function should return another function which takes a new argument, and returns the sum of the "base number" and the new argument.
# Please check the examples below for a clearer representation of the behavior expected.
# Examples
# # Calling make_plus_function(5) returns a new function that takes an input,
# # and returns the result when adding 5 to it.

# plus_five = make_plus_function(5)

# plus_five(2) ➞ 7

# plus_five(-8) ➞ -3'''

# '''solution'''

# def make_plus_function(base_num):
#     return lambda x:x+base_num

# x=make_plus_function(7)
# print(x(5))

# '''Create a function that takes a list containing only numbers and return the first element.
# Examples
# get_first_value([1, 2, 3]) ➞ 1

# get_first_value([80, 5, 100]) ➞ 80

# get_first_value([-500, 0, 50]) ➞ -500
# '''
# '''solution'''

# number_list = []
# n = int(input("Enter the list size "))

# print("\n")
# for i in range(0, n):
#     print("Enter number at index", i, )
#     item = int(input())
#     number_list.append(item)
# print("User list is ", number_list)
# def get_first_value(number_list):
#     if not number_list: return None
#     return number_list[0]

# print(get_first_value(number_list))

# '''Create a function that takes length and width and finds the perimeter of a rectangle.
# Examples
# find_perimeter(6, 7) ➞ 26

# find_perimeter(20, 10) ➞ 60

# find_perimeter(2, 9) ➞ 22

# '''
# '''solution'''

# def find_perimeter(length, width):
#     return length * 2 + width * 2
# x= find_perimeter(2,4)
# print(x)


# '''Building a Pie Chart
# A pie chart is a circular graphical representation of a dataset, 
# where each category frequency is represented by a slice (or circular sector) with an amplitude in degrees given by the single frequency percentage over the total of frequencies.
# You can obtain the degrees of sectors following these steps:
# •	Calculate frequencies total.
# •	Calculate percentage of every category frequency dividing it by the frequencies total.
# •	Transform every percentage in degrees multiplying it for 360.
# You are given a dictionary data with keys being the data categories (represented by letters) and values being the data frequencies. 
# Implement a function that returns a map to design a pie chart, like to say the same dictionary with values transformed in degrees instead of frequencies. 
# Round final values to the nearest tenth.
 
# Example
# pie_chart({ "a": 1, "b": 2 }) ➞ { "a": 120, "b": 240 }

# '''


# '''Solution 1'''
# def pie_chart(data):
# 	total = sum(a for b,a in data.items())
# 	for key in data:
# 		data[key] *= 360/total
# 		data[key] = round(data[key],1)
# 	return data
# print(pie_chart({ "a": 1, "b": 2 }))

# '''Solution 2'''
# def pie_chart(data):
# 	total = 0
# 	for item in data:
# 		total+=data[item]
# 	for item in data:
# 		data[item]=round(data[item]*360/total, 1)
# 	return data
# print(pie_chart({  "a": 30, "b": 15, "c": 55  })) 


#################### 
'''A built-in timer inside your car can count the length of your ride in minutes and you have started
 your ride at 00:00.

Given the number of minutes n at the end of the ride, calculate the current time. 02:05
Return the sum of digits that the digital timer in the format hh:mm will show at the end of the ride.

Examples
car_timer(240) ➞ 4
# 240 minutes have passed since 00:00, the current time is 04:00
# Digits sum up is 0 + 4 + 0 + 0 = 4

car_timer(808) ➞ 14

car_timer(14) ➞ 5'''

# x = int(input("Enter the number of minutes: "))
# def car_timer(n):
#     sec = n % 60  # 
#     min = (n-sec)/60
#     temp = 0
#     while sec:
#         temp += sec % 10
#         sec //= 10
#     while min:
#         temp += min % 10
#         min //= 10
#     return temp

# print("Answer: ", car_timer(x))

# print (int(n/60),":",n%60)
# n=int(n/60)*100+n%60
#   tot=int(0)
#   while(n>0):
#     dig=n%10
#     tot=tot+dig
#     n=n//10
#   print(tot)
n = 808

def sum_digit(a):
    temp = 0
    # n%10 
    while a:
        temp += a%10
        a //= 10
    return temp

def car_timer(n):
    hours = n//60  #13.46
    minute = n - (hours*60)  # 808 - 780 = 28
    print(f"{hours}:{minute}")
    # 13:28
    return sum_digit(hours) + sum_digit(minute)


# print(car_timer(n))


