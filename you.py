def change(text):
	array = text.split()

	for i in range(len(array)):
		if array[i] == "you":
			array[i] = "your sister"
		if len(array[i]) > 3:
			if array[i][:3] == "you" and list(set(array[i][3:]))[0] == "u":
				array[i] = "your sister"
	return ' '.join(array)			

print(change("you are your youuuuuuu youuuuhhg"))