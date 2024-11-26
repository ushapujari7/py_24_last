di = {1:1, 2:4, 3:9, 4:16, 5:25, 1:0, 6:9 , "nithin":"class host",
      (1, 2, 3):66, 11:{4:{3:4}}}
dd = dict([(1, 2), (2, 3)])

tp = (22.33,)
print(type(di), type(tp))
print(di)
print(type(di))
print(id(di))

print(di.keys()) #list #dict_keys
print(di.values()) #list #dict_values
print(di.items()) # list of tuples [(),()]

print(di.pop(1))
print(di.pop(4))
# print(di.pop()) #error
# print(di.pop(100)) #error


# print(di.update((200, 300)))
# print(di.update({400, 300}))
print(di.update({400: 300, 50:500}))
print(di.update([(200, 300), (40, 400)]))
print(di)
# di.popitem() ??????????????????????????????????????????

dd4 = dict.fromkeys([1, 2, 3, 4, 5, 6], 500)
print(dd4)
dd4 = dict.fromkeys([1, 2, 3, 4, 5, 6], [500, 400])
print(dd4)


dd5 = {1:10, 2:20, 3:30}
dd5.setdefault(5, 100)
dd5.setdefault(6)
dd5.setdefault(7)
print(dd5)


print(dd5.get(1))
print(dd5.get(3))
print(dd5.get(4))
print(dd5[3])
print(dd5[4])











