def merge_the_tools(string, k):
    # res = []
    # part_length = len(string) // k
    # for i in range(0, len(string), part_length):
    #     res.append(s[i : i + part_length])
    # for strings in res:
    #     seen = set()
    #     new_str = ""
    #     for char in strings:
    #         if char not in seen:
    #             seen.add(char)
    #             new_str += char
    #     res[res.index(strings)] = new_str

    # return resdef merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substr = []
        for j in range(i, i + k):
            if string[j] not in substr:
                substr.append(string[j])
        print("".join(substr))


s = "AABCAAADA"
k = 3
print(merge_the_tools(s, k))
