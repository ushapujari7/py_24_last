from pickle import PROTO


class A:
    '''About Class A and its char'''
    NAME = "Nithin Reddy"

    def __init__(self):
        pass

    def __str__(self):
        return "10"

    def __repr__(self):
        return 15

    # def __add__(self, a):
    #     return self + a


# cc = A()
# print(cc)
# print(dir(cc))
# for i in range(cc):
#     print(i)
# cc.__add__(10)


class SS:
    def __init__(self, r=10):
        print("From INIT")
        self.r = r

    def m1(self):
        print("From M1")
        return range(self.r)

    @staticmethod
    def m2(ss):
        print("From M2")
        ll = [i for i in ss if i % 2 == 0]
        print(ll)
        return ll


    def m3(self):
        print("from M3")
        return sum(self.m2(self.m1()))


ss = SS(17)
# ss.m3()
ss.m2([1, 2, 3, 4])
ss.m3()