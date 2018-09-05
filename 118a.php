<?php 

// http://codeforces.com/problemset/problem/118/A

// INPUT - reads a line from he standard input
$given_string = trim(fgets(STDIN));
// fscanf(STDIN, "%s", $given_string);

// in the given string, consisting if uppercase and lowercase Latin letters, it:
// deletes all the vowels,
$vowels = ["a", "e", "i", "o", "u", "y" , "A", "E", "I", "O", "U", "Y"];
$given_string = str_replace($vowels, "", $given_string);

for ($i=strlen($given_string)-1; $i >= 0; $i--)
{
	// replaces all uppercase consonants with corresponding lowercase ones.
	if (ord($given_string[$i]) < 97)
		$given_string[($i*2)+1] = chr(ord($given_string[$i])+32); 
	else
		$given_string[($i*2)+1] = $given_string[$i];

	// inserts a character "." before each consonant,
	$given_string[($i*2)] = '.'; 
}

// OUTPUT
echo $given_string;

?>