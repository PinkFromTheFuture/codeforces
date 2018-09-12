# http://codeforces.com/problemset/problem/58/A


# Vasya has recently learned to type and log on to the Internet.
# He immediately entered a chat room and decided to say hello to everybody.
# Vasya typed the word s.
# It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello".
# For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello,
# and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello.
# Determine whether Vasya managed to say hello by the given word s.

# Input
# The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.
s = input()

hello_string = 'hello'
hello_iterator = 0
s_iterator = 0

while (s_iterator < len(s) and hello_iterator < len(hello_string)):
    if hello_string[hello_iterator] == s[s_iterator]:
        # if a letter is found, step to the next letter of the word hello
        hello_iterator += 1

    # continue iterating through s
    s_iterator += 1

# Output
# If Vasya managed to say hello, print "YES", otherwise print "NO".
if hello_iterator == len(hello_string):
    print('YES')
else:
    print('NO')


