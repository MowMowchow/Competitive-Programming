import sys
seq = [int(x) for x in sys.stdin.readline().split()]

if 0 not in seq:
    print("NO")

else:
    foundtotal = 0
    for i in seq:
        count = 0
        curr = i-1
        currvalid = False
        while count < 3:
            if seq[curr] != 0:
                curr = seq[curr]-1

            else:
                currvalid = True
                break

            count += 1

        if currvalid:
            foundtotal += 1

    if foundtotal == 3:
        print("YES")
    else:
        print("NO")