def dial_div(a, b):
    try:
        return a/b
    except TypeError:
        return f"cannot divide {a} with {b}"
    except ZeroDivisionError:
        return f"any num cannot device with Zero"
    except:
        return f"found an error while {a} device {b}"

dd = dial_div(10, "nnn")
dd3 = dial_div(10, 2)
dd4 = dial_div(10, 0)
print(dd)
print(dd3)
print(dd4)


def dial_add(a, b):
    tem = 0
    try:
        tem = a + b
    except TypeError:
        return f"Cannot add {a, b}"
    finally:
        return tem

print(dial_add(2, 3))
print(dial_add("5", "6"))
print(dial_add(9, '4'))



def find_rank(li, stu):
    temp = -1
    try:
        temp = li.index(stu)
    except ValueError:
        return f"{stu} not found in the list"
    except AttributeError:
        return f"operation cannot be done with {li, [stu]}"
    else:
        return f"from else {temp}"




l = ["nithin", "purnesh", "sai", "venkey", "usha"]
st = "sai"
print(find_rank(l, "sai"))
print(find_rank(l, "NithIn"))
print(find_rank("nithin", "rr"))
print(find_rank(22, "rr"))



def find_in_dic(d, ser):
    temp = -1
    try:
        temp = d[ser]
        pass
    except KeyError:
        temp = d.get(ser)
    finally:
        return temp


di = {1:3, 4:"55", "nithin": "guid", 'students':["sai", "venky", "purnesh"]}
print(find_in_dic(di, 'nithin'))
print(find_in_dic(di, 'reddy'))











