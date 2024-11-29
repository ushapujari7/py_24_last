s = "p#%yt hon@1$"
vowels = ['A', 'E', 'I', 'O', 'U']
for i in s:
    if i.upper() in vowels:
        print(i.upper())
    elif i == " ":
        break
    elif not i.isalnum():
        continue
    elif i.isalnum():
        print(i)

data_types_list = [
    10,                             # Integer
    -42,                            # Integer
    3.14,                           # Float
    -0.987,                         # Float
    2 + 3j,                         # Complex number
    7 - 4j,                         # Complex number
    {"key1": "value1"},             # Dictionary
    {"key2": 42, "key3": 3.14},     # Dictionary
    {1, 2, 3},                      # Set
    {4, 5, 6},                      # Set
    (1, 2, 3),                      # Tuple
    (7.5, "tuple", 9),              # Tuple
    [1, 2, 3],                      # List
    ["a", "b", "c"],                # List
    "Hello, Python!",               # String
    "12345",                        # String
    [1.1, 2.2, 3.3],                # List
    {100, 200, 300},                # Set
    {"name": "Python", "type": "language"}, # Dictionary
    (10, 20.5, "mixed")             # Tuple
]

pre_li = []
col_li = []
for i in data_types_list:
    if isinstance(i, (int, str, bool, float, complex)):
        pre_li.append(i)
    elif isinstance(i, (set, tuple, list, dict)):
        if isinstance(i, dict):
            pass
        else:
            for j in i:
                if isinstance(j, int):
                    for cn in range(j):
                        print(cn)
                else:
                    print(j)

print(pre_li)
print(col_li)




di = {
    1: "integer key one",           # Integer key
    2: "integer key two",           # Integer key
    "three": "string key three",    # String key
    "four": "string key four",      # String key
    5: "integer key five",          # Integer key
    "six": "string key six"         # String key
}

in_key = []
sr_key = []
for i, j in di.items():
    if type(i) == int: # isinstance(i, int,)
        in_key.insert(0, (i, j))
    else:
        sr_key.append((i, j))

print(in_key)
print(sr_key)



