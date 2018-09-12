# INPUT: You are given a rectangular board of M × N squares.
# In a single line you are given two integers M and N — board sizes in squares (1 ≤ M ≤ N ≤ 16).
M, N = map(int, input().split(' '))

# initialize output
maximal_number_of_dominoes = 0

# case 1 of 2: all of the numbers in the board dimensions are odd.
if ( (0 != M % 2) and (0 != N % 2) ):
    # (all columns except the last + only the last column) / 2. 2 is the linear size of the domino.
    maximal_number_of_dominoes = ( ((M-1)*N) + (N-1) )/2
# case 2 of 2: there is an even number in the board dimensions
else:
    maximal_number_of_dominoes = M*N/2

# Output one number — the maximal number of dominoes, which can be placed
print(int(maximal_number_of_dominoes))