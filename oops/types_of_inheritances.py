class A:
    def __init__(self):
        print("A class INIT")

    def m1(self):
        print("A class M1")

    def m2(self):
        print("A class M3")

class B(A):
    def __init__(self):
        print("B class INIT")

    def m1(self):
        print("B class M1")

    def m3(self):
        print("B class M3")

class C(B):
    def __init__(self):
        print("C class INIT")

    def m1(self):
        print("C class M1")

    def m4(self):
        print("C class M4")

aa = C()
aa.m1()
aa.m3()
aa.m4()
aa.m2()



class A:
    def __init__(self):
        print("A class INIT")

    def m1(self):
        print("A class M1")

    def m2(self):
        print("A class M3")

class B(A):
    def __init__(self):
        print("B class INIT")

    def m1(self):
        print("B class M1")

    def m3(self):
        print("B class M3")

class C(A):
    def __init__(self):
        print("C class INIT")

    def m1(self):
        print("C class M1")

    def m4(self):
        print("C class M4")

cc = C()
cc.m4()
# cc.m3()
bb = B()
bb.m3()

print(f"{'#' * 20}")



class A:
    def __init__(self):
        print("A class INIT")

    def m1(self):
        print("A class M1")

    def m2(self):
        print("A class M3")

    def m3(self):
        print("A class M3")

class B:
    def __init__(self):
        print("B class INIT")

    def m1(self):
        print("B class M1")

    def m3(self):
        print("B class M3")

class C:
    def __init__(self):
        print("C class INIT")

    def m1(self):
        print("C class M1")

    def m4(self):
        print("C class M4")



class D(A, B, C):
    def __init__(self):
        print("C class INIT")

    def m1(self):
        print("D class M1")

    def m4(self):
        print("C class M4")



mm = D()
mm.m4()
mm.m3()












class A:
    def __init__(self):
        print("A class INIT")

    def m1(self):
        print("A class M1")

    def m2(self):
        print("A class M3")

    def m3(self):
        print("A class M3")

class B(A):
    def __init__(self):
        print("B class INIT")

    def m1(self):
        print("B class M1")

    def m3(self):
        print("B class M3")

class C(B):
    def __init__(self):
        print("C class INIT")

    def m1(self):
        print("C class M1")

    def m4(self):
        print("C class M4")



class D(C, B, A):
    def __init__(self):
        print("C class INIT")

    def m1(self):
        print("D class M1")

    def m4(self):
        print("C class M4")


hy = D()
hy.m4()
hy.m3()


