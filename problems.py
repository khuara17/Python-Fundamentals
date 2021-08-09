# Write a program to find the maximum element in the list without using inbuilt function

myls = [3,5,6,7,8]
# print(max(myls))
# max=-1


myls.sort()
# print(myls[-1])
# for i in ls:
#     if i>max:
#         max=i
# print(max)

# for i in range(len(myls)):
#     if myls[i] > max:
#         max= myls[i]
# print(max)

# ls = [3,5,6,9,7,8]
# x = 0
# y = 0
# while y < len(ls):
#     if x >= ls[y]:
#         pass
#     else:
#         x = ls[y]
#     y+=1
# print(x)

# Suppose x is defined as follows: 

x = [ 'a','b', 
    {
        'foo': 1,
        'bar': {
                'x' : 10,
                'y' : 20,
                'z' : 30 },
        'baz': 3 },
        'c','d'] 

# Is the following statement True or False? 
#  x[2] = {
#         'foo': 1,
#         'bar': {
#                 'x' : 10,
#                 'y' : 20,
#                 'z' : 30 },
#         'baz': 3 }

# print('z' in x[2])



############### Function#################


'''
Write a function to check  string is palinrome.

palindrome :-  nitin
'''

def palindrome(word):
    temp=word[::-1]
    if temp==word:
        print("IT IS A PALINDROME")
    else:
        print("IT IS NOT A PALINDROME")

# word=input("Enter a string:")
# palindrome(word)

# p=input("Enter a string:")

# def palindrome(p):
#     return p==p[::-1]

# if palindrome(p):
#     print("Palindrome")
# else:
#     print("Not palindrome")



# def palindrome(word):



'''
Write a python program to find and display the product of three positive integer 
values based on the rule mentioned below:

1. It should display the product of the three values except when one of the integer value is 7. 
2. In that case, 7 should not be included in the product and the values to its left also should 
not be included.
3. If there is only one value to be considered, display that value itself. 
4. If no values can be included in the product, display -1.

Note: Assume that if 7 is one of the positive integer values, then it will occur only once. 
Refer the sample I/O given below.

Sample Input    Expected Output

1, 5, 3                 15
3, 7, 8                 8
7, 4, 3                 12
1, 5, 7                 -1

'''
# def find_product(num1,num2,num3,num4):
#     args = []
#     # args = args + [num1,num2,num3]
#     args.extend([num1,num2,num3,num4])
#     product = 1
#     if 7 in args:
#         j = args.index(7)
#         if j is len(args)-1:
#             return -1
#     else:
#         j = -1

#     for i in range(j+1,len(args)):
#         product *= args[i]

#     return product
    # print(args)

def find_product(*args):
    # args = []
    # args = args + [num1,num2,num3]
    # args.extend([num1,num2,num3,num4])
    product = 1
    if 7 in args:
        j = args.index(7)
        if j is len(args)-1:
            return -1
    else:
        j = -1

    for i in range(j+1,len(args)):
        product *= args[i]

    return product
# product = find_product(7,1,5,9,2)
# print("The result is:",product)
# ls = [1,4,7]
# def find_product(num1,num2,num3):
#     product= 0
#     if (num1 != 7 and num2 != 7 and num3 != 7):
#         product = num1 * num2 * num3
#     elif (num1 == 7):
#         product = num2 * num3
#     elif(num2 == 7):
#         product = num3
#     elif(num3 == 7):
#         product = -1
#     return product

# product=find_product(1,5,7)
# print("The result is:",product)

# def productFunction(ls):
#     if ls[0]==7:
#         print(ls[1]*ls[2])
#     elif ls[1]==7:
#         print(ls[2])
#     elif ls[2]==7:
#         print("-1")
#     else:
#         print(ls[0]*ls[1]*ls[2])

# ls=[]
# print("Enter the 3 numbers:")
# for i in range(3):
#     n=int(input())
#     ls.append(n)

# productFunction(ls)

'''
FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.

A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. 
Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.

Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. The delivery charges are as mentioned below:

Distance in kms     Delivery charge in Rs per km

For first 3kms          0

For next 3kms           3

For the remaining       6

Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point,

write a python program to calculate the final bill amount to be paid by a customer. 

The below information must be used to check the validity of the data provided by the customer: 

Type of food must be ‘V’ for vegetarian and ‘N’ for non-vegetarian.

Distance in kms must be greater than 0.

Quantity ordered should be minimum 1.

If any of the input is invalid, the bill amount should be considered as -1.
'''
# vegetarian combo costs Rs.120
# non-vegetarian combo costs Rs.150 per plate

# food, quantity (no. of plates) and the distance in kms

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if food_type=="N":
        plate_cost=150
    elif food_type=="V":
        plate_cost=120
    
    else:
        bill_amount=-1
        return bill_amount

    food_bill=plate_cost*quantity_ordered

    if distance_in_kms<=3:
        delivery_bill=0

    elif distance_in_kms>6:
        distance_in_kms=distance_in_kms-3 ###  7 -3 = 4
        delivery_bill_1=3*3
        delivery_bill_2=(distance_in_kms-3)*6    ##   (4 -3) * 6 = 6 + 9 =15

        delivery_bill=delivery_bill_1+delivery_bill_2
    elif distance_in_kms>3:
        delivery_bill=(distance_in_kms-3)*3


    bill_amount=food_bill+delivery_bill

    return bill_amount

# bill_amount=calculate_bill_amount("N",2,7)
# print(bill_amount)


# def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
#     if food_type == 'V' and quantity_ordered>0:
#         food_cost=120*quantity_ordered
#     elif food_type== 'N' and quantity_ordered>0:
#         food_cost=150*quantity_ordered
#     else:
#         return -1
   
#     if distance_in_kms<0:
#         return -1
#     if distance_in_kms>6:
#         delivery_charge = (distance_in_kms-6)*6+9
#     elif distance_in_kms>3 and distance_in_kms<=6:
#         delivery_charge=(distance_in_kms-3)*3
#     else:
#         delivery_charge=0
   
#     bill_amount=food_cost+delivery_charge
#     return bill_amount

# bill_amount=calculate_bill_amount("N",2,4)
# print("Total amount:",bill_amount)

# 300 + 3 = 303
# def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
#     bill_amount=0
#     deli_cst = 0
#     #write your logic here
#     dist = [(3,0),(6,3),(7,6)]
#     if food_type == "V":
#         bill_amount += 120*quantity_ordered
#     elif food_type == "N":
#         bill_amount += 150*quantity_ordered
#     else:
#         return -1


#     dist_covered = 0
#     while dist_covered <= distance_in_kms:
#         for distance in dist:
#             if dist_covered <= distance[0]:
#                 value = distance[1]
#                 break
#         deli_cst += value
#         dist_covered += 1

#     bill_amount += deli_cst
#     return bill_amount

# bill_amount=calculate_bill_amount("N",2,7)
# print(bill_amount)

# 150 * 2 = 300 + 9 + 6

# def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
#  bill_amount = 0
#  if food_type=='N' or 'n':
#   bill_amount=150*quantity_ordered
#   if distance_in_kms <= 3:
#    return bill_amount
#   elif distance_in_kms <= 6:
#    return bill_amount + 3
#   elif distance_in_kms > 6:
#    return bill_amount + 6
#   else:
#    return -1


#  elif food_type=='V' or 'v':
#   bill_amount=120*quantity_ordered
#   if distance_in_kms <=3:
#    return bill_amount
#   elif distance_in_kms<=6:
#    return  bill_amount+3
#   elif distance_in_kms>6:
#    return bill_amount+6
#   else:
#    return -1

#  else:
#   return -1


 # write your logic here


# bill_amount = calculate_bill_amount("N", 2, 7)
# print(bill_amount)

# 150 * 2 = 300 + 6 = 306



''''
You are keeping score for a baseball game with strange rules. The game consists of several rounds,
 where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops,
 where ops[i] is the ith operation you must apply to the record and is one of the following:

1. An integer x - Record a new score of x.
2. "+" - Record a new score that is the sum of the previous two scores. 
It is guaranteed there will always be two previous scores.
3. "D" - Record a new score that is double the previous score. It is guaranteed there will always be
 a previous score.
4. "C" - Invalidate the previous score, removing it from the record. 
It is guaranteed there will always be a previous score.

Return the sum of all the scores on the record.

Input: ops = ["5","2","C","D","+"]
Output: 30
'''

# myresult = 5  10 15 = 30


# records= [5]
# last = 1

# def calsum(ops):
#     records = [] 
#     last = -1
#     for i in ops:
#         if i.lstrip('-').isdigit():
#             records.append(int(i))
#             last += 1
#         elif i == 'D':
#             temp = records[last] * 2
#             records.append(temp)
#             last += 1
#         elif i == 'C':
#             records.pop()
#             last -= 1
#         elif i == '+':
#             # temp = records[last] + records[last-1]
#             records.append(records[last] + records[last-1])
#             last += 1
#     # print(records)
#     return sum(records)

def calsum(ops):
    records = []
    for i in ops:
        if i == 'C':
            records.pop()
        elif i == 'D':
            records.append(records[-1]*2)
        elif i == '+':
            records.append( records[-1] + records[-2]   )
        else:
            records.append(int(i))

    return sum(records)



ops = ["5","-2","C","D","+"]
# res = calsum(ops)
# print(res)

# print('534'*2)


'''
Write a python program which finds the maximum number from num1 to num2 
(num2 inclusive) based on the following rules.
 

1. Always num1 should be less than num2

# 8 -> 15 =  
# 12 = 1 +2 = 3
2. Consider each number from num1 to num2 (num2 inclusive). Populate the number
 into a list, if the below conditions are satisfied

      a. Sum of the digits of the number is a multiple of 3

      b. Number has only two digits

      c. Number is a multiple of 5

3. Display the maximum element from the list

In case of any invalid data or if the list is empty, display -1.
'''
# number = 123

def find_max(num1, num2):
    ls = []
    if num1 < num2:
        for i in range(num1,num2+1):
            if len(str(i)) == 2:
                sum = 0
                for digit in str(i):
                    sum += int(digit)
                if sum % 3 == 0:
                    if i % 5 == 0:
                        ls.append(i)
        return max(ls)
    else:
        return -1


# max_num=find_max(10,15)
# print(max_num)    

# 10 11 12 13 14 15

############### 
def create_largest_number(ls):
    ls.sort(reverse=True)
    ans = ''
    for i in ls:
        ans += str(i)
    # ls=list(map(str,ls))
    # n="".join(ls)
    print(int(ans))

# 
# y = [23,54,67]
# create_largest_number(y)

# 675423

################### Problem ####################
'''
Write a python program to display all the common characters between two strings. 

Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Sample Input                                Expected output

"I like Python"
"Java is a very popular language"               lieyon
'''

# def find_common_characters(msg1,msg2):
#     pass #Remove pass and write your logic here

# #Provide different values for msg1,msg2 and test your program
# msg1="I like Python"
# msg2="Java is a very popular language"
# common_characters=find_common_characters(msg1,msg2)
# print(common_characters)

# def find_common_characters(msg1,msg2):
#     s=""
#     for i in msg1:
#         if i==" ":
#             pass
#         elif i in msg2:
#             s+=i
#     if s=="":
#         return -1
#     else:
#         return s

# # #Provide different values for msg1,msg2 and test your program
# msg1="I like Python"
# msg2="Java is a very popular language"
# common_characters=find_common_characters(msg1,msg2)
# print(common_characters)

def find_common_characters(msg1,msg2):
    string = ''
    for i in msg1:
        if i in msg2:
            if i not in string:
                string = string + i
    if(string):
        return string.replace(" ","")
    else:
        return -1

#msg1 = input('Enter 1st string: ')
#msg2 = input('Enter 2nd string: ')

msg1="I like Python"
msg2="Java is a very popular language"
# common_characters=find_common_characters(msg1,msg2)
# print(common_characters)


'''
Write a python function to check whether three given numbers can form the sides of a triangle. 
Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.
'''

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    #Write your logic here

    #Use the following messages to return the result wherever necessary
    return success
    return failure

num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)


'''
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels
 and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.

Perform case sensitive string operations wherever necessary.

Exmple :-

the sun rises in the east    --> eht snu sesir ni eht stea
'''

                                                                                                                                                                                                                                                                                    
# def encrypt_sentence(sentence):
#     #start writing your code here

# sentence="The sun rises in the east"
# encrypted_sentence=encrypt_sentence(sentence)
# print(encrypted_sentence)


vowels=['a','e','i','o','u']

def encrypt_sentence(sentence):
    final=[]
    list_sentence = sentence.split(" ")
    for index,word in enumerate(list_sentence):
        if (index+1)%2!=0:
            final.append(word[::-1])
        else:
            v=[]#to store all vowels
            t=[]#to store the letters temporily
            for letter in word:
                if letter not in vowels:
                    t.append(letter)
                else:
                    v.append(letter)
            t.extend(v)
            # t = ['s','n','u']
            final.append("".join(t))
    #if len(final)>1:
    return " ".join(final)
                    
# sentence="the"
# encrypted_sentence=encrypt_sentence(sentence)
# print(encrypted_sentence)
sentence="the sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)



