// http://codeforces.com/problemset/problem/131/A

//Input: The first line of the input data contains a word consisting of uppercase and lowercase Latin letters. The word's length is from 1 to 100 characters, inclusive.
var word = readline();

var caps = 0;

// case where it's all CAPS
if ( 97 > word.charCodeAt(0))
{
	caps++;
	for (var i = 1; i < word.length; i++)
	{
		if (97 > word.charCodeAt(i))
			caps++;
	}

	if (caps == word.length)
		word = word.toLowerCase();
}
// case where the first is not caps but the rest is
else
{
	for (var i = 1; i < word.length; i++)
	{
		if (97 > word.charCodeAt(i))
			caps++;
	}

	if (caps == word.length-1)
		word = word.substr(0,1).toUpperCase() + word.substr(1,word.length-1).toLowerCase();
}

//Output: Print the result of the given word's processing.
print(word);
