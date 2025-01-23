def pair_sum(myArray, target):
    prev_numbers = {}
    for index, element in enumerate(myArray):
        if element not in prev_numbers:
            prev_numbers[element] = index
        complement = target - element
        if complement in prev_numbers:
            return (prev_numbers[complement], index)


if __name__ == "__main__":
    theArray = [3, 2, 5, 4, 1]
    theTarget = 8
    print(pair_sum(theArray, theTarget))
