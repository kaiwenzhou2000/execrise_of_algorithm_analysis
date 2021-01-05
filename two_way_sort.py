def merge(arr, left, middle, right):
    """
    将两个子列表进行排序
    :param arr:     # 母数组
    :param left:    # 最左边的下标
    :param middle:  # 中间的下标
    :param right:   # 最右边的下标
    :return:
    """
    left_list = []
    right_list = []
    # 构造左边的列表
    left_list = arr[left: middle + 1]
    # 构造右边的列表
    right_list = arr[middle + 1: right + 1]

    index = left
    while left_list != [] and right_list != []:
        if left_list[0] > right_list[0]:
            arr[index] = right_list.pop(0)
            index += 1
        else:
            arr[index] = left_list.pop(0)
            index += 1

    while left_list:
        arr[index] = left_list.pop(0)
        index += 1
    while right_list:
        arr[index] = right_list.pop(0)
        index += 1


def mergesort(arr, left, right):
    """
    使用递归将数组查分过来
    :param arr:     将要被拆分的数组
    :param left:    最左边的下标
    :param right:   最右边的下标
    :return:
    """
    if left >= right:
        return
    middle = int((right + left) / 2)
    mergesort(arr, left, middle)
    mergesort(arr, middle + 1, right)
    merge(arr, left, middle, right)


array = [5, 2, 4, 7, 1, 3, 2, 6]

mergesort(array, 0, len(array) - 1)

print(array)
