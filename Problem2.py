########## P1. Wite a function that wil get a no as input and return the multiplication table of the number ###########
# 4 * 1 = 4
# 4 * 2 = 8

def mult_table(n, x):
    for i in range(1, x+1):
        print(n, '*', i, '=', n*i)

# n=int(input("Enter a positive integer: "))
# mult_table(n, 10)

########### P2 ##########
'''
Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4
'''
s = "Celebration"
vwls = 'aeiou'
def count_vowels(string):
    c = 0
    string = string.lower()
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            c += 1
    print("Number of vowels present in the word: ", c)

# count_vowels(s)

########### P3 ##########
'''
Create a function that takes a string (will be a person's first and last name) and 
returns a string with the first and last name swapped.

Examples
name_shuffle("Donald Trump") ➞ "Trump Donald"

name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"

name_shuffle("Seymour Butts") ➞ "Butts Seymour"

Notes
There will be exactly one space between the first and last name.
'''

# def name_shuffle(mystr):
#     return ' '.join(mystr.split(' ')[::-1])

# print(name_shuffle("Donald Trump")) 

def name_shuffle(str1):
    fname=''
    lname=''
    myflag= False
    for i in str1:
        if i == ' ':
            myflag = True
        if myflag == False: 
            lname= lname+i
            # print(lname)
        else:
            fname=fname+i
    print(fname,lname)
# name_shuffle('Donald Trump')

########### P4 ##########

# 55 - 50 = 5
'''
Create a function that takes a list of numbers between 1 and 10 (excluding one number) 
and returns the missing number.

Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7

Notes
The list of numbers will be unsorted (not in order).
Only one number will be missing.
'''
# 1, 2, 3, 4, 6, 7, 8, 9, 10]
# def Missing_no(list):
#     list.sort()
#     i=0
#     while i<10:
#         if list[i]!= list[i+1]-1:
#             return i+2
#         i+=1
#     return 'false'
# print(Missing_no([10, 5, 1, 2, 4, 6, 8, 3, 9]))

def missing_num(ls):
    total = 55
    print(total - sum(ls))

missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])

############# P5 ##########
'''
Create a function that takes a list of non-negative integers and strings and return a new list 
without the strings.

Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]

Notes
Zero is a non-negative integer.
The given list only has integers and strings.
Numbers in the list should not repeat.
The original order must be maintained.
'''


################ P6 ####################
'''
Write a function that takes a string, breaks it up and returns it with vowels first, consonants second.
For any character that's not a vowel (like special characters or spaces), treat them like consonants.

Examples
split("abcde") ➞ "aebcd"

split("Hello!") ➞ "eoHll!"

split("What's the time?") ➞ "aeieWht's th tm?"

Notes
Vowels are a, e, i, o, u.
'''