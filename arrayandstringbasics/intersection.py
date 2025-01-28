def intersection(firstArray, secondArray):
    firstArrayAsSet = set(firstArray)
    return [element for element in secondArray if element in firstArrayAsSet]


if __name__ == "__main__":
    firstArray = [4, 2, 1, 6]
    secondArray = [3, 6, 9, 2, 10]
    print(intersection(firstArray, secondArray))
