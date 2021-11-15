from collections import namedtuple
from pympler import asizeof
# tuple : collection of items in a sequence 
# tup =(1,'ANUSHA',23) 
# tup[0] :1
#dictionary consumes more space , tuple is lighter weight. I Want to acces the tuple like dictionary but not with much of a space
#pip install pympler --- one of the memory profiling tool

Point = namedtuple("Point","x y z ")
p =Point(10,20,30)
print(p.x)

#run this in prompt -- we can see  output like this : namedtuple:160 bytes (67.74 % smaller), dict496 bytes
namedtuple_size=asizeof.asizeof(p)
dict_size=asizeof.asizeof(p._asdict())
gain=100 -namedtuple_size/dict_size*100
print(f"namedtuple:{namedtuple_size} bytes ({gain:.2f} % smaller)")
print(f"dict{dict_size} bytes")
