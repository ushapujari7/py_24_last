class one:
    def __init__(self, a, b):
        print("calling init")
        self.a = a
        self.b = b

    def add(self):
        print('calling add')
        print(self.a + self.b)

    def mul(self, c):
        print("calling mul")
        print(self.a * c)

    def add_self(self, d):
        print("calling add self")
        self.d = d

    def mul_d_a(self):
        print(self.a * self.d)

obj = one(2, 5)
obj.add()
obj.mul(5)
obj.add_self(6)
obj.mul_d_a()

