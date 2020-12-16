import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

N = int(input())
lines = []
for line in sys.stdin:
    lines.append(tuple(map(int, line.rstrip('\n').split())))

eprint(lines)

agents_by_level = {0 : 1}
while lines:
    A, B = lines.pop(0)
    eprint(A, B)
    # On ne connait pas encore A
    if A not in agents_by_level:
        # Si on connait B, alors A est le niveau en dessous
        if B in agents_by_level:
            agents_by_level[A] = agents_by_level[B] + 1
        else:
            # On ne connait pas encore B, on met A de côté pour l'instant
            lines.append((A, B))

eprint(agents_by_level)

from collections import Counter

counter = Counter(agents_by_level.values())
eprint(counter)

results = []
for i in range(1, 11):
    if i in counter:
        results.append((counter[i]))
    else:
        results.append(0)

print(" ".join(map(str, results)))