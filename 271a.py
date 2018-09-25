# https://codeforces.com/problemset/problem/271/A

# It seems like the year of 2013 came only yesterday.
# Do you know a curious fact? The year of 2013 is the first year after the old 1987 with only distinct digits.

# Now you are suggested to solve the following problem: given a year number,
# find the minimum year number which is strictly larger than the given one and has only distinct digits.

# Input
# The single line contains integer y (1000 ≤ y ≤ 9000) — the year number.
year_number = int(input())

is_strictly_larger = False
while not is_strictly_larger:
    # get the next number and analyse it
    year_number += 1

    # we will need to transform into a string to get the length
    year_number_string = str(year_number)

    # all the elements in a set are unique
    year_number_set = set(year_number_string)

    # when we made a set of the digits, if one was repeated the length will be smaller.
    if len(year_number_string) == len(year_number_set):
        # if the lengths before and after are the same, it means that we found a strict larger number
        is_strictly_larger = True

# Output
# Print a single integer — the minimum year number that is strictly larger than
# y and all it'sdigits are distinct. It is guaranteed that the answer exists.
print(year_number)
