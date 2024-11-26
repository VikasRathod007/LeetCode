from typing import List


def dividePlayers(skill):
    sum_ = sum(skill)
    if sum_ % (len(skill) / 2) != 0:
        return -1
    skill_team = sum_ / (len(skill) / 2)
    skill.sort()
    left, right = 0, len(skill) - 1
    res = 0
    while left < right:
        if skill[left] + skill[right] == skill_team:
            res += skill[left] * skill[right]
            left += 1
            right -= 1
        elif skill[left] + skill[right] < skill_team:
            left += 1
        else:
            right -= 1
    return res


skill = [3, 2, 5, 1, 3, 4]
print(dividePlayers(skill))
# 1, 2, 3, 3, 4, 5
