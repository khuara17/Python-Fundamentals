# #Basic of function passing
# # def add (x):
# #     def b(y):
# #         print(y)
# #         return x+y
# #     return b
# # a = add(10)
# # print(a(15))    

# #* args  
# # This is used to get dynamic number of arguments 
# # it is mostly used in decorators
# # return type is tuple
# def demo(electronics ,*numbers):
#     print(f"electronics value is {electronics}")
#     for i in numbers:
#         print(i)
# # ** kwargs 
# # return type as dic 
# def demokwargs(*args ,**kwargs):
#     print(args) 
#     print(kwargs.keys())

# demokwargs(1,2,3,a=10,b=11)

"""Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.
Example 1:
Input
: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1"""

def anything(a):
    def fromdec():

        print("i am called ")
        a()
        print("Executed")
    return fromdec    

@anything
def test():
    print("I am tested")

test()






