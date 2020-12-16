import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

N = input()

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

eprint(lines)

def is_suspect(compte):
    last_5 = compte[-5:]
    eprint(last_5)

    try:
        int(last_5)
    except:
        # Pas suspect
        return False
    return True

nb_suspect = 0
for line in lines:
    if is_suspect(line):
        nb_suspect += 1

print(nb_suspect)