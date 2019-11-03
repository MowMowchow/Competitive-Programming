import sys
numberofslides = int(sys.stdin.readline())
slides = [[] for x in range(numberofslides+1)]
paths = [0 for x in range(numberofslides+1)]
while True:
    slide = sys.stdin.readline().split()
    slide = [int(x) for x in slide]
    if slide[0] == 0 and slide[1] == 0:
        break
    else:
        slides[slide[0]].append(slide[1])


def slidethrough(currentpoint):
    if currentpoint == numberofslides:
        return 1
    elif paths[currentpoint] != 0:
        return paths[currentpoint]

    else:
        for i in slides[currentpoint]:
            result = slidethrough(i)
            paths[currentpoint] += result

    return paths[currentpoint]



print(slidethrough(1))