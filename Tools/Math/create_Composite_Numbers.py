# Creates a list of composite Numbers

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

# Looks for composite numbers till the given limit
while i < stop:
	# Because 2 is the only even prime number this segment is specifically for it
	if i != 2:
		if i == 0:
			f.write(str(i)+"\n")
			
		elif i == 1:
			f.write(str(i)+"\n")
		elif i % 2 == 0:
			f.write(str(i)+"\n")
		elif i % 3== 0 and i != 3:
			f.write(str(i)+"\n")
		elif i % 5== 0 and i != 5:
			f.write(str(i)+"\n")
		elif i % 7 == 0 and i != 7:
			f.write(str(i)+"\n")
	i += 1
f.close()
