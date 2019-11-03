t = int(input())

def find(a, b, n):
    if n % a == 0 or n % b == 0:
        return True

    for currval1 in range(1, n+1):
        if currval1 % a == 0:
            if (n-currval1) % b == 0:
                return True

        elif currval1%b == 0:
            if (n-currval1) % a == 0:
                return True

for i in range(t):
    a, b, n = [int(x) for x in input().split()]
    if find(a, b, n):
        print("YES")
    else:
        print("NO")