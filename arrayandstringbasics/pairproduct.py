def pair_product(theArray, theTarget):
	if len(theArray) < 2:
		return None
	prev_numbers = {} 
	for index in range(0,len(theArray)):
		complement = theTarget / theArray[index]
		if complement in prev_numbers:
			return (prev_numbers[complement], index)
		prev_numbers[theArray[index]] = index

if __name__ == '__main__':
  myArray = [4,7,9,2,5,1]
  myTarget = 35
  print(pair_product(myArray, myTarget))
