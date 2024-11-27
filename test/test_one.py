# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# s = "welcome to python class"
# temp = 0
# for i in s:
#     if i in vowels:
#         print(temp, i)
#     temp += 1


# vowels = ['A', 'E', 'I', 'O', 'U']
# s = "welcome to python class"
# for i, j in enumerate(s):
#     if j.upper() in vowels:
#         print(i, j)


# vowels = ['A', 'E', 'I', 'O', 'U']
# var = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
#        'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
#        'x', 'y', 'z']
# s = "welcOme to p@ython c####lass@"
#
# for i, j in enumerate(s):
#     if j.upper() in vowels:
#         print(f"{j} at index {i} is vowel")
#     elif (j.lower() not in vowels) and (j.lower() in var):
#         print(f"{j} at index {i} is consonants")
#     else:
#         print(f"{j} at index {i} is not vowel nether consonants")


vowels = ['A', 'E', 'I', 'O', 'U']
var = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
       'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
       'x', 'y', 'z']
nli = ["1", '2', '3', '4', '5', '6']
s = "welc45Ome to p@yt12hon c####lass@1234&&&%64%"
v_li = []
c_li = []
s_li = []
space_li = []
at_li = []
num_li = []
for i, j in enumerate(s):
    if j.upper() in vowels:
        v_li.append(j)
    elif (j.lower() not in vowels) and (j.lower() in var):
        c_li.append(j)
    elif j == " ":
        space_li.append(j)
    elif j == "@":
        at_li.append(j)
    elif j.isdigit():
        num_li.append(j)
    else:
        s_li.append(j)




print(v_li,
c_li,
s_li,
space_li ,
at_li,
num_li)
