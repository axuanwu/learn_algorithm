# 多种随机数生成算法
import math
def set_seed(seed):
    # 字符串或者数字输入转换为一个数字作为随机数的种子
    # TODO
    seed = str(seed)
    seed_int = 0
    for i in seed:
        int_i = ord(i)
        seed_int = seed_int << 8
        seed_int = seed_int | int_i
        if seed_int>2**30:
            b = seed_int>>18
            a = seed_int&(2**30-1)
            seed_int = a^b
    return seed_int


def rand_mod(seed, m):
    # 根据seed 得到一个随机数 h(k) = k mod m
    seed = set_seed(seed)
    return (seed%(m))


def rand_mult(seed, m):
    # 根据seed 得到一个随机数 h(k) = floor(m(kA mod 1))
    seed = set_seed(seed)
    A = (math.sqrt(5)- 1)*0.5
    index = math.floor((seed* A - math.floor(seed* A))*m)
    return index


def rand_double(seed, i, m):
    # 根据双重散列的方法计算位置  h(k, i) = (h1(k) + i * h2(k))%m
    index = (rand_mod(seed, m) + i * rand_mult(seed, m))% m
    return index




def getseed(str1):
    """
    :param str1: 字符串
    :return: 生成 256的位指纹
    """
    h = 0
    for x in str1:
        if ord(x) > 256:
            h <<= 12
            h += ord(x)
        else:
            h <<= 6
            h += ord(x)
    while (h >> 256) > 0:
        h = (h & (2 ** 256 - 1)) ^ (h >> 256)  # 数字不能太大
    return h


def getindex(seed, nummax2=22):
    # 通过循环移位来计算随机数
    N_max = 2 ** nummax2
    a = 0
    k = 3
    seed1 = seed
    while seed1 > 0:
        a =  a^((seed1 & (N_max - 1)) + k) #  22个1
        a = ((a << k) & (N_max - 1)) | (a >> (nummax2 - k))  # 左循环移位
        seed1 >>= nummax2
    return a
