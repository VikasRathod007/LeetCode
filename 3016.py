# 3016. Minimum Number of Pushes to Type Word II


def minimumPushes(word):

    hash_map = {}
    for i in word:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    # highFrequency = sorted(hash_map.items(), key=lambda k: k[1], reverse=True)
    highFrequency = sorted(hash_map.values(), reverse=True)
    res = 0
    distinct = 1
    for i in range(len(highFrequency)):
        if i == 8 or i == 16 or i == 24:
            # print(i)
            distinct += 1
            print(i, distinct)
        res += highFrequency[i] * distinct

    print(highFrequency)
    return res


word = "aremgjnptohswfdkyuzvicqxb"
print(minimumPushes(word))
