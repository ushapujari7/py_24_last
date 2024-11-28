import  math
import datetime
import random
import time


li = [1, 2, 3, 4, 5, 6,7, 8, 16, 25]
for v in li:
    print(math.sqrt(v))
    print(math.pow(v, 3))
    print(math.cos(v))

time.sleep(2)
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S.%f"))
time.sleep(2)
print(random.randint(1, 10))
print(random.random())
time.sleep(2)
print(random.randrange(4))



