// http://codeforces.com/problemset/problem/116/A

// Input
// The first line contains a single number n (2 ≤ n ≤ 1000) — the number of the tram's stops. 
var n = parseInt(readline());


var a = [];
var b = [];
var aux;
var minimum = 0;
var passengers_inside = 0;

//Then n lines follows
for (var i = 0; i < n; i++)
{
	// each contains two integers ai and bi (0 ≤ ai, bi ≤ 1000) — the number of passengers
	// that exits the tram at the i-th stop, and the number of passengers that enter the tram
	// at the i-th stop. The stops are given from the first to the last stop in the order of
	// tram's movement.
	aux = readline().split(" ").map( function(x){return parseInt(x);});
	a.push(aux[0]);
	b[b.length] = aux[1];

	// even shorter solution:
	// passengers_inside += parseInt(aux[1]) - parseInt(aux[0]);
	passengers_inside += b[i] - a[i];

	if (passengers_inside > minimum)
		minimum = passengers_inside;
}


// Output: Print a single integer denoting the minimum possible capacity of the tram (0 is allowed).
print(minimum);