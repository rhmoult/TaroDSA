from math import sqrt
from sys import argv


# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)
def is_prime(myInteger):
    if myInteger < 2:
        return False

    output = True  # Assume prime
    possible_factor = 2
    while possible_factor <= sqrt(myInteger):
        if myInteger % possible_factor == 0:
            output = False
        possible_factor += 1

    return output


if __name__ == "__main__":
    if len(argv) > 1:
        number_under_test = int(argv[1])
        if isinstance(number_under_test, int):
            print(is_prime(number_under_test))
