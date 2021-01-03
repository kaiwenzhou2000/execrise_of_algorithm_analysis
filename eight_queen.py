MAXN = 8

# 初始化棋盘
chess_broad = [[0 for i in range(MAXN)] for j in range(MAXN)]
cnt = 0


def copy_arr(a):
    temp = []
    for line in a:
        temp.append(line[:])
    return temp


def check_out(x, y):
    """
    判断是否出现皇后之间的冲突
    :param x: 表示当前检查第几行
    :param y: 表示当前检查第几列
    :return: True表示有冲突
    :return: False表示有无冲突
    """
    for i in range(MAXN):
        for j in range(MAXN):
            # 如果上面没有棋子就不要检查了
            if chess_broad[i][j] == 0:
                continue

            # 表示在同一列
            if i == x and j != y:
                return False

            # 表示在同一列
            if j == y and x != i:
                return False

            # 表示在主对角线
            if y-x == j-i and x != i:
                return False

            # 表示在辅对角线
            if y+x == i+j and x != i:
                return False

    return True


def find(row):
    """
    递归查询八皇后
    :param row: 现在所处在第一行
    :return:
    """
    global cnt
    # 表示满足条件
    if row == MAXN:
        cnt += 1
        return

    for i in range(MAXN):
        if check_out(row, i):
            chess_broad[row][i] = 1
            find(row + 1)
            chess_broad[row][i] = 0  # 恢复现场


find(0)

print(cnt)
