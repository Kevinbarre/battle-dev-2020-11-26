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
threshold = 5

def decrypt_message_naive(octet):
    L, R = octet
    cle_part = cle[L:R+1]
    #eprint("Cle part", cle_part)
    xor = reduce(lambda i, j: int(i) ^ int(j), cle_part)
    #eprint(xor)
    return xor

def decrypt_message(octet):
    #eprint("Cle", cle)
    #eprint(cache)
    L, R = octet
    if L == R:
        return cle[L]

    if L in cache:
        cache_L = cache[L]
        if R in cache_L:
            return cache_L[R]
        else:
            if R - L < threshold:
                result = decrypt_message_naive((L, R))
            else:
                M = int((L + R) / 2)
                result = decrypt_message((L, M))^decrypt_message((M+1, R))
            cache_L[R] = result
            return result
    else:
        if R - L < threshold:
            result = decrypt_message_naive((L, R))
        else:
            M = int((L + R) / 2)
            result = decrypt_message((L, M))^decrypt_message((M+1, R))
        cache[L] = {R: result}
        return result

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