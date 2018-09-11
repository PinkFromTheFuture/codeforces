# http://codeforces.com/problemset/problem/266/B


# Input
# The first line contains two integers n and t (1 ≤ n, t ≤ 50),
# which represent the number of children in the queue
# and the time after which the queue will transform into the arrangement you need to find.
number_of_children_in_the_queue, time_after_which_the_queue_will_transform_into_the_arrangement = map(int, input().split(' '))
# The next line contains string s, which represents the schoolchildren's initial arrangement.
# If the i-th position in the queue contains a boy, then the i-th character of string s equals "B",
# otherwise the i-th character equals "G".
queue_string = input()

# convert the string to a list, so we can manipulate it
queue_list = list(queue_string)

for time in range(0,time_after_which_the_queue_will_transform_into_the_arrangement):
    i = 0
    while (i < number_of_children_in_the_queue-1):
        if queue_list[i] == 'B' and queue_list[i+1] == 'G':
            # swap the boy and the girl
            queue_list[i] = 'G'
            queue_list[i+1] = 'B'
            # jump a child to don't analyse it twice
            i += 2
        else:
            i += 1

# convert the list back into a string so we can print it
final_queue = "".join(queue_list)

# Output
# Print string a, which describes the arrangement after t seconds.
# If the i-th position has a boy after the needed time, then the i-th character a must equal "B", otherwise it must equal "G".
print(final_queue)
