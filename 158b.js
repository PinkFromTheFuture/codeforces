// http://codeforces.com/problemset/problem/158/B

// Input :The first line contains integer n (1 ≤ n ≤ 105) — the number of groups of schoolchildren. The second line contains a sequence of integers s1, s2, ..., sn (1 ≤ si ≤ 4). The integers are separated by a space, si is the number of children in the i-th group.
// read n
var n = readline("\n");

// read s

// var s_array = readline().split(" ").map(function(x) { return parseInt(x); });
var s_array = readline().split(" ");

var taxi_count = 0;
var one = 0;
var two = 0;
var three = 0;
var four = 0;

// count the groups
for (var i = 0; i < n; i++)
{
	// if (s_array[i][0] == '4')
	// {
	// 	four++;
	// }
	// else
	// {
	// 	if (s_array[i][0] == '4')
	// 	{
	// 		four++;
	// 	}
	// }
	switch (s_array[i][0])
	{
		case '1': one++;	break;
		case '2': two++;	break;
		case '3': three++;	break;
		case '4': four++;	break;
		default:			break;
	}
}

// count the number of taxis
taxi_count = four;
if (0 == two%2)
{
	taxi_count = taxi_count + (two/2);
}
else
{
	taxi_count = taxi_count + ((two+1)/2);
	// there are two remaining spots:
	if (0 < one)
	{
		one--;
	}
	if (0 < one)
	{
		one--;
	}
}
taxi_count+=three;
// fit alone people in the taxis with the groups of threes
while(0 < one && 0 < three)
{
	one--;
	three--;
}
taxi_count+=Math.ceil(one/4);

//Output: Print the single number — the minimum number of taxis necessary to drive all children to Polycarpus.
print(taxi_count);