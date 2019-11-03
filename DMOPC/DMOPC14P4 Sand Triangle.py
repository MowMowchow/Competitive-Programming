n = int(input())
previousrowleading = 0
previousrownumber = 1
i = 1
done = False
total = 0
if n == 1:
    print("1")

else:
    while not done:
        currentrownumber = i
        currentrowleading = previousrowleading + previousrownumber
        nextrowleading = currentrowleading + currentrownumber

        if currentrowleading < n < nextrowleading: #if the number is in the current row
            for i in range(currentrowleading, nextrowleading):
                #print(i)
                total += i
            done = True

        elif i > n:
            print("whut")
            break

        previousrownumber = i
        previousrowleading = currentrowleading
        i += 1

    print(total)