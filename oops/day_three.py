bus_stop = "Majestic"
airpot = "KIA"
G_num = 55


class Narayana:
    '''hello doc string'''
    ground = "Narayana Ground"

    def __init__(self, name, roll, age, cls, t_name, adds=None):
        self.name = name
        self.cls = cls
        self.age = age
        self.roll = roll
        self.t_name = t_name
        self.adds = adds

    def student_data(self):
        '''it contains all student info'''
        return (f"My name is {self.name}, studing in {self.cls} year, "
                f"with roll num of {self.roll} under {self.t_name}")

    def teachers_data(self):
        return f"my name is {self.t_name} and {self.name} is studying under my inspection"



class Chaitnya:

    def __init__(self):
        pass

purnesh = Narayana(name="purnesh", roll="1234", age=25, cls=4, t_name="nithin")
print(dir(purnesh))
# print(help(purnesh))
print(purnesh.student_data())
purnesh.teachers_data()
print(callable(purnesh.student_data))
print(callable(purnesh.roll))

usha = Narayana(name="usha", roll="456", age="xx", cls=3, t_name="Reddy")
print(usha.student_data())

# dum = Chaitnya()
# dum.student_data()




