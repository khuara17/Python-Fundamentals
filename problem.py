'''question 1'''
'''Create a function that takes a number as its parameter and returns another function. The returned function must take a list of numbers as its parameter, and return a list of the numbers divided by the number that was passed into the first function.
Examples
first = factory(15)
# returns a function first.

lst = [30, 45, 60]—sub_factory
# 30 / 15 = 2, 45 / 15 = 3, 60 / 15 = 4

first(lst) ➞ [2, 3, 4]'''

lst=[]
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele)
print(lst)

def factory(n):
    def sub_factory(lst):
        return [i//n for i in lst]
    return sub_factory

x= factory(n)
print(x(lst))


'''question 2'''
'''Create a function that takes a list of dictionaries like [{ "name": "John", "notes": [3, 5, 4]}, { "name": "Mich", "notes": [1, 3, 5]}] and 
returns a list of dictionaries like [{ "name": "John", "top_note": 5 }, {"name": "Mich", "top_note": 5}].
If a student has no notes (an empty list), return top_note: 0.'''

def get_name_and_top_note(students):
    for s in students:
        s['top_note'] = max(s['notes'] + [0])
        s.pop('notes')
    return students
x=[{ "name": "John", "notes": [2, 4, 5]}, { "name": "Mich", "notes": [1, 3, 5]}]
print(get_name_and_top_note(x))


'''question 3'''
'''Create a function that multiplies two matrices (n x n each).
Examples
matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]'''

def matrix_mult(m1, m2):
    [[e, f],[g, h]], [[a, b], [c, d]] = m1, m2
    return [[a*e + c*f, b*e + d*f], [a*g + c*h, b*g + d*h]]
x=matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]])
print(x)


'''question 4'''
'''Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).
Examples
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions

char_at_pos("EDABIT", "odd") ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions'''

def char_at_pos(r, s):
    lst = []
    for i in range(len(r)):
        if s == 'even':
            lst.append(r[i+1::2])
        elif s == 'odd':
            lst.append(r[i::2])
    return lst[0]

print(char_at_pos([2,4,6],"even"))

'''if you are taking string then print() will be  print(char_at_pos("PYTHON","even"))'''









