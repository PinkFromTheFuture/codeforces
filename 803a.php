<?php

// Educational Codeforces Round 20
// http://codeforces.com/contest/803/problem/A


// Input
// The first line consists of two numbers n and k (1 ≤ n ≤ 100, 0 ≤ k ≤ 106).
fscanf(STDIN, "%d %d", $n, $k);

for ($row=0; $row < $n; $row++)
{ 
	for ($col=0; $col < $n; $col++)
	{ 
		$matrix[$row][$col] = 0;
	}
}

// if ( ( $k > $n*$n ) || ( (1 == $k % 2 ) && ($k > ($n*($n-1)+1)) ) )
if ( $k > $n*$n )
{
	// Output
	// If the answer exists then output resulting matrix. Otherwise output -1.
	echo -1;
	return;
}
else
{
	for ($row = 0; $row < $n; $row++)
	{
	    if ($k > 0)
	    {
	        $matrix[$row][$row] = 1;
	        $k--;
	    }
	    for ($col = $row + 1; $col < $n; $col++)
	    {
	        if ($k > 1)
	        {
	            $matrix[$row][$col] = 1;
	            $matrix[$col][$row] = 1;
	            $k -= 2;
	        }
	    }
	}

	// Output
	// If the answer exists then output resulting matrix. Otherwise output -1.
	for ($row=0; $row < $n; $row++)
	{ 
		for ($col=0; $col < $n; $col++)
		{ 
			echo "{$matrix[$row][$col]} ";
		}
		echo "\n";
	}	
}

?>