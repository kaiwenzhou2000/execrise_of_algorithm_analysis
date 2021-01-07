# 利用动态规划解决数塔问题

tower = [
    [9],
    [12, 15],
    [10, 6, 8],
    [2, 18, 9, 5],
    [19, 7, 10, 4, 16]
]

# 数塔的高度
level = len(tower)-2

# 采用逆顺法解决
while level >= 0:
    for i in range(len(tower[level])):
        tower[level][i] = max(tower[level][i] + tower[level+1][i], tower[level][i] + tower[level+1][i+1])
    level -= 1

print(tower[0][0])
