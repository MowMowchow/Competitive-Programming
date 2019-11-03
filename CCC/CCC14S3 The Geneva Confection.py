testCases = int(input())
List = []

# Creates a nested list with each test case inside of the main list "List"
for x in range(testCases):
    List.append([])
    f = input()
    for y in range(int(f)):
        List[x].append(int(input()))

# For each test case
for x in range(testCases):
    # We need to store the location of the cars on the mountain, branch and the car we are looking for
    carList = List[x]
    branch = []
    current = 1

    while True:
        # First step:
        # If cars are on the mountin try to send them into the mountain
        if len(carList) > 0:

            # If the car on the mountain is the one we are looking for send it to the lake (remove from mountain)
            if carList[-1] == current:
                current += 1
                carList.pop();

            # Othwerwise see if there are any cars in the branch
            elif len(branch) > 0:
                # If there are cars on the branch see if they can be sent into the lake
                if branch[-1] == current:
                    current += 1
                    branch.pop()

                # Otherwise send the car from the mountain to the branch
                else:
                    branch.append(carList.pop())

            # Otherwise send the car from the mountain to the branch
            else:
                branch.append(carList.pop())

        # If there are no cars on the mountain see if there are any on the branch
        elif len(branch) > 0:
            if branch[-1] == current:  # If the cart on the branch can be moved into the lake do so
                current += 1
                branch.pop()
            else:  # Otherwise there is no way for us to complete the recipe
                print('N')
                break

        # If the mountain and the branch are empty then we are done!
        else:
            print('Y')
            break
