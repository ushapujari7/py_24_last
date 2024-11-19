l = [1, "nithin", True, 3+2j, 33.2, [33, 55, "varun", False]]
print(l)
print(type(l))
print(id(l), end="\n#########\n")
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# mutable
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a))
# print(id(b))
# b.append(33)
# print(a, b)

print(l[3])
print(l[1:5])
print(l[1][:4])
# print(l[3][:4])
print(l[0::3])
print(li[1::2])
print(li[2:100:3])
print(li[::-1])   #apply in string
print(l[-1])
# ll = l + li
# print(ll)
print(l + li)

ll = [1, 2, 3]
# print(dir(ll))
ll.append(4)
ll.append(5)
ll.append(5)
ll.append([123, 22, 33, 55])
ll[-1].append(22)
# ll.append(22, 33, 44, 55) # error
ss = ll.append((22, 33, 44, 55))
print(ss)
print(ll)

print(ll.count(5))
print(ll.count(22))
cc = ll[-2].count(22)
print(cc)
print(ll)
print(ll.count(100))

ll.pop(4)
ll.pop(-1)
pp = ll.pop(-1)
print(ll)
# ll.pop(7) #Error
print(ll)
print(pp)

















