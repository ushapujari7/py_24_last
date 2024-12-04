def first_four(a, b, c, d, e):
    return sum([a, b, c, d, e])

dd = first_four(1, 2, 3, 4, 5)
print(dd)

def first_four_two(*a):
    print(type(a))
    return sum(a[:3] + a[4:]) - a[3]

dd = first_four_two(1, 2, 3, 4, 5, 6, True, False)
print(dd)


def second_four(a, b, *c):
    return  sum(c) + b + a
sf = second_four(1, 2, 3, 4, 5, 6, 7, 8)
print(sf)


def second_four_2(*c, a, b=0):
    print(*(a, b, c), sep="\n")
    return sum(c) + a + b
sf = second_four_2(1, 2, 3, 4, 5, 6, 7, 8, a=3, b=True)
print(sf)



def third_four(a, *b, **c):
    print(*(a, b, c), sep="\n")
    return f"{c.get('nn')}:- {sum(b) + a - c.get('d') - c['c']}"

kk = third_four(1, 2, 3, 4, 5, 6, d=2, c=3, nn="nithin reddy")
print(kk)




a, b, *c = [1, 'Nithin', 33.44, 33, 55, 66, 77, 85]
print(a, b, c)
a, b, *c = (1, 'Nithin', 33.44, 33, 55, 66, 77, 85)
print(a, b, c)










