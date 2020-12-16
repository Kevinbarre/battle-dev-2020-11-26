import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

N, M = tuple(map(int, input().split()))

cle = list(map(int, input().split()))

message = []
for line in sys.stdin:
    message.append(tuple(map(int, line.rstrip('\n').split())))

precalc = [0]

for elem in cle:
    precalc.append(precalc[-1]^elem)

eprint(precalc)

results = [0 for _ in range(256)]

for octet in message:
    L, R = octet
    result = precalc[R+1] ^ precalc[L]
    results[result] += 1

print(*results)
# precalc(r+1) ^ precalc(l)

# 11 22 33 44 55
# 1 3
# 0 1
# 2 2
# 2 4

# precalc
# 0
# 11
# 11 22
# 11 22 33
# 11 22 33 44
# 11 22 33 44 55

# 1 3 -> 22 33 44 -> 11 22 33 44 ^ 11
# 0 1 -> 11 22  -> 11 ^ 22
# 2 2 -> 33 -> 11 22 33 ^ 11 22
# 2 4 -> 33 44 55 -> 11 22 33 44 55 ^ 11 22