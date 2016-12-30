def isPrime (value):
	result = True		# assumes number is prime
	for i in range(2, value+1, 1):		# if proven to be not prime, make false
		if value%i == 0 and value != i:
			result = False
	return result

def reverse(number):
	count = 0
	string1 = str(number)	# converts number into a string
	string2 = str(number)
	length = len(string1)

	for i in range(-1, -length + 1, -1): # move backwards through string1
		string2[count] = string1[i]		 # puts reverse of string1 in string2
		count += 1
	return int(string2)		# converts back to an int


num = int(input("Please enter a positive number: "))
count = 0		# tracks number of emirps found
i = 2			# cycles through numbers to be tested

while count < num:
	if isPrime(i) and isPrime(reverse(i)):	# if num and reverse are prime			
		print(i, end = " ")					# print to screen
		count += 1							
		if count%5 == 0 and count != 0:		# prints only 5 numbers to each line
			print()
	i += 1