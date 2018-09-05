<?php
// http://codeforces.com/problemset/problem/231/A

// initialize answer
$number_of_problems_to_implement = 0;

// INPUT
// The first input line contains a single integer n (1 ≤ n ≤ 1000) — the number of problems in the contest. 
fscanf(STDIN, "%d", $n);

// Then n lines contain three integers each.
for ($i=0; $i < $n; $i++)
{ 
	// The numbers on the lines are separated by spaces. Each integer is either 0 or 1
	fscanf(STDIN, "%d %d %d", $integers_matrix[$i][0], $integers_matrix[$i][1], $integers_matrix[$i][2] );

	// If the first number in the line equals 1, then Petya is sure about the problem's solution, otherwise he isn't sure. The second number shows Vasya's view on the solution, the third number shows Tonya's view.

	// they will implement a problem if at least two of them are sure about the solution. Otherwise, the friends won't write the problem's solution:
	if
	(	( 1 == $integers_matrix[$i][0] && 1 == $integers_matrix[$i][1] ) 
	||	( 1 == $integers_matrix[$i][0] && 1 == $integers_matrix[$i][2] ) 
	||	( 1 == $integers_matrix[$i][1] && 1 == $integers_matrix[$i][2] )
	)
	{
		$number_of_problems_to_implement++;
	}

}



//Output: Print a single integer — the number of problems the friends will implement on the contest.
echo $number_of_problems_to_implement;

?>