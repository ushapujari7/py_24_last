def doc_str_test_method(a, b=1, c=None):
    '''
    This is a testing of doc string
    :param a: it is required arg
    :type: int
    :param b: it is optional, Default value will be 1.
    :type: int
    :param c: Optional, default value None
    :return: it will return Mul of a, b int with string c.
    :rtype: string
    '''
    return (a*b)*c

st = doc_str_test_method(2, 3, "Nithin")
print(help(doc_str_test_method))


def doc_sec_type(x, y=1, z=None):
    '''
    this second doc
    Args:
        arg1 (int): x desc of arg1
        arg2 (int): y desc of arg2
        arg3 (str): z desc of arg3
    Return (str): it will return Mul of x, y int with string z
    '''
    if isinstance(x, int):
        return (x * y) * z


print(doc_sec_type(2, True, "Nithin"))
print(help(doc_sec_type))


m_li = []
j=1
def multiples(mul):
    mul = 5
    for i in range(1,11):
        mul = 7
        m_li.append(f'{mul}*{i}={j*mul}')
    return  m_li

def hello_test(x):
    m_li = []
    for i in range(x):
        m_li.append(i)
    # print(mul)
    # print(j)
    return m_li

print(*multiples(5), sep="\n")
print(hello_test(5))




def is_even(x):
    return
print(is_even(21))
print(is_even)
hh = is_even
print(hh(23))

#lambda <arg>: <logic>
is_even_l = lambda x: x % 2 == 0
print(is_even_l(22))

a = lambda : 21 % 2 == 0
print(a)
print(a())

mu = lambda i, j: i*j
print(mu(3, 5))


ad = lambda y: sum(y)
print(ad([1, 2, 3, 4, 5, 6]))


def hello_list(l):
    sum = 0
    summ = 0
    for i in l:
        sum = sum + i
        summ += i
    return sum, summ+10, 10, 15


print(hello_list([1, 2, 3, 4, 5, 6, 7]))
ss = hello_list([1, 2, 3, 4, 5, 6, 7, 8])
print(len(ss))
print(type(ss))

def printing(ll):
    for j in ll:
        print(j - 20)

printing(ss)
