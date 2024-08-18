from collections import Counter


def longestPalindrome(s):
    if len(s) == 1:
        return 1
    s1 = Counter(s)
    print(s1)
    count = 0
    odd_count_found = False
    for values in s1.values():
        if values % 2 == 0:
            count += values
        else:
            count += values - 1
            odd_count_found = True

    if odd_count_found:
        count += 1
    return count


s = "abccccdd"
print(longestPalindrome(s))  # Output: "dccaccd"
