# 这是最优装载问题，这里使用的方法是回溯法，想看分支限界法的可以去查看一下我期末考试卷的分析
w = [10, 40, 40]  # 物品的重量
ship = 50  # 船的最大载重
bestw = 0
ans = 0


def find(level):
    global bestw, ans
    if level == len(w):
        if ans < bestw:
            ans = bestw
        return
    # 拿
    if bestw + w[level] <= ship:
        bestw += w[level]
        find(level + 1)
        bestw -= w[level]  # 恢复现场
    # 不拿
    find(level + 1)


find(0)

print(ans)
