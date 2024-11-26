def combinationSum(candidates, target):
    res = []
    candidates.sort()

    def backtrack(rem_target, curr_comb, curr_index):
        if rem_target == 0:
            res.append(list(curr_comb))
            return
        if rem_target < 0:
            return
        for i in range(curr_index, len(candidates)):
            candidate = candidates[i]
            if candidate > rem_target:
                break
            curr_comb.append(candidate)
            backtrack(rem_target - candidate, curr_comb, i)
            curr_comb.pop()

    backtrack(target, [], 0)
    return res


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
