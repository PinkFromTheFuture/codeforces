# http://codeforces.com/problemset/problem/1040/A

# A group of n dancers rehearses a performance for the closing ceremony.
# The dancers are arranged in a row, they've studied their dancing moves and can't change positions.
# For some of them, a white dancing suit is already bought, for some of them — a black one, and for the rest the suit will be bought in the future.

# On the day when the suits were to be bought, the director was told that the participants
# of the olympiad will be happy if the colors of the suits on the scene will form a palindrome.
# A palindrome is a sequence that is the same when read from left to right and when read from right to left.
# The director liked the idea, and she wants to buy suits so that the color of the leftmost dancer's
# suit is the same as the color of the rightmost dancer's suit, the 2nd left is the same as 2nd right, and so on.

# The director knows how many burls it costs to buy a white suit, and how many burls to buy a black suit.
# You need to find out whether it is possible to buy suits to form a palindrome, and if it's possible,
# what's the minimal cost of doing so. Remember that dancers can not change positions,
# and due to bureaucratic reasons it is not allowed to buy new suits for the dancers who already have suits,
# even if it reduces the overall spending.

# Input
# The first line contains three integers n, a, and b( 1 ≤ n ≤ 20 ,  1 ≤ a , b ≤ 100 ) — the number of dancers, the cost of a white suit, and the cost of a black suit.
n, a, b = map(int,input().split())

# The next line contains n numbers ci, i-th of which denotes the color of the suit of the i-th dancer.
# Number 0 denotes the white color, 1 — the black color, and 2 denotes that a suit for this dancer is still to be bought.
c = list(map(int,input().split()))


minimal_price = 0
is_forming_a_palindrome_possible = False

for i in range(n//2):
    if c[i] == c[n-i-1] and c[i] != 2:
        continue
    elif (c[i] == 0 and c[n-i-1] == 2) or (c[i] == 2 and c[n-i-1] == 0):
        minimal_price += a
    elif (c[i] == 2 and c[n-i-1] == 1) or (c[i] == 1 and c[n-i-1] == 2):
        minimal_price += b
    elif c[i] == 2 and c[n-i-1] == 2:
        minimal_price += (2*min(a,b))
    else:
        is_forming_a_palindrome_possible = True
        break

# Output
# If it is not possible to form a palindrome without swapping dancers and buying new suits for those who have one,
# then output -1. Otherwise, output the minimal price to get the desired visual effect.
if is_forming_a_palindrome_possible == True:
    print('-1')
else:
    if n%2==1 and c[n//2] == 2:
        minimal_price += min(a,b)
    print(minimal_price)