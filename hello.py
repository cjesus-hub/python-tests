#!/usr/bin/python3

from pprint import pprint as pprint

greetings: str = "Hello World"
NUMBER = 100_000
NUMBER_SIMPLE = 100
DECIMAL = 100.1
COMPLEX = 8j
seq = ["bla", 1]
tuple = (1, 1, 1)
range = range(1, 1000)
dict: dict = {"a": NUMBER}
set: set = {1, 1, 2, 2, 3, 4}
frozenset = frozenset({1, 1, 1, 2, 2, 3})
boolean = True
bytes = bytes(0)
bytearray = bytearray(0)
memoryview = memoryview(bytes)

pprint(type(greetings))
pprint(type(NUMBER))
pprint(type(NUMBER_SIMPLE))
pprint(type(DECIMAL))
pprint(type(complex))


pprint(type(seq))
pprint(type(tuple))
pprint(type(range))
pprint(type(dict))
pprint(type(set))
pprint(type(frozenset))
pprint(type(boolean))
pprint(type(bytes))
pprint(type(bytearray))
pprint(type(memoryview))
pprint(type(None))

pprint(float(NUMBER) + float(DECIMAL))

pprint(int(NUMBER) + int(DECIMAL))
pprint(int(NUMBER_SIMPLE) + int(DECIMAL))
pprint(greetings + str(NUMBER))


def function():
    pprint("lsp test")

# test lsp import, flake8 error
from pprint import pprint as pprint
pprint(test)

