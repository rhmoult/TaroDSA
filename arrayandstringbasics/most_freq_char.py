from collections import Counter


def most_freq_char(input_string):
    input_dict = Counter(input_string)

    most_frequent = None
    for char in input_string:
        if most_frequent is None or input_dict[char] > input_dict[most_frequent]:
            most_frequent = char

    return most_frequent


if __name__ == "__main__":
    print(most_freq_char("potato"))
    ...
