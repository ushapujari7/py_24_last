# #even numbers in given range
#
# inp = input("Enter your input number: ")
#
# if inp.isnumeric():
#     for j in range(int(inp)):
#         if j % 2 == 0:
#             print(j)
# else:
#     print("input cannot be converted into int")
#
#
# # String input, ovels, conc, spl
#
# while True:
#     input_num = input("enter your number: ")
#     if input_num == "":
#         break
#     else:
#         if input_num.isnumeric():
#             for i in range(int(input_num)):
#                 if i % 2 == 0:
#                     print(i)
#         else:
#             print("input cannot be converted into int")
#             continue
import math

# even_li = []
# for k in range(23):
#     if k % 2 == 0:
#         even_li.append(k)

even_li = [k for k in range(5) if k % 2 == 0]
print(even_li)
odd_li = [k for k in range(5) if k % 2 == 1]
print(even_li)

even_tp = (k for k in range(5) if k % 2 == 0)
print(even_tp)


cube_di = {k:k**3 for k in range(11)}
print(cube_di)
import math
cube_di2 = {k:math.pow(k, 3) for k in range(11)}
print(cube_di2)












