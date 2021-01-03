import random


def get_random():
    """
    生成【1， 10】的随机数
    :return: 返回【1， 10】之间的随机数
    """
    return random.randint(1, 10)


num = int(get_random() / 2)

if num == 0:
    print(5)
else:
    print(num)
