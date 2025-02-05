from collections import Counter
from sys import argv


# Time Complexity: O(n)
# Space Complexity: O(n)
def is_anagram_via_counter(baseline, possible_anagram):
    baseline_count = Counter(baseline)
    possible_anagram_count = Counter(possible_anagram)
    return baseline_count == possible_anagram_count


# Time Complexity: O(n)
# Space Complexity: O(n)
def is_anagram_manually(baseline, possible_anagram):
    return char_count(baseline) == char_count(possible_anagram)


# Time Complexity: O(n)
# Space Complexity: O(n)
def char_count(myString):
    count = {}

    for char in myString:
        if char not in count:
            count[char] = 0

        count[char] += 1

    return count


if __name__ == "__main__":
    if len(argv) > 2:
        one = argv[1]
        two = argv[2]
        print(is_anagram_via_counter(one, two))
        print(is_anagram_manually(one, two))
