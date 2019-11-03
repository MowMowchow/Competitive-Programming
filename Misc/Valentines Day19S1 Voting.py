import sys

n, m = [int(x) for x in sys.stdin.readline().strip("\n").split()]
candidates = [[sys.stdin.readline().strip("\n"), False, 0] for x in range(n)]
voters = []

def identifycandidate(candidate):
    for i in range(n):
        if candidate == candidates[i][0]:
            return i
    print("wtf")

for i in range(m):
    q = sys.stdin.readline().strip("\n").split()
    q[0] = int(q[0])
    temp = [identifycandidate(x) for x in q[1:]]
    add = [q[0]] + [False] + temp
    voters.append(add)
    # print(add)
# print(voters)

candidatesleft = n
while candidatesleft > 1:
    for person in voters:
        if len(person) > 2:
            if not candidates[person[2]][1]: # if candidate haven't been voted out yet
                if not person[1]: # if the person has not voted yet
                    candidates[person[2]][2] += 1
                    person[1] = True  # they have voted now

            elif candidates[person[2]][1]:  # the person has been voted out
                if len(person) > 2: # if they still have vote ideas left
                    while len(person) > 2:
                        if not candidates[person[2]][1]:
                            candidates[person[2]][2] += 1
                            person[1] = True  # they have voted now
                            break

                        else:
                            person.pop(2)
                            person[1] = False # reset their vote


    takeout = [float("inf"), 0]  # val, candidate
    for cand in range(n):
        if candidates[cand][2] < takeout[0] and not candidates[cand][1]:
            takeout = [candidates[cand][2], cand]

    candidates[takeout[1]][1] = True
    candidatesleft -= 1
    # print(candidates)

for i in candidates:
    if not i[1]:
        print(i[0])
        break