from collections import Counter


def commonChars(words):
    # Initialize a list to hold counters for each word
    counters = [Counter(word) for word in words]

    # Initialize the result counter with the first word's counter
    common_count = counters[0]

    # Update the result counter with each subsequent word
    for counter in counters[1:]:
        for char in list(common_count.keys()):
            if char in counter:
                common_count[char] = min(common_count[char], counter[char])
            else:
                del common_count[char]

    # Construct the result list
    res = []
    for char, count in common_count.items():
        res.extend([char] * count)

    return res


# Example usage
words = ["bella", "label", "roller"]
print(commonChars(words))  # Output: ['e', 'l', 'l']
