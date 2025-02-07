# Time Complexity: O(n)
# Space Complexity: O(n)
def pair_sum(myArray, target):
    if len(myArray) < 2:
        return None
    prev_numbers = {}
    for index, element in enumerate(myArray):
        complement = target - element
        if complement in prev_numbers:
            return (prev_numbers[complement], index)
        prev_numbers[element] = index


if __name__ == "__main__":
    theArray = [3, 2, 5, 4, 1]
    theTarget = 8
    print(pair_sum(theArray, theTarget))
