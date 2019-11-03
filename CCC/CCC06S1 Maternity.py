import sys
parenta = [x for x in sys.stdin.readline()]
parentb = [x for x in sys.stdin.readline()]


def finddom(parent, final):
    for gene in range(10): #for parent a
        if gene % 2 == 0:
            final.append([parent[gene], parent[gene+1]])

        if gene == 8:
            return final


a = finddom(parenta, [])
b = finddom(parentb, [])

n = int(sys.stdin.readline())


for q in range(n):
    child = [x for x in sys.stdin.readline().strip("\n")]
    possible = True


    for i in range(len(child)):
        if child[i].isupper():
            if child[i] in a[i] or child[i] in b[i]:
                pass
            else:
                possible = False

        elif child[i].islower():
            if child[i] in a[i] and child[i] in b[i]:
                pass
            else:
                possible = False

    if possible:
        print("Possible baby.")

    else:
        print("Not their baby!")
