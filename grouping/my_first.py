# def <name of func>():
#     <logic>

def my():
    my_li = []
    for i in range(10):
        my_li.append(i)
    return my_li


def my_two():
    li_t = []
    start = input("enter your start num: ")
    end = input("enter your enf num:")
    for j in range(int(start), int(end)):
        li_t.insert(0, j)
    return li_t

def my_three():
    for c in range(51, 100, 5):
        print(c)

def test():
    pass

# fu = my()
# print(fu)
# fu.append(33)
# print(fu)

print(my_two())
print(my_two())
print(my_two())
print(my_two())


#today we are working on func