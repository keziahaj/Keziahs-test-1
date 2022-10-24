# if the letter

# Custom function
string = input(f'Enter a word')

def RepeatingFunc(string):
	char_order = []
	count = {}

	for x in string:
		if x in count:
			count[x] += 1
		else:
			count[x] = 1
			char_order.append(x)
	for x in char_order:
		if count[x] == 1:
			return x
	

print("First Non-Repeating Character = ",RepeatingFunc(string))