# https://codeforces.com/problemset/problem/580/A

# Kefa decided to make some money doing business on the Internet for exactly n days.
# He knows that on the i-th day (1 ≤ i ≤ n) he makes ai money. Kefa loves progress,
# that's why he wants to know the length of the maximum non-decreasing subsegment in sequence ai.
# Let us remind you that the subsegment of the sequence is its continuous fragment.
# A subsegment of numbers is called non-decreasing if all numbers in it follow in the non-decreasing order.

# Help Kefa cope with this task!

# Input
# The first line contains integer n (1 ≤ n ≤ 10^5).
n = int(input())

# The second line contains n integers a1,  a2,  ...,  an (1 ≤ ai ≤ 10^9).
a = list(map(int, input().split(' ')))

# (1 ≤ i ≤ n) so we start at 1 instead of 0:
length = 1

i = 0
current_length = 1
while i < len(a)-1:
    if a[i] <= a[i+1]:
        current_length += 1
        if current_length > length:
            length = current_length
    else:
        current_length = 1
    i += 1

# Output
# Print a single integer — the length of the maximum non-decreasing subsegment of sequence a.
print(length)
