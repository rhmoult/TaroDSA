import pdb
def pair_sum(myArray, target):
    myDict = {}
    for index, element in enumerate(myArray):
        if element not in myDict:
            myDict[element] = index
        complement = target - element
        if complement in myDict:
            return (myDict[complement], index)


if __name__ == "__main__":
    theArray = [3, 2, 5, 4, 1]
    theTarget = 8
    print(pair_sum(theArray, theTarget))
