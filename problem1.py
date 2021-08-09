############### Problem 0 (9 Aug) ############33
'''# Write a function TO DO MULTIPLICATION WITOUT USING THE * OPERATOR.
'''
# 4 * 3 = 4 + 4+ 4 or 3+3+3+3
def mul(n1,n2):
    sum=0
    for i in range(n1):
        sum+=n2
    print(sum)

# mul(2,9)
################## Problem 1  ###############
'''
Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples:-
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4

'''
vowels=['a','e','i','o','u','A','E','I','O','U']

def count_vowels(line):
    no=0
    for i in line:
        if i in vowels:
            no+=1
    print(no)

# count_vowels("Prediction")
############## Problem 2 #####################
'''
Create a function that takes three arguments a, b, c and 
returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
'''

def evenly_divisible(x,y,z):
    ans=0
    for i in range(x,y+1):
        if i%z==0:
            ans+=i

    print(ans)

# evenly_divisible(1,10,20)
# evenly_divisible(1, 10, 2)
# evenly_divisible(1, 10, 3)


############## Problem 3 ###############3333

'''
Create a function that returns True if a given inequality expression is correct and False otherwise.

Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
'''

def correct_signs(s):
    print(eval(s))
    # s = s.split()
    # c = 0
    # flag = True

    # for i in s:
    #     if i=='<' or i=='>':
    #         c+=1

    # for i in range(0,c,2):
    #     print(i)
    #     a=s[i]  #3
    #     b=s[i+1] #<
    #     c=s[i+2]  #7
    #     if b=='<':
    #         if a>c:
    #             flag=False
    #             break
    #     if b=='>':
    #         if a<c:
    #             flag=False
    #             break
    # print(flag)      


correct_signs("3 < 7 < 11")
correct_signs("13 > 44 > 33 > 1")
correct_signs("1 < 2 < 6 < 9 > 3")


########### Problem 4 #############3

'''

Create a function that takes a list of non-negative integers and strings and return a new list without the strings.

Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
'''

#############Problem 5 ##################
'''
Write a function that moves all elements of one type to the end of the list.

Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.

move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]

move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
'''
##############Problem 6 ##############3
'''
Create a function that takes a string and returns a string in which each character is repeated once.

Examples:- 
double_char("String") ➞ "SSttrriinngg"

double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"

double_char("1234!_ ") ➞ "11223344!!__  "
Notes
All test cases contain valid strings. Don't worry about spaces, special characters or numbers. They're all considered valid characters.
'''