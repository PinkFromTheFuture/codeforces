# https://codeforces.com/problemset/problem/337/A

# Input
# The first line contains space-separated integers n and m (2 ≤ n ≤ m ≤ 50).
n, m = map(int, input().split(' '))
# The second line contains m space-separated integers f1, f2, ..., fm (4 ≤ fi ≤ 1000) — the
# quantities of pieces in the puzzles sold in the shop.
f = list(map(int, input().split(' ')))

# order the list with the quantities of pieces in the puzzles
f.sort()

puzzles_to_discard = m - n

if puzzles_to_discard == 0:
	# there are no puzzles to discard
	least_possible_difference = f[-1] - f[0]
else:
	least_possible_difference = 999999
	i = 0
	while (i <= puzzles_to_discard):
		# print('checking f[n+i] - f[i]: {} - {} = {}'.format(f[n+i], f[i], f[n+i] - f[i]))
		difference_between_head_and_tail = f[n+i-1] - f[i]
		if difference_between_head_and_tail < least_possible_difference:
			least_possible_difference = difference_between_head_and_tail
		i += 1


# Output
# Print a single integer — the least possible difference the teacher can obtain.
print(least_possible_difference)
