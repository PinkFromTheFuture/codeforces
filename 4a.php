<?php

// http://codeforces.com/problemset/problem/4/A

// The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.
fscanf(STDIN, "%d", $w);

// if a number is odd it can't be divided by two even numbers. 2 is the only even that would be an exception
if ( (0 == $w % 2) && (2 != $w) )
	echo "YES";
else
	echo "NO";

?>