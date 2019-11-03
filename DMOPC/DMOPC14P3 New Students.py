import sys

numberofinitialstudents = int(sys.stdin.readline())
students = []
for i in range(numberofinitialstudents):
    students.append(int(sys.stdin.readline()))
numberofnewstudents = int(sys.stdin.readline())
newstudents = []
for i in range(numberofnewstudents):
    newstudents.append(int(sys.stdin.readline()))

# dp pls
total = sum(students)
for newstudent in newstudents:
    students.append(newstudent)

    total += students[-1]

    print(round(total / len(students), 3))