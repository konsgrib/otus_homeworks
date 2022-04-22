from random import randint, sample, shuffle

rands = [i for i in range(1, 91)]
shuffle(rands)
print(rands)


for i in range(3):
    line = []
    for i in range(9):
        print("i", i)
        line.append(rands.pop())
    line = sorted(line)
    print(line)
