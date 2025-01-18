array = [4, 7, 5, 9, 2]


def max_value(myarray):
    max = float("-inf")

    for item in array:
        if item > max:
            max = item

    return max


if __name__ == "__main__":
    print(max_value(array))
