# The lower limit of the user's search for prime numbers
i = int(input("Where do you want to start from? "))
# The upper limit of the user's search for prime numbers
stop = int(input("How far do you want to count up to? "))

# Does the destination file exist
exist = input('Does the destination file exist already? y/n ')
# Name of the destination file
fName = input("Where do you want to print the output? ")

# Edits or creates a file depending on the user's wishes
def openStream(exist, fName):
	if exist == "y" :
		return open(fName,"w")
	else :
		return open(fName,"x")

f = openStream(exist, fName)
check = True

# Looks for prime numbers till the given limit
while i < stop:
    # Because 2 is the only evan prime number this segment is specifically for it
	if stop > 2 and i == 2:
		f.write(str(i))
		f.write("\n")
		i += 1
	j = 2

	# Decides whether or not a number is prime
	while j < i:
		# If the number is not prime then this loops ends
		if  i % j == 0:
			check = False
			break
		j += 1

	# If the number is prime it's printed to the given file
	if check:
		f.write(str(i))
		f.write("\n")
	check = True
	i += 2

f.close()
