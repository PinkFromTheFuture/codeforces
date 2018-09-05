<?php

// INPUT
// The first input line contains a non-empty string consisting of characters "0" and "1", which represents players. The length of the string does not exceed 100 characters. There's at least one player from each team present on the field.
$players_string = fgets(STDIN);

// // sollution using functions (62 ms, 500 KB):
// if ( false === strpos($players_string, '0000000') && false === strpos($players_string, '1111111') )
// 	$output_string = 'NO';
// else
// 	$output_string = 'YES';

// hand made solution (60 ms, 500 KB):
// warning counter must be less than 7. if it's seven, than the answer is yes.
$warning_counter = 1;
$output_string = 'NO';
for ($i=1; $i < strlen($players_string) ; $i++)
{ 
	if ($players_string[$i-1] == $players_string[$i])
	{
		$warning_counter++;
		if ($warning_counter == 7)
		{	
			$output_string = 'YES';
			break;
		}
	}
	else
	{
		$warning_counter = 1;
	}
}

// Output
// Print "YES" if the situation is dangerous. Otherwise, print "NO".
echo $output_string;

?>

