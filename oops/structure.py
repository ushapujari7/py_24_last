from abc import ABC, abstractmethod

class Engien(ABC):
    @abstractmethod
    def start(self):
        print("starting engin")
    @abstractmethod
    def stop(self):
        print("Stopping engin")

class Scooty(Engien):

    def start(self):
        print("starting Scooty engin")

    def stop(self):
        print("Stopping Scooty engin")

class Car(Engien):
    def start(self):
        print("starting Car engin")

    def stop(self):
        print("Stopping Car engin")

class cycle(Engien):

    def start(self):
        pass

    def stop(self):
        pass

# ob1 = Scooty()
# ob1.start()
# ob1.stop()
# ob2 = Car()
# ob2.start()
# ob2.stop()