import sys
from functools import reduce
from operator import xor

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

N, M = tuple(map(int, input().split()))

cle = list(map(int, input().split()))

message = []
for line in sys.stdin:
    message.append(tuple(map(int, line.rstrip('\n').split())))

results = [0 for i in range(256)]

cache = {}

for L, R in message:
    if L in cache:
        cache_L = cache[L]
    result = reduce(xor, map(int, cle[L: R+1]))
    results[result] += 1


#eprint(results)
print(" ".join(map(str, results)))