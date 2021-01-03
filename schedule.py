N = 8
a = [[0 for i in range(N)] for j in range(N)]


def copy(n):
    m = int(n / 2)  # m 是指现在方块规模的大小
    for i in range(m):
        for j in range(m):
            # 左上角映射到右下角
            a[i + m][j + m] = a[i][j]
            # 右下角+n/2映射到右上角
            a[i][j + m] = a[i + m][j + m] + int(n / 2)
            # 右上角映射到左下角
            a[i + m][j] = a[i][j + m]


def table(n):
    if n == 1:
        a[0][0] = 1
    else:
        table(int(n / 2))
        copy(n)


table(8)

# 第一排表示参赛的选手的序号
# 第二排表示第一天参赛选手对阵的对手
# 。。。。
for line in a:
    print(line)
