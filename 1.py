with open('./input.txt', 'r') as input_file:
	input = input_file.read()

a, b = input.split(' ');
print(float(a) + float(b))