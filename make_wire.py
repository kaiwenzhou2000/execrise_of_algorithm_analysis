MAXN = 6

wire_map = [[0 for i in range(MAXN)] for j in range(MAXN)]
step = 0
queen = [-1]
res = []


# 起点(1, 1)
# 终点(4, 4)

class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def copy_arr(a):
    temp = []
    for line in a:
        temp.append(line[:])
    return temp


# 这是好不可达的标记，-1表示不可达
def set_block():
    global wire_map
    wire_map[4][0] = -1
    wire_map[4][1] = -1
    wire_map[4][2] = -1
    wire_map[3][2] = -1
    wire_map[2][2] = -1
    wire_map[1][2] = -1


def find_way(x, y):
    global step, wire_map
    step += 1
    if x == 4 and y == 4:
        res.append(copy_arr(wire_map))
        return
    else:
        # 向上
        if x != 0 and wire_map[x - 1][y] == 0:
            wire_map[x - 1][y] = step
            find_way(x - 1, y)
        # 向下
        if x != MAXN - 1 and wire_map[x + 1][y] == 0:
            wire_map[x + 1][y] = step
            find_way(x + 1, y)
        # 向左
        if y != 0 and wire_map[x][y - 1] == 0:
            wire_map[x][y - 1] = step
            find_way(x, y - 1)
        # 向右
        if y != MAXN - 1 and wire_map[x][y + 1] == 0:
            wire_map[x][y + 1] = step
            find_way(x, y + 1)


set_block()
wire_map[1][1] = 'a'
wire_map[4][4] = 'b'
# 初始化queen队列
queen.append(node(1, 1))
# find_way(1, 1)


while len(queen) != 0:
    head = queen[0]     # 找到头结点作为E-节点，有其来生成子节点
    # 检测到层级结束
    if head == -1:
        del queen[0]
        queen.append(-1)
        step += 1
        continue

    # x, y 表示当前头结点所在的位置
    x = head.x
    y = head.y

    # 检测到结果
    if (x == 4 and abs(y-4) == 1) or (y == 4 and abs(x-4) == 1):
        break

    if x != 0 and wire_map[x - 1][y] == 0:
        wire_map[x - 1][y] = step
        queen.append(node(x-1, y))
    # 向下
    if x != MAXN - 1 and wire_map[x + 1][y] == 0:
        wire_map[x + 1][y] = step
        queen.append(node(x+1, y))
    # 向左
    if y != 0 and wire_map[x][y - 1] == 0:
        wire_map[x][y - 1] = step
        queen.append(node(x, y-1))
    # 向右
    if y != MAXN - 1 and wire_map[x][y + 1] == 0:
        wire_map[x][y + 1] = step
        queen.append(node(x, y+1))
    # 删除头结点
    del queen[0]


# 展示结果
for line in wire_map:
    print(line)
