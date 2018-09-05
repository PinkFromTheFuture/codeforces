<?php

// Input
// Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.
$first_string = fgets(STDIN);
$second_string = fgets(STDIN);


// If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.

//initilize ouput
$result = 0;
// check if the are equal
if (stripos($first_string, $second_string) )
{
	$result = 0;
}
else
{
	// Now Petya wants to compare those two strings lexicographically.
	for ($i=0; $i < strlen($first_string); $i++)
	{ 
		if ( ord($first_string[$i])%32 != ord($second_string[$i])%32 )
		{
			if ( ord($first_string[$i])%32 < ord($second_string[$i])%32 )
				$result = -1;
			else
				$result = 1;
			// solution found. get out of the loop. 
			break;
		}
	}
}

// Output
echo $result;

?>