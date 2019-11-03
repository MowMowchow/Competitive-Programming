responses = []
answers = []
length = int(input())
correct = 0

for i in range(2*length):
    if i < length:
        responses.append(input())
    else:
        answers.append(input())

for i in range(length):
    if responses[i] == answers[i]:
        correct += 1

print(correct)