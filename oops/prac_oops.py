from abc import ABC, abstractmethod
class RBI(ABC):
    def w_limit(self):
        pass

class SBI(RBI):
    def __init__(self, name, bal, ph_num, address, ac_t):
        self.name = name
        self.bal = bal
        self.ph = ph_num
        self.add = address
        self.at = ac_t

    def __repr__(self):
        return self.name

    def w_limit(self):
        if self.at == "nsal":
            return 20000
        elif self.at == "sal":
            return 40000

    def deposit(self, d_amo):
        self.bal += d_amo

    def withdrawl(self, w_amo):
        if self.bal >= w_amo:
            if self.w_limit() > w_amo:
                self.bal -= w_amo
                print(f"hi {self.name}, {w_amo} has be deducted, and your bal is {self.bal}")
            else: print("limit is higher than your daily liit")
        else: print("Low balance")

    def check_bal(self):
        print(f"hi {self.name}, your balance is {self.bal}")

class HDFC():
    pass


nn = SBI(name="venkey", bal=50000, ph_num="xxxxxxx123", address="khlkvadh, jfaw, avbsa", ac_t='nsal')
nn.check_bal()
nn.withdrawl(2000)
nn.check_bal()
nn.withdrawl(19000)
nn.check_bal()
us = SBI(name="usha", bal=70000, ph_num="xxxxxxx123", address="khlkvadh, jfaw, avbsa", ac_t='sal')
us.check_bal()
us.withdrawl(35000)
us.check_bal()
us.withdrawl(36000)
us.withdrawl(35000)
us.check_bal()


