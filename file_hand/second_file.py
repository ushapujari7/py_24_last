# file = open("test.txt", 'r')
# print(file.read())
# file.close()

# def read_any_file(f_p, mod="r"):
#     try:
#         print("entered into try")
#         file = open(f_p, mod)
#         print(file.read())
#     except FileNotFoundError:
#         print("entered into except")
#         print("please check the file if it exist in the path")
#     finally:
#         print("entered into finally")
#         file.close()
#
# read_any_file("test1.txt", "r")


f = open("test2.txt", "w")
f.write("jgdhkjggisa\nugdfiiashfdihsdgiufwe\niudshcuisahfidcz\njhdfuwa\n")
f.writelines(["dvadda\n", "dfasfasdf\n", "fasdfasfasd\n"])
# f.read()
f.close()


ff = open("test3.txt", "a")
ff.write("jgdhkjggisa\nugdfiiashfdihsdgiufwe\niudshcuisahfidcz\njhdfuwa\n")
ff.writelines(["dvadda\n", "dfasfasdf\n", "fasdfasfasd\n"])
# ff.read()
ff.close()


fff = open("test5.txt", "r+")
print(fff.read())
fff.write("jckdchkcs\njhjkhd\nsdhsghfga\nhfgkhads\n")









