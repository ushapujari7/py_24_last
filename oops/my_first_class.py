GLOBAL_VAR = "Global"


class MyClass:
    '''
    This is my first class
    And here we are learning about OOPS and class structures
    '''
    CLASS_VAR = "Class"
    a = 22

    def __init__(self, b, c, d):
        self.b = b
        self.c = c
        self.nn = d

    def double(self):
        '''here we are doubling a value'''
        return self.a + self.a

    def sum_of_all(self):
        '''returning sum of a, b, c, d'''
        return self.a + self.b + self.c + self.nn

    def mul_a_b(self):
        return self.a * self.b

    def mul_a_with_your_choice(self, f):
        return self.a * f

    def assign_to_self(self, g):
        self.g = g

    def new_mul_g_with_a(self):
        return self.g * self.a


obj = MyClass(10, 20, 30)
print(obj.double())
aa = obj.sum_of_all()
print(aa)
print(obj.mul_a_b())
print(obj.mul_a_with_your_choice(5))
obj.assign_to_self(15)
print(obj.new_mul_g_with_a())



# print(dir(obj))
# print(help(obj))
# ob = MyClass()
# dou = ob.double()
# print(dou)