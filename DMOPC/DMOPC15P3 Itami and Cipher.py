string = input()
motto = input()
shift = 0
new = ""
alphabet = ["a","b","c","d","e","f","g","h","i","j","k",
           "l","m","n","o","p","q","r","s","t","u",
           "v","w","x","y","z"]
encrypted = True


while encrypted:
    for i in string:
        new += alphabet[alphabet.index(i) - shift]


    if motto in new:
        encrypted = False
        break


    shift +=1
    new = ""

print(shift)
print(new)