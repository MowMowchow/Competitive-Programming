bolean = input()
boleans = bolean.split(" ")
counter = 0

for i in boleans:
    if i == "not":
        counter += 1

if counter % 2 == 1:
    if boleans[-1] == "True":
        print("False")
    elif boleans[-1] == "False":
        print("True")

elif counter % 2 == 0:
    if boleans[-1] == "True":
        print("True")
    elif boleans[-1] == "False":
        print("False")