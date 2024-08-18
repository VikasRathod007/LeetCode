# 3. Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(str):
    # substring = set()
    # count = 0
    # max_lenght = 0
    # for char in str:
    #     # print(char)
    #     if char not in substring:
    #         substring.add(char)
    #         count += 1
    #     else:
    #         max_lenght = max(max_lenght, count)
    #         substring.clear()
    #         substring.add(char)
    #         count = 1
    # return max(max_lenght, count)
    substring = set()
    left = 0
    max_lenght = 0
    for right in range(len(str)):
        while str[right] in substring:
            substring.remove(str[left])
            left += 1
        substring.add(str[right])
        max_lenght = max(max_lenght, right - left + 1)
    return max_lenght


s = "pwwkew"
print(lengthOfLongestSubstring(s))
