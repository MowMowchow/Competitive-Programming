import sys
#recurseive cause bigbrainmode and I felt like it


def binarySearch(first, last):
    if last >= first:

        mid = first + (last - first) // 2
        print(mid)
        sys.stdout.flush()
        check = sys.stdin.readline().strip("\n")


        if check == "OK":
            return

        elif check == "FLOATS":
            return binarySearch(first, mid - 1)


        elif check == "SINKS":
            return binarySearch(mid + 1, last)

    else:
        return -1

first = 1
last = 2*(10**9)
binarySearch(first, last)