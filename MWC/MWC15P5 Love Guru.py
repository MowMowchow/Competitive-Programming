import sys
alphabet = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6",
            "g": "7", "h": "8", "i": "9", "j": "10", "k": "11", "l": "12",
            "m": "13", "n": "14", "o": "15", "p": "16", "q": "17", "r": "18",
            "s": "19", "t": "20", "u": "21", "v": "22", "w": "23", "x": "24", "y": "25", "z": "26"}

one = sys.stdin.readline().strip("\n").lower()
two = sys.stdin.readline().strip("\n").lower()
onetotal = 0
twototal = 0
cycles = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1], [0]]

for i in range(len(one)):
    cyclesindex = int(alphabet[one[i]][-1])  # which cycle the last letter is (ie r = 8)
    onetotal += (cycles[cyclesindex][((i+1) % len(cycles[cyclesindex]))-1]) % 10

for i in range(len(two)):
    cyclesindex = int(alphabet[two[i]][-1])  # which cycle the last letter is (ie r = 8)
    twototal += (cycles[cyclesindex][((i+1) % len(cycles[cyclesindex]))-1]) % 10

if onetotal % 10 == 0:
    onetotal = 10
else:
    onetotal = onetotal % 10
if twototal % 10 == 0:
    twototal = 10
else:
    twototal = twototal % 10

print(onetotal + twototal)