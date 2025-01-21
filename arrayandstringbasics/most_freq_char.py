from collections import Counter


def most_freq_char(input_string):
    input_dict = Counter(input_string)

    most_frequent = ""
    frequency = 0
    for key in input_dict:
        if input_dict[key] > frequency:
            most_frequent = key
            frequency = input_dict[key]

    return most_frequent


if __name__ == "__main__":
    print(most_freq_char("potato"))
    ...
