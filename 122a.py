# http://codeforces.com/problemset/problem/122/A

# Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers
# whose decimal representation contains only the lucky digits 4 and 7.
# For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

# Petya calls a number almost lucky if it could be evenly divided by some lucky number.
# Help him find out if the given number n is almost lucky.

# Input
# The single line contains an integer n (1 ≤ n ≤ 1000) — the number that needs to be checked.
n = int(input())

is_n_almost_lucky = False


# build lucky numbers up to n
lucky_numbers = []
# Note that all lucky numbers are almost lucky as any number is evenly divisible by itself, so the range goes up to n+1
for i in range(0,n+1):
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

# check if the given number is almost lucky by looking for an even division
# with the lucky numbers smaller than the given number
for lucky_number in lucky_numbers:
    if n % lucky_number == 0:
        is_n_almost_lucky = True
        # we found out that it is almost lucky, so no reason to keep looping
        break

# Output
# In the only line print "YES" (without the quotes), if number n is almost lucky.
# Otherwise, print "NO" (without the quotes).
if is_n_almost_lucky:
    print('YES')
else:
    print('NO')
