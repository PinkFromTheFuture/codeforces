<?php


// Input
//The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 10^9).

fscanf(STDIN, "%d %d %d\n", $n, $m, $a); // reads number from STDIN
//echo "{$n}, {$m}, {$a}";




$quantity_of_vertical_flagstones = ceil( $n / $a );
$quantity_of_horizontal_flagstones = ceil( $m / $a) ;
// echo "{$quantity_of_vertical_flagstones}\n";
// echo "{$quantity_of_horizontal_flagstones}\n";

$needed_number_of_flagstones = $quantity_of_vertical_flagstones * $quantity_of_horizontal_flagstones;

echo number_format($needed_number_of_flagstones, 0, '', '');

?>