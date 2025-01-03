from time import perf_counter

li = [2, 6, 3, 9, 15, 7, 4, 16]

#for <DY_VAR> in <Iterable>:
    #operation

for i in li:
    a = i * i
    print(a)

for j in li:
    b = j + 2
    print(b)


#while <Condition>:
#   operation

while li:
    ll = li.pop(0)
    print(ll)
    print("yes")
print("###########################################################")
vrr = 0
while vrr < 10:
    print(vrr)
    vrr += 1
    print("after adding" , vrr)


# if <CONDITION>>:
#     Operation
# else:
#     Operation

if 2+2 == 5:
    print("Hi ")
elif 3+3 == 6:
    print("hello")
elif 4+4 == 9:
    print("good")
else:
    print("Bye")



if 2+2 == 5:
    print("operation done")
elif 3+3 == 6:
    print("operation passed in 2 step")
else:
    print("operation failed")

ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for k in ll:
    if k == 2:
        print('it is two')
    elif k == 3:
        print('its three')
    elif k == 4:
        print('its four')
    elif k == 5:
        print('its five ')
    else:
        print('it is not two, three, four or five')