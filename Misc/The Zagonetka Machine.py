import sys
n = int(sys.stdin.readline())
word = sys.stdin.readline().strip("\n")

def substrings(string):
    counter = 0
    length = len(string)
    alist = []
    for i in range(length):
        for j in range(i,length):
            case = string[i:j + 1]
            if word.startswith(case) and word.endswith(case):
                counter += 1

    return counter

print(substrings(word))