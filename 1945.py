# 1945. Sum of Digits of String After Convert
# You are given a string s consisting of lowercase English letters, and an integer k.


# First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.
def getLucky(s, k):
    s = "".join(str(ord(char) - 97 + 1) for char in s)
    for i in range(k):
        s = str(sum(int(digit) for digit in s))
    return s


s = "zbax"
k = 2
print(getLucky(s, k))
