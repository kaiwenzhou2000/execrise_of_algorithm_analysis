# M1就表示r1*r2
# M2就表示r2*r3
r = [-1, 5, 20, 50, 1, 100]

MATRIX_NUM = len(r)-2

# 初始化状态记录的矩阵
# 里面记录着i-j的最小值
# 如multi_table[1][3] 就是矩阵M1*M2*M3
multi_table = [[0 for i in range(MATRIX_NUM+1)] for j in range(MATRIX_NUM+1)]

for i in range(MATRIX_NUM-1):
    multi_table[i+1][i+2] = r[i+1]*r[i+2]*r[i+3]

# 进行动态规划
# s表示偏移量
for s in range(2, MATRIX_NUM):
    for i in range(1, MATRIX_NUM - s + 1):
        j = i + s
        temp = -1
        for k in range(i, j):
            if temp == -1:
                temp = multi_table[i][k] + multi_table[k+1][j] + r[i]*r[k+1]*r[j+1]
                multi_table[i][j] = temp
            else:
                if temp > multi_table[i][k] + multi_table[k+1][j] + r[i]*r[k+1]*r[j+1]:
                    temp = multi_table[i][k] + multi_table[k+1][j] + r[i]*r[k+1]*r[j+1]
                    multi_table[i][j] = temp

# 展示
for line in multi_table[1:]:
    print(line)

print('最少的连乘次数是' + str(multi_table[1][MATRIX_NUM]))
