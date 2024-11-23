# Identity Operators
a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

print(a == b) #T
print(a is b) #T
print(c == d) #T
print(c is d) #F

# Membership Operators
print(f"{'#' * 10} Membership Operators {'#' *  10 }")
n = "Nithin"
li = [2, 3, 4, 5, True, False, n, "python"]
print("i" in n)
print("z" not in n)
print(1 in li)
print(0 not in li)
print(n in li)


# Tuple
t = (1,)
print(type(t))
t2 = tuple([1])
print(type(t2))
# Char ???
t3 = (1, 2, 3, "Nithin", True, False, 22.33, 3, 2)
print(t3.index(3, 3))
# print(t3.index(100)) #error
print(t3.count(3))
print(t3.count(100))


ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

for i in ll:
    if i % 2 == 0:
        print(f"{i} is even number")
    elif i % 2 != 0:
        print(f"{i} is odd number")



r = range(100)
for j in r:
    if j % 2 != 1:
        print(j)

rr = range(0, 100, 2)
print(list(rr))
rrr = range(1, 100, 2)
print(list(rrr))

cc = 14
if cc % 2 == 0 :
    print("yes")
else:
    print("No")

ln = len([1, 2, 3, 4, 5, 6, 7, "nirhin"])
print(ln)
lns = "nithin kumar reddy"

print(len(lns))

