import sys
from collections import Counter


def create(strr):
    if "+" in strr:
        first, last = strr.split("@")
        first = "".join([char for char in first if char != "."])
        plusindex = first.index("+")
        new = str(first[:plusindex] + "@" + last)
    else:
        first, last = strr.split("@")
        first = "".join([char for char in first if char != "."])
        new = first + "@" + last

    new = new.lower()
    return new


for q in range(10):
    n = int(sys.stdin.readline())
    distinct = []
    for qq in range(n):
        temp = sys.stdin.readline().strip("\n")
        curr = create(temp)
        distinct.append(curr)
    print(len(Counter(distinct).keys()))