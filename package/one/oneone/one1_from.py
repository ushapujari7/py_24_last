from package.sample import *
from package.one import one_from as of
from package.sample import MAIN_VAR as mv


def add_sur_name(f_n, l_n):
    return f'{f_n} {l_n}'


full_name = add_sur_name(mv, "Thallapalli")
# print(full_name)
#
print(sample_add(5, 6))
#
# print(TEST_VAR)
# print(Hello_Hello("Venkey"))

convert_into_list = of.give_it_to_for_loop(full_name)
print(convert_into_list)


print(of.VARABLE_FROM_ONE)
print(of.sub_from_one(3, 2))


