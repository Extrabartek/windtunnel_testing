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

comb = list(itr.combinations_with_replacement(value_range_list, dice_count))
# print(comb)
good_comb_list = []
for combination in comb:
    if combination[0][1] > combination[1][0] and combination[0][0] < combination[1][1]:
        if combination[1][1] > combination[2][0] and combination[1][0] < combination[2][1]:
            if combination[2][1] > combination[3][0] and combination[2][0] < combination[3][1]:
                if combination[3][1] > combination[4][0] and combination[3][0] < combination[4][1]:
                    if combination[4][1] > combination[0][0] and combination[4][0] < combination[0][1]:
                        good_comb_list.append(combination)

print(len(value_range_list))
print(len(comb))
print(len(good_comb_list))
comb_count = 0

for combination in good_comb_list:
    i = min(abs(combination[0][1] - combination[1][0]), abs(combination[0][0] - combination[1][1]))
    i *= min(abs(combination[1][1] - combination[2][0]), abs(combination[1][0] - combination[2][1]))
    i *= min(abs(combination[2][1] - combination[3][0]), abs(combination[2][0] - combination[3][1]))
    i *= min(abs(combination[3][1] - combination[4][0]), abs(combination[3][0] - combination[4][1]))
    i *= min(abs(combination[4][1] - combination[0][0]), abs(combination[4][0] - combination[0][1]))
    comb_count += i

    # Obviously zero
    # for n_0 in range(combination[0][0], combination[0][1]):
    #   for n_1 in range(combination[1][0], combination[1][1]):
    #      if n_0 > n_1:
    #         for n_2 in range(combination[2][0], combination[2][1]):
    #            if n_1 > n_2:
    #               for n_3 in range(combination[3][0], combination[3][1]):
    #                   if n_2 > n_3:
    #                      for n_4 in range(combination[4][0], combination[4][1]):
    #                         if n_3 > n_4 > n_0:
    #                            comb_count += 1

print(comb_count)
