# Write a program to find the maximum element in the list without using inbuilt function

myls = [3,5,6,7,8]
# print(max(myls))
# max=-1


myls.sort()
print(myls[-1])
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