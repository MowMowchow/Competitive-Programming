import sys
numberofcollections = int(sys.stdin.readline().strip("\n"))

for q in range(numberofcollections):
    fixfree = True
    x = sys.stdin.readline()
    y = sys.stdin.readline()
    z = sys.stdin.readline()

    if x.startswith(y) or x.endswith(z):
        fixfree = False

    elif x.startswith(z) or x.endswith(y):
        fixfree = False

    elif y.startswith(z) or y.endswith(z):
        fixfree = False

    elif y.startswith(x) or y.endswith(x):
        fixfree = False

    elif z.startswith(x) or z.endswith(y):
        fixfree = False

    elif z.startswith(y) or z.endswith(x):
        fixfree = False


    if fixfree:
       print("Yes")

    else:
       print("No")