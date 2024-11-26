# 424. Longest Repeating Character Replacement
from collections import Counter


def characterReplacement(s, k):
    left = 0
    max_length = 0
    charCount = Counter()
    for right in range(len(s)):
        charCount[s[right]] += 1

        window_length = right - left + 1
        replacements_needed = window_length - max(charCount.values())
        if replacements_needed > k:
            charCount[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


s = "AABABBA"
k = 1
print(characterReplacement(s, k))
