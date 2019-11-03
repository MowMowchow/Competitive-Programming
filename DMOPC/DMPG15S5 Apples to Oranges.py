import sys
sys.setrecursionlimit(1000000)
n, m = [int(x) for x in sys.stdin.readline().split()]
adj = {}
answers = {}
for i in range(n):
    temp = sys.stdin.readline().strip("\n")
    adj[temp] = []
    answers[temp] = 0
for i in range(m):
    a, b, c = sys.stdin.readline().strip("\n").split()
    c = float(c)
    adj[a].append([b, c])


def dfs(curr):
    if curr == 'APPLES' and answers[curr] > 1.1:
        return True

    else:
        for nextfruit, cost in adj[curr]:
            if answers[curr]*cost > answers[nextfruit]:
                answers[nextfruit] = answers[curr]*cost
                result = dfs(nextfruit)
                if result:
                    return True


answers['APPLES'] = 1
ans = dfs('APPLES')

if ans:
    print("YA")
else:
    print("NAW")