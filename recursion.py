############ Recursion #################
'''
1.  Recursion means that a function calls itself. 
    This has the benefit of meaning that you can loop through data to reach a result.
2.  should be very careful with recursion as it can be quite easy to slip into  writing a function
    which never terminates, or one that uses excess amounts of  memory or processor power.
3.  Every recursive function must have a base condition that stops the recursion or 
    else the function calls itself infinitely.
4.  However, when written correctly recursion can be a very efficient and mathematically-elegant 
    approach to programming.
5.  The Python interpreter limits the depths of recursion to help avoid infinite recursions,
    resulting in stack overflows.
6.  By default, the maximum depth of recursion is 1000.
    If the limit is crossed, it results in RecursionError.
'''

######## Advantages of Recursion ###########
'''
1. Recursive functions make the code look clean and elegant.
2. A complex task can be broken down into simpler sub-problems using recursion.
3. Sequence generation is easier with recursion than using some nested iteration.
'''
################# Disadvantages of Recursion #########
'''
1. Sometimes the logic behind recursion is hard to follow through.
2 .Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
3 .Recursive functions are hard to debug. '''


############## Examples ###########

def myfunction():
    myfunction()
    return True

# def myfunction2():
#     print(myfunction())

# myfunction()











######  Write a function to display factorial of number ##############

# 6! =  6 * 5 * 4 *   3 * 2 * 1

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))
















######### problem 2 ############

''' Write a function to calaulate sum of first n numbers. 

ex: n = 3 
op == 6  ( 3 + 2 +1 )
'''

def addition(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

# print(addition(3))


# 4 + 3 + 2 + 1
def addition_Rec(n):
    if n == 1:
        return 1
    else:
        return n + addition_Rec(n-1)

# addition_Rec(3)  === 3 + addition_Rec(2)   __3___    <------
#                                                            |
# addition_Rec(2)  === 2 + addition_Rec(1) <-   ===> 3  ------
#                                           |
# addition_Rec(1)  ==== 1    ---------------

# addition_Rec(2)  === 2 + 1 = 3

# addition_Rec(3)  === 3 + 3 = 6



# print(addition_Rec(3))


# |   |
# | 2 + addition_Rec(1)  |
# | 3 + addition_Rec(2)  |
# |___|












######## Problem 3 ########## 

'''Write a program to display first n elements of fibonacci series 

0 1 1 2 3    5 8 13 21 ..................

'''