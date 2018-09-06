# http://codeforces.com/problemset/problem/281/A

# Capitalization is writing a word with its first letter as a capital letter.

# Input
# A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 10^3.
word = input()

# Your task is to capitalize the given word.
# Note, that during capitalization all the letters except the first one remains unchanged.
word = word[0].upper() + word[1:]

# Output
# Output the given word after capitalization.
print(word)
