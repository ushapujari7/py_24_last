class A:
    av = "nithin"
    av2 = 22
    _av3 = "python"
    __av4 = "mysql"

    def m1(self):
        print("from class A - M1")
        print(self.__av4)

    def __m3(self):
        print("from A - M3")

    def _m4(self):
        print("from A - M4")

class B(A):
    bv = "reddy"

    def m2(self):
        print("from class B - M2")
        print(self._av3)
        # print(self.__av4)
        print(self._A__av4)
        self.m1()

obj = B()
# print(dir(obj))
# print(help(obj))
# print(callable(obj.bv))
# print(callable(obj.m2))
# print(obj._av3)
# print(obj.__av4)
obj.m1()
obj.m2()
print(obj._A__av4)
obj._A__m3()
obj._m4()


