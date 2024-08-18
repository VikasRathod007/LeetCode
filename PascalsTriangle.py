def generate(n):
    arr = []
    for i in range(1, n + 1):
        row = []
        for j in range(0, i):
            if j == 0 or j == i - 1:
                row.append(1)
            else:
                if arr:
                    prev_row = arr[i - 2]
                    row.append(prev_row[j - 1] + prev_row[j])
        arr.append(row)
    return arr


n = 5
print(generate(n))
