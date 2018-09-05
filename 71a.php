<?php
// http://codeforces.com/problemset/problem/71/A

//The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.
fscanf(STDIN, "%d", $n);

for ($i=0; $i < $n; $i++)
{
	fscanf(STDIN, "%s", $words_array[] );
}


// This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.
// Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".
foreach ($words_array as $i => $word)
{
	$word_length = strlen($word);
	if ( 10 < $word_length )
	{
		$words_array[$i] = $word[0] . ($word_length-2) . $word[$word_length-1];
	}
	
}

// outputs one word per line:
foreach($words_array as $word)
{
	echo "{$word}\n";
}

?>