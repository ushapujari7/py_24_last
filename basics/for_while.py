# s = "welcome to python class 28"
# vowels = ['A', 'E', 'I', 'O', 'U']
#
# for i, j in enumerate(s):
#     if j.upper() in vowels:
#         print(i, j)
#     elif j == " ":
#         continue
#     elif j.upper() not in vowels:
#         print(j)


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in li:
    if i % 2 == 0:
        continue
    else:
        print(i)

lli = []
for j in li:
    if len(lli) == 5:
        break
    else:
        lli.append(j)
print(lli)


for i in li:
    if i % 3 == 0:
        pass
    else:
        print(i)


def pass_func():
    pass


def for_loop():
    lli = []
    for j in li:
        if len(lli) == 5:
            break
        else:
            lli.append(j)
    print("hello")
    return lli
    print(lli)



jj = for_loop()
print('jj value:- ', jj)


di = {1:1, 2:2, 3:3}












