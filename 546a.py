# http://codeforces.com/problemset/problem/546/A

# A soldier wants to buy w bananas in the shop.
# He has to pay k dollars for the first banana,
# 2k dollars for the second one and so on
# (in other words, he has to pay i·k dollars for the i-th banana).

# He has n dollars.
# How many dollars does he have to borrow from his friend soldier to buy w bananas?

# Input
# The first line contains three positive integers k, n, w (1  ≤  k, w  ≤  1000,0 ≤ n ≤ 10^9),
# the cost of the first banana, initial number of dollars the soldier has and number of bananas he wants.
k_cost_of_the_first_banana, n_initial_number_of_dollars_the_soldier_has, w_number_of_bananas_he_wants = list(map(int, input().split(' ')))

total_cost_of_bananas = 0

# calculate thje total cost of the bananas
for i in range(0,w_number_of_bananas_he_wants+1):
    total_cost_of_bananas += k_cost_of_the_first_banana * i

# calculate the difference between what he has to pay and what he has
amount_of_dollars_to_borrow = total_cost_of_bananas - n_initial_number_of_dollars_the_soldier_has

# If he doesn't have to borrow money, output 0.
if amount_of_dollars_to_borrow < 0:
    amount_of_dollars_to_borrow = 0

# Output
# Output one integer — the amount of dollars that the soldier must borrow from his friend.
print(amount_of_dollars_to_borrow)
