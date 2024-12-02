from basics.all_prac_two import even_li


def is_even_num(a):
    out = (a % 2 == 0)
    return out

print(is_even_num(999)) #False
print(is_even_num(22)) # True
print(is_even_num(True + True)) # True
print(is_even_num(0)) # True

def math_table(table_num):
    pass

math_table(2)
math_table(6)


def second_func_two(a, b, c):
    return a + c - b

second_func_two(3, 5, 10) #8
second_func_two(a=3, c=5, b=10) #-2
second_func_two(9, c=2, b=1)
second_func_two(3, 5, c=22)
# second_func_two(9, 2, a=1, c=3)
# second_func_two(33)
# second_func_two(b=24)


def third_func_day_two(a, b, c, d):
    return a + b

# third_func_day_two(a=100, b=200) #Error
print(third_func_day_two(1,8,6,9))
print(third_func_day_two(c=100, b=10, d=300, a=10))


def four_func(a, b, c=10, d=0):
    return a+b+c-d

print(four_func(1, 2))
print(four_func(10, 20, 30, 40))
print(four_func(20, 40, d=10)) #70, 60, 70

#string with default arguments
#Table task


















