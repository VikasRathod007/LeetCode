import math


def minEatingSpeed(piles, h):
    low, high = 1, max(piles)
    while low <= high:
        mid = (low + high) // 2
        if getHour(piles, h, mid):
            high = mid - 1
        else:
            low = mid + 1
    return low


def getHour(piles, h, speed):
    hour = 0
    for pile in piles:
        hour += math.ceil(pile / speed)
    return hour <= h


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))
