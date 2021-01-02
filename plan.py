s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
plan = []
res = []

# 构造plan数组字典
for i in range(len(s)):
    temp = {'start': s[i], 'finish': f[i]}
    plan.append(temp)

# 根据结束时间排序
for i in range(len(plan)):
    for j in range(i+1, len(plan)):
        if plan[i]['finish'] > plan[j]['finish']:
            temp = plan[i]
            plan[i] = plan[j]
            plan[j] = temp

# 首先将第一个结束的时间放入res中
res.append(plan[0])
# 筛选
for i in plan[1:]:
    if i['start'] >= res[len(res)-1]['finish']:
        res.append(i)

print(res)
