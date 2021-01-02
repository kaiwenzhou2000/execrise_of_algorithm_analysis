MAX_SIZE = 5  # 表示map的大小

tank_map = [[0 for i in range(MAX_SIZE)] for j in range(MAX_SIZE)]  # 初始化map，全为0

res = []


def is_good():
    for i in tank_map:
        for j in i:
            if j == 0:
                return False
    return True


def take_place(x: int, y: int):
    global tank_map
    tank_map[x][y] = 2  # 坦克的位置为2
    # 上
    if x != 0 and tank_map[x - 1][y] != 2:
        tank_map[x - 1][y] = 1
    # 下
    if x != MAX_SIZE - 1 and tank_map[x + 1][y] != 2:
        tank_map[x + 1][y] = 1
    # 左
    if y != 0 and tank_map[x][y - 1] != 2:
        tank_map[x][y - 1] = 1
    # 右
    if y != MAX_SIZE - 1 and tank_map[x][y + 1] != 2:
        tank_map[x][y + 1] = 1


def make_backup(arr):
    """
    实现二维列表的深拷贝
    :param arr: 需要被拷贝的二维列表
    :return:    返回拷贝完成的二维列表
    """
    temp = []
    for i in arr:
        temp.append(i[:])
    return temp


def find_way(x, y):
    """
    用来寻找坦克的路径
    :param x:   表示现在的横坐标
    :param y:   表示现在的纵坐标
    :return:
    """
    global tank_map, res
    # 越界
    if y >= MAX_SIZE:
        x += 1
        y = 0
    if x >= MAX_SIZE:
        return

    # 找到结果
    if is_good():
        res.append(make_backup(tank_map))
    # 占据
    backup = make_backup(tank_map)  # 保护现场
    take_place(x, y)
    find_way(x, y + 1)
    tank_map = backup  # 恢复现场
    # 不占据
    find_way(x, y + 1)


def print_tank_map():
    global res
    for m in res:
        for i in range(MAX_SIZE):
            for j in range(MAX_SIZE):
                print(str(m[i][j]) + ' ', end='')
            print()
        print()


find_way(0, 0)
print_tank_map()
