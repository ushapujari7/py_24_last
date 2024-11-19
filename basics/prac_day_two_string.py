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


#string
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
# diff between casefold, lower?????
print(f.center(50, "*"))
g = "bye"
print(g.center(9))
print(g.center(9, "*"))
print(g.rjust(9, "#"))
print(g.ljust(9, "#"))
print(g.zfill(10))

txt = "\thello \twelcome \tto \tpython \tclass"
txt2 = "   he   llo   "
txt3 = "we are going to prac python string we are"
t1 = txt.expandtabs(9)
print(t1)
t2 = txt3.replace("we are", "I am").replace("o", "0")
t3 = txt3.replace("a", "@")
print(txt3)
print(t2)
print(t3)
print(txt2)
t3 = txt2.strip()
print(t3)



#bool
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




#List
cen = "we are going to test a split method"
cc = cen.split()
cc2 = cen.split("to")
cc3 = cen.split("a")
print(cc)
print(cc2)
print(cc3)

enst = "My name is Ståle"
en1 = enst.encode()
print(en1)

st = "Hi hello how are you nithin, class are taken by Nithin"
st1 = st.count("i")
print(st1)
print(st.count("I"))
print(st.count("Ni"))
print(st.count("in"))


# format_map, join ??????????????????????????????????

nst = 'its nithin\'s class'
nst2 = '''its nithin's class'''
nst3 = "its nithin's class"
nst4 = 'its nithin"s class'

# its nithin's class

print(*[nst, nst2, nst3, nst4], sep="\n", end='*********\n')




si1 = "my name is Nagendra, im here to learn SQL"
si2 = "my name is Venkat, im here to learn python"
si3 = "my name is usha, im here to learn python & django"

print(*(si1, si2, si3), sep="\n")

sid = "my name is {0}, im here to learn {1}"
si_na = sid.format("Nagendra", "SQL")
print(si_na)
si_ve = sid.format("Venkat", "python")
print(si_ve)



name = "Saikiran"
cou = "Full stack"
fst = f"my name is {name}, im here to learn {cou}"
print(fst)



s_st = "Hi my name is Nithin, here Im teaching Pyhton"
print(s_st[0])
print(s_st[20])
print(s_st[3:10]) #print(s_st[inc:exe])
print(s_st[0:26])
print(s_st[:26])
print(s_st[3:])
print(s_st[3:500])
print(s_st[-6:])
print(s_st[-6:200])


im_s = "Nithin"
he = "Nithin"
hs = "nithin"
print(id(im_s))
print(id(he))
print(id(hs))

hh = he.upper()
print(he.upper())
print(hh)
print(he)


# li = [1, 2, 3]
# li2 = [1, 2, 3]
# li.append(10)
# print(id(li))
# print(id(li2))
# print(li)
#
#
#
# s = "lkfdlk"
# print(dir(s))
# print(help(str))
# i = 2
# print(dir(i))

























