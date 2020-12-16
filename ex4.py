import sys
from functools import reduce

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

N, M = tuple(map(int, input().split()))

cle = list(map(int, input().split()))

message = []
for line in sys.stdin:
    message.append(tuple(map(int, line.rstrip('\n').split())))

#eprint(cle)
#eprint(message)

cache = {}

def decrypt_message(octet):
    #eprint("Cle", cle)
    if octet in cache:
        return cache[octet]
    else:
        L, R = octet
        cle_part = cle[L:R+1]
        #eprint("Cle part", cle_part)
        xor = reduce(lambda i, j: int(i) ^ int(j), cle_part)
        #eprint(xor)
        cache[octet] = xor
        return xor

occurences = {}
for line in message:
    xor = decrypt_message(line)
    if xor in occurences:
        occurences[xor] += 1
    else:
        occurences[xor] = 1

#eprint(occurences)

results = []
for i in range(0, 256):
    if i in occurences:
        results.append((occurences[i]))
    else:
        results.append(0)

print(" ".join(map(str, results)))