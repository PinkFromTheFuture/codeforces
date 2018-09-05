<?php

// http://codeforces.com/problemset/problem/339/A

//Input: The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces. It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3. String s is at most 100 characters long.
$s = trim(fgets(STDIN));

// Rearrange the summans and print the sum in such a way that Xenia can calculate the sum.
$numbers = explode('+', $s);
sort($numbers);
$s = implode('+', $numbers);

// Output: Print the new sum that Xenia can count.
echo $s;
?>