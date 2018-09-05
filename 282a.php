<?php
// http://codeforces.com/problemset/problem/282/A

// Input
// The first line contains a single integer n (1 ≤ n ≤ 150) — the number of statements in the programme.
$n = fgets(STDIN);

// The language is that peculiar as it has exactly one variable, called x. 
$x = 0;

// Next n lines contain a statement each. Each statement contains exactly one operation (++ or --) and exactly one variable x (denoted as letter «X»). Thus, there are no empty statements. The operation and the variable can be written in any order.
for ($i=0; $i < $n; $i++)
{ 
	$operation = rtrim(fgets(STDIN));

	if (false !== strpos($operation, '++'))
		$x++;
	else
		$x--;
}

echo $x;

?>