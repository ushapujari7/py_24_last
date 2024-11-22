from pickle import PROTO

a = 10
b = 2
c = 0
d = 22.3
e = True
f = False
l = [1, 2, 3]
st = "nithin"

#Arithmetic Operators
ar1 = a + b # 12 int
ar2 = a - b # 8 int
ar3 = e + f # 1 int
ar4 = a / b # 5 float
ar5 = a // 3 # 3.33
ar6 = a //b # 5
# ar7  = st - b
ar8  = st * b
ar9 = st + " reddy"
ar10 = 10 % 3 # 1 reminder
ar11 = a ** 3 # 1000, ---- 10*10*10

print(*(ar1, ar2, ar3, ar4, ar5, ar6, ar8, ar9, ar10, ar11), sep="\n")




##Comparison Operators # True , False

x, y, z = 10, 5, 22
co1 = x == y # F
co2 = x != y # T
co3 = z > x # T
co4 = x < y # F
co5 = x >= y # T
co6 = z <= 22 # T
co7 = "nithin" == "Nithin"

print(*(co1, co2, co3, co4, co5, co6, co7), sep="\n")


# Assignment Operators
ao = 1
ao += 3 # ao = ao + 3
ao -= 2 # ao = ao - 2
ao *= 3 # ao = ao * 3

print(ao)


# Logical Operators
print("#" * 10, "Logical Operators", "#" * 10)
print(True and True)
print(5 > 2 and 8 <= 9)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)

print(not True)
print(not 22 % 10 == 2)
print(not False)

















