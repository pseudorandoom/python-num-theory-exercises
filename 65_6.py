def magic_square(m):
    l = len(m[0])
    sum_list = []

    for col in range(l):
        sum_list.append(sum(row[col] for row in m))

    sum_list.extend([sum(lines) for lines in m])

    dlResult = 0
    for i in range(0, l):
        dlResult += m[i][i]
    sum_list.append(dlResult)

    drResult = 0
    for i in range(l - 1, -1, -1):
        drResult += m[i][i]
    sum_list.append(drResult)

    if len(set(sum_list)) > 1:
        return False
    return (True, drResult)

magic = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

no_magic = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(magic_square(magic))
print(magic_square(no_magic))