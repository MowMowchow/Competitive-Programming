import sys
t = int(sys.stdin.readline())

def calc(n):
    return (n*(n+1))//2


def binsearch(m):
    left = 0
    right = m
    index = 0

    while left <= right:
        index = left+(right-left)//2
        curr = calc(index)
        if curr < m:
            left = index+1
        elif curr >= m:
            right = index-1

    return left

for i in range(t):
    q = int(sys.stdin.readline())
    print(binsearch(q)+1)