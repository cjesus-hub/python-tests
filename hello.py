#!/usr/bin/python3

from pprint import pprint as pprint
greetings: str = "Hello World"
number = 100_000
number_simple = 100
decimal = 100.1
complex = 8j
seq = ["bla",1]
tuple = (1,1,1)
range = range(1,1000)
dict = {"a": number}
set  = {1,1,2,2,3,4}
frozenset = frozenset({1,1,1,2,2,3})
boolean = True
bytes = bytes(0)
bytearray = bytearray(0)
memoryview  = memoryview (bytes)

pprint (type(greetings))
pprint (type(number))
pprint (type(number_simple ))
pprint (type(decimal))
pprint (type(complex))
pprint (type(seq))
pprint (type(tuple))
pprint (type(range))
pprint (type(dict))
pprint (type(set))
pprint (type(frozenset))
pprint (type(boolean))
pprint (type(bytes))
pprint (type(bytearray))
pprint (type(memoryview))
pprint (type(None))

pprint (float(number)  + float(decimal))

pprint (int(number)  + int(decimal))
pprint (int(number_simple)  + int(decimal))
pprint (greetings + str(number))
