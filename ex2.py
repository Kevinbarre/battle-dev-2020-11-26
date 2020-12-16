import sys

from datetime import time

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

N = input()
lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

eprint(lines)

debut = time.fromisoformat("20:00")
fin = time.fromisoformat("07:59")

def is_suspect(hour):
    return debut <= hour or hour <= fin

nb_suspect = 0
nb_clean = 0
for line in lines:
    if is_suspect(time.fromisoformat(line)):
        nb_suspect += 1
    else:
        nb_clean += 1

eprint(is_suspect(time.fromisoformat("23:00")))

if nb_suspect > nb_clean:
    print("SUSPICIOUS")
else:
    print("OK")