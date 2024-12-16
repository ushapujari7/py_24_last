class A():

    def __init__(self):
        print("from class A init")

    def m1(self):
        return "from class A - M1"

    def m2(self):
        print("from class A - M2")

class B(A):

    def __init__(self):
        print("from class B init")

    def m3(self):
        return "from class B - M3"

    def m2(self):
        # print("from class B - M2")
        super().m2()

# aa = A()
# print(aa.m1())
# print(aa.m3())
bb = B()
print(bb.m3())
print(bb.m1())
bb.m2()




