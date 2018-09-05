<?php

// http://codeforces.com/problemset/problem/158/A


// input
// The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space.
fscanf(STDIN, "%d %d", $n, $k);
// The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100), where ai is the score earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: ai ≥ ai + 1).

$scores_string = fgets(STDIN);

$a = explode(" ", trim($scores_string));

// "Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.
$quantity_that_will_advance = 0;
$kth_place_score = (int)$a[$k-1];
foreach ($a as $score)
{
	$score_int = (int)$score;
	if ( ( (int)$kth_place_score <= $score_int ) && $score_int )
		$quantity_that_will_advance++;
	else
		break;
}

// output
// the number of participants who advance to the next round.
echo "{$quantity_that_will_advance}";

?>