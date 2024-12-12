file = open(r'C:\work\py_24_last\basics\hello.txt')

data = file.readline()
print(f"data {data}")
print(file.tell())
data2 = file.readline()
print(f"data2 {data2}")
print(file.tell())
file.seek(0)
re = file.read()
print(f"re {re}")
print(file.tell())
file.seek(36)
data_lines = file.readlines()
print(data_lines)









