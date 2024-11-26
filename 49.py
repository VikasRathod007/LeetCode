# 49. Group Anagrams
def groupAnagram(strs):
    hashMap = {}
    for s in strs:
        sortedString = "".join(sorted(s))
        if sortedString not in hashMap:
            hashMap[sortedString] = [s]
        else:
            hashMap[sortedString].append(s)

    return list(hashMap.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = [""]
print(groupAnagram(strs))
