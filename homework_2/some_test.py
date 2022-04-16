from random import randint, sample, choice


line = []
items_set = 0
empty_cnt = 0

skip_items = sample(range(9), 4)

line = [randint(1, 90) for _ in range(9)]
print(line)

new_line = []

for i in range(9):
    if i not in skip_items:
        new_line.append(line[i])
    else:
        new_line.append("_")


print(line)
print(new_line)
print(skip_items)

# if items_set < 5 and empty_cnt < 4:
#     if choice([True, False]):
#         items_set += 1
#         line.append(randint(1, 90))
#     else:
#         empty_cnt += 1
#         line.append("_")
