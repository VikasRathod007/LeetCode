from collections import Counter


def isNStraightHand(hand, k):
    if len(hand) % k != 0:
        return False
    hand.sort()
    print(hand)
    freq = Counter(hand)
    print(freq)
    for num in hand:
        if freq[num] > 0:
            for i in range(num, num + k):
                if freq[i] == 0:
                    return False
                freq[i] -= 1
    return True


hand = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
groupSize = 3
print(isNStraightHand(hand, groupSize))
