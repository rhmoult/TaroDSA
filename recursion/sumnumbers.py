def sum_numbers(intArray):
    if len(intArray) == 0:
        return 0
    return intArray[0] + sum_numbers(intArray[1:])


array = [5, 2, 9, 10]
print(sum_numbers(array))
