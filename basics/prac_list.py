l = [1, "nithin", True, 3+2j, 33.2, [33, 55, "varun", False]]
l2 = list((1, 2, 3, 4, 5, 6))
print(l, l2)
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

lis = [1, 2, 3, 'nithin', "python", True, 44.3, 33, 56, 75, 89, 99, 100]
liss = [3, 1, 9, 3, 5, 7, 1, 4, True, False]
liss.sort()
print(liss)
print(liss[::-1])
liss.sort(reverse=True)
print(liss)
# lis.sort()
# print(lis)

#sorting for only int, only strings
print(lis)
lis.reverse()
print(lis)

lc = [1, 2, 3, 4, 5]
lc.clear()
print(lc)

lii = [1, 2]
lii.append([22]) # [1, 2, [22]]
print(lii)
lii.extend([33]) # [1, 2, [22], 33]
# lii.extend(33) # error
lii.extend(['Django', 44, 77, 100])
print(lii)
lii.extend('python')
print(lii)


l4 = [1, 10, 4, True, False, 33, 55, 77, 86, 92]
l4.remove(10)
# l4.remove(100) #error
# l4.remove() #error
print(l4)

l5 = ['nithin', 'nagendra', 'purnesh', 'venkat']
l6 = l5.copy()
l5.append('saikiran')
print(l6)
print(l5)
l6.append('usha')
print(l6)


l7 = [3, 7, 5, 9, 2, 1, 4]
l7.insert(0, 10)
print(l7)
l7.insert(0, 20)
print(l7)
#l7.insert(50) #error
l7.insert(5, "hello")
print(l7)
l7.insert(5, ["hello", 4444, 555, 666])
print(l7)
l7.insert(100, "testing")
print(l7)
# negative index insert



l8 = [1, 4, 2, 7, 3, 8, 4, 0, 3, 4, 5, 6, 6]
print(l8.index(7))
# print(l8.index(50)) Error
print(l8.index(4))
print(l8.index(4, 2))
# print(l8.index(4, 7)) Error
print(l8.index(3, 5, 10))

l1 = [1, 2, 3]
l2 = [5, 4, 6]
ll1 = l1+l2 #extend
print(ll1)
ll2 = l1 + [l2] #[1, 2, 3, [5, 4, 6]]
print(ll2)
#v1 = 33






















