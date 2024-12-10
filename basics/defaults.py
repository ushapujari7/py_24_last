['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError',
 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError',
 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError',
 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError',
 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning',
 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError',
 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',
 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError',
 '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__',


 '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes',
 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr',
 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format',
 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map',

 'max', 'memoryview','min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr',
 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple',
 'type', 'vars', 'zip']

a = -2.2
print(abs(a))
b = all([2==2, 2 + 4 ==6, 3*3==9])
print(b)
# if 2==2 and 2 + 4 ==6 or 3*3==10:
#     print("yes")
c = any([False, False, False])
print(c)
d = bin(22)
print(d)
n = "nithin"
for ind, i in enumerate(n,0):
    print(ind, i)


b = "[1, 2, 3, 4, 5]"
print(type(b))
print(type(eval(b)))
# d = "nithin"
# print(type(d))
# print(type(eval(d)))

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def eve_f(x):
    return x % 2 == 0

even = filter(eve_f, li)
odd_l = filter(lambda x: x % 2 == 1 , li)

print(list(even))
print(list(odd_l))

def mpp(x):
    return x + 2
mp = map(mpp, li)
print(list(mp))
mppp = map(lambda x: x**3, li)
print(list(mppp))


mx = max(li)
print(mx)

mi = min(li)
print(mi)

po = pow(3, 3)
print(po)


rev = reversed(li)
print(list(rev))


fl = 22.56999
rr = round(fl, 2)
print(rr)

ll = [3, 4, 7, 9, 2, 1, 6, 8, 6, 8, 4, 2, 4]
print(sorted(ll, reverse=True))

l1 = [1, 2, 3, 4, 5, 6]
l2 = [4, 5, 6, 7]
l3 = [4, 6, 0]

z1 = zip(li, l2, l3)
print(list(z1))












