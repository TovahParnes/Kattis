text = input()
split = list(text)

correct = False

for i in range(len(split)):
    if (split[i] == "(" and split[-i - 1] == ")"):
        print("correct")
        correct = True

if not correct:
    print("fix")
