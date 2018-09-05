// http://codeforces.com/problemset/problem/266/A

//There are n stones on the table in a row, each of them can be red, green or blue. 

//Input
// The first line contains integer n (1 ≤ n ≤ 50) — the number of stones on the table.
var n = parseInt(readline());

//The next line contains string s, which represents the colors of the stones. We'll consider the stones in the row numbered from 1 to n from left to right. Then the i-th character s equals "R", if the i-th stone is red, "G", if it's green and "B", if it's blue.
var s = readline();

//Count the minimum number of stones to take from the table so that any two neighboring stones had different colors. Stones in a row are considered neighboring if there are no other stones between them.
var count = 0;

for (var i = 0; i<n-1; i++)
{
	if (s.charAt(i) == s.charAt(i+1))
	// if (s[i] == s[i])
		count++;
}

//Output: Print a single integer — the answer to the problem.
print(count);