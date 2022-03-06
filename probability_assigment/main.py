import numpy as np
import itertools as itr

low = 0
high = 9
sides = 6
dice_count = 5

value_range_list = []
value_range = []

for i in range(high + 1):
    for j in range(high + 1):
        if i >= j:
            value_range = [j, i]
            value_range_list.append(value_range)

# print(value_range_list)
# print(len(value_range_list))

comb = list(itr.combinations(value_range_list, dice_count))
# print(comb)
good_comb_list = []
for combination in comb:
    if combination[0][1] > combination[1][0] and combination[0][0] < combination[1][1]:
        if combination[1][1] > combination[2][0] and combination[1][0] < combination[2][1]:
            if combination[2][1] > combination[3][0] and combination[2][0] < combination[3][1]:
                if combination[3][1] > combination[4][0] and combination[3][0] < combination[4][1]:
                    if combination[4][1] > combination[0][0] and combination[4][0] < combination[0][1]:
                        good_comb_list.append(combination)

print(len(comb))
print(len(good_comb_list))







