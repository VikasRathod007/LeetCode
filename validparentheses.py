def isValid(s):
    stack = []
    matching = {")": "(", "}": "{", "]": "["}
    for i in s:
        if i in matching:
            top_element = stack.pop() if stack else "#"
            print(matching[i], top_element)
            if matching[i] != top_element:
                return False
        else:
            stack.append(i)
    return not stack


s = "[]"
print(isValid(s))
