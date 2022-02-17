import sys
input = sys.stdin.readline

T = int(input())

while T:
  Nbase = int(input())
  baseArr = [int(x) for x in input().split()]
  total = 0

  def calc(N):
    cnt = 0
    for num in arr:
      if num == 0:
        cnt += 1

    return (N-cnt) + cnt*2


  for subSeg in range(1, Nbase+1):
    for offset in range(Nbase-subSeg+1):
      tempAns = -float("inf")
      arr = baseArr[offset:offset+subSeg]
      total += calc(subSeg)

  print(total)

  T -= 1