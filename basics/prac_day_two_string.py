a = "Nithin"
print(a)
print(type(a))
print(id(a))

b = 'python class'

c = '''\nhello welcome to python class jlkfhjdsho
thanks for joining'''

d = """\nbye jhflkjha
khsfkl
\tkjklfs"""

print(b, c, d)
print(type(b), type(c), type(d), sep="\n", end="\n########################\n")

e = "Hi welcome to python class"
e1 = e.upper()
print(e)
print(e1)
e_tit = e.title()
print(e_tit)
e3 = e.capitalize()
print(e3)

f = "tHis is Python ClAsS"
print(f.swapcase())
print(f.casefold())
print(f.lower())
# diff between casefold, casefold?????
print(f.center(50, "*"))
g = "bye"
print(g.center(9))
print(g.center(9, "*"))
print(g.rjust(9, "#"))
print(g.ljust(9, "#"))
print(g.zfill(10))

s = "nithinreddy221"
s2 = "hello"
s3 = "234"
print(s.endswith("dy221"))
print(s.endswith("223"))
print(s.startswith("n"))
print(s.startswith("nith"))
print(s.startswith("221"))
print(s.isalnum())
print(s.isalpha())
print(g.isalpha())
print(s.isdigit())
print(s2.isdigit())
print(s3.isdigit())
print(s2.isalnum())
print(s3.isalnum())














