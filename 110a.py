# http://codeforces.com/problemset/problem/110/A

# Petya loves lucky numbers.
# We all know that lucky numbers are the positive integers whose decimal representations
# contain only the lucky digits 4 and 7.
# For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

# Unfortunately, not all numbers are lucky.
# Petya calls a number nearly lucky if the number of lucky digits in it is a lucky number.
# He wonders whether number n is a nearly lucky number

# Input
# The only line contains an integer n (1 ≤ n ≤ 10^18).
n = int(input())

is_n_nearly_lucky = False

n_list = list(str(n))

# check if the given number is nearly lucky by couting the lucky digits it has
lucky_digits_count = 0
for digit in n_list:
    if digit == '4' or digit == '7':
        lucky_digits_count += 1

# build lucky numbers up to the count
lucky_numbers = []
# Note that all lucky numbers are nearly lucky as any number is evenly divisible by itself, so the range goes up to lucky_digits_count+1
for i in range(0,lucky_digits_count+1):
    i_string = str(i)
    is_valid_lucky_number = True
    # check if all the digits of the number are either 4 o 7
    for char in i_string:
        if char not in ('47'):
            is_valid_lucky_number = False
            # the number is not valid, so no reason to keep looping
            break
    if is_valid_lucky_number:
        lucky_numbers.append(i)

# decide if it's a nearly lucky number
if lucky_digits_count in (lucky_numbers):
    is_n_nearly_lucky = True

# Output
# In the only line print "YES" (without the quotes), if number n is nearly lucky.
# Otherwise, print "NO" (without the quotes).
if is_n_nearly_lucky:
    print('YES')
else:
    print('NO')
