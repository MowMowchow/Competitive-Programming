import sys
temp = sys.stdin.readline().strip("\n")
word = []
for letter in temp:
    word.append(letter)
total = []


def scramble(word, curr, length):
    if curr not in total and len(curr) == length:
        total.append(curr)
    if len(curr) < length:
        for letter in word: # don't append, concatate with the function call
            if letter not in curr:
                scramble(word, curr+[letter], length)

    else:
        return


for letter in word:  # what?
    scramble(word, [letter], len(word))
total.sort()

for word in total:
    print(''.join(word))