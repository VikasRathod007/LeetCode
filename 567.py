# 567. Permutation in String
from collections import Counter


def checkInclusion(s1, s2):
    s1Freq = Counter(s1)
    s2Freq = Counter(s2[: len(s1)])
    low = 0
    for high in range(len(s1), len(s2)):
        if s2Freq == s1Freq:
            return True
        s2Freq[s2[low]] -= 1
        if s2Freq[s2[low]] == 0:
            del s2Freq[s2[low]]
        low += 1
        s2Freq[s2[high]] += 1
    return s1Freq == s2Freq


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))
