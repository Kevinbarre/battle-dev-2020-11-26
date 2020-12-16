import sys
from collections import Counter

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

cache = {}

def decrypt_message(octet):
    L, R = octet
    if L == R:
        return cle[L]

    if L in cache:
        cache_L = cache[L]
        if R in cache_L:
            return cache_L[R]
        else:
            M = int((L + R) / 2)
            result = decrypt_message((L, M))^decrypt_message((M+1, R))
            cache_L[R] = result
            return result
    else:
        M = int((L + R) / 2)
        result = decrypt_message((L, M))^decrypt_message((M+1, R))
        cache[L] = {R: result}
        return result

N, M = tuple(map(int, input().split()))

cle = list(map(int, input().split()))

message = []
for line in sys.stdin:
    message.append(tuple(map(int, line.rstrip('\n').split())))

counter = Counter(message)

sorted_counter = sorted(Counter(message), key=lambda octet: octet[1] - octet[0])

occurences = {}

for octet in sorted_counter:
    xor = decrypt_message(octet)
    if xor in occurences:
        occurences[xor] += counter[octet]
    else:
        occurences[xor] = counter[octet]

results = []
for i in range(0, 256):
    if i in occurences:
        results.append((occurences[i]))
    else:
        results.append(0)

#eprint(results)
print(" ".join(map(str, results)))