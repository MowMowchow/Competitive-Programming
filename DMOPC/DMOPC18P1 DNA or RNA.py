import sys
n = int(sys.stdin.readline())
seq = sys.stdin.readline().strip("\n")

dna = False
rna = False
both = False
neither = False

a = False
c = False
g = False
t = False
u = False

for base in seq:

    if base == "T":
        t = True

    elif base == "U":
        u = True

    elif base == "A":
        a = True

    elif base == "C":
        c = True

    elif base == "G":
        g = True

    else:
        neither = True
        print("neither")
        break


if not neither:
    if t and u:
        print("neither")
    elif not t and not u:
        print("both")
    elif t:
        print("DNA")
    elif u:
        print("RNA")