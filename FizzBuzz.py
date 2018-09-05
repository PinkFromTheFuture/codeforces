#Problem: http://rosettacode.org/wiki/FizzBuzz

# made for python 3:

dictionary = {
    3: "Fizz",
    5: "Buzz"
}

for i in range(1,100):
	output_string = ""

	for number, word in dictionary.items():
		if 0 == i % number:
			output_string += word

	if "" == output_string:
		output_string = i

	print(output_string)