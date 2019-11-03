import sys
numberofpies = int(sys.stdin.readline())
numberofpeople = int(sys.stdin.readline())
dp = [[[-1 for x in range(numberofpies+1)] for x in range(numberofpies+1)] for x in range(numberofpies+1)]

def pi(currentperson, piesleft, prev):
    #this first if statement is inefficient and can be fixed
    # with editing the for loop's range for the recursion
    if dp[currentperson][piesleft][prev] == -1:

        if currentperson == piesleft:
            return 1

        if currentperson == 1:
            return 1

        else:
            sum = 0 #is 1 becaues each case is valid
            for case in range(prev, int((piesleft/currentperson))+1):
                sum += pi(currentperson-1, piesleft-case, case)

            dp[currentperson][piesleft][prev] = sum

    return dp[currentperson][piesleft][prev]


print(pi(numberofpeople, numberofpies, 1))