import sys
n = int(sys.stdin.readline())

for q in range(n):
    temp = [sys.stdin.readline().split()[-1].lower() for x in range(4)]
    lastvowels = []
    for word in temp:
        for i in range(len(word)-1, -1, -1):
            if word[i] in ["a", "e", "i", "o", "u"]:
                lastvowels.append(i)
                break
            elif i == 0 and word not in ["a", "e", "i", "o", "u"]:
                lastvowels.append(0)
                break

    # print(temp)
    # print(lastvowels)
    if temp[0][lastvowels[0]:] == temp[1][lastvowels[1]:] == temp[2][lastvowels[2]:] == temp[3][lastvowels[3]:]:
        print("perfect")

    elif temp[0][lastvowels[0]:] == temp[1][lastvowels[1]:] and temp[2][lastvowels[2]:] == temp[3][lastvowels[3]:]:
        print("even")

    elif temp[0][lastvowels[0]:] == temp[2][lastvowels[2]:] and temp[1][lastvowels[1]:] == temp[3][lastvowels[3]:]:
        print("cross")

    elif temp[0][lastvowels[0]:] == temp[3][lastvowels[3]:] and temp[2][lastvowels[2]:] == temp[1][lastvowels[1]:]:
        print("shell")

    else:
        print("free")