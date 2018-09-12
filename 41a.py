# https://codeforces.com/problemset/problem/41/A

# The translation from the Berland language into the Birland language is not an easy task.
# Those languages are very similar: a berlandish word differs from a birlandish word with
# the same meaning a little: it is spelled (and pronounced) reversely.
# For example, a Berlandish word code corresponds to a Birlandish word edoc.
# However, it's easy to make a mistake during the «translation».
# Vasya translated word s from Berlandish into Birlandish as t.
# Help him: find out if he translated the word correctly.

# Input
# The first line contains word s, the second line contains word t.
# The words consist of lowercase Latin letters. The input data do not consist unnecessary spaces.
# The words are not empty and their lengths do not exceed 100 symbols.
s = input()
t = input()

t_is_s = True

# eliminate words of different legths

if len(s) == len(t):
    head = 0
    tail = len(t)
    while(head < len(s)):
        if s[head] != t[tail-1]:
            t_is_s = False
            # they are different, so the words don't match and there is no reason to keep looping
            break
        else:
            head += 1
            tail -= 1
else:
    t_is_s = False

# Output
# If the word t is a word s, written reversely, print YES, otherwise print NO.
if t_is_s:
    print('YES')
else:
    print('NO')
