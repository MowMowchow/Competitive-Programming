import sys
n = int(sys.stdin.readline())
villages = [int(sys.stdin.readline()) for x in range(n)]
villages.sort()
dist = [0 for x in range(n)]
dist[0], dist[n-1] = float("inf"), float("inf")

for i in range(1, n-1):
    dist[i] += ((villages[i]-villages[i-1])/2) + ((villages[i+1]-villages[i])/2)

print(min(dist))