s = {1}
s2 = set((1, 2, 3))
print(type(s))
print(type(s2))

s3 = {1, 2, 3, 1, 2, 4, 5, "Nithin", 3, 4, 5, True, False, [1,2, 3], {1, 2, 3}}
# s3[2]
print(s3)
s4 = {9, 7, 5, 7, 8, 9,4, 3, 2, 1, 2, 3, 4}
print(s4)
print(s4.pop())
# print(s4.pop(4)) #error
print(s4.remove(4))
# print(s4.remove())
# print(s4.remove(10))
print(s4)
s4.add(1)
s4.add((1, 2, 3))
print(s4)
# s4.update(3)
s4.update((11, 12, 13))
print(s4)
s4.discard(11)
print(s4)
print("####################################################")
ss = {1, 2, 3, 4, 5, 6, 7}
sss = {5, 6, 7, 8, 9, 10}
ss2 = {1, 2, 3}
oo = ss.difference(sss)
print(oo)
oo2 = sss.difference(ss)
print(oo2)

print(ss.union(sss))
print(ss.intersection(sss))
print(ss.issuperset(ss2))
print(ss.issuperset(sss))
print(ss.issubset(ss2))
print(ss2.issubset(ss))














