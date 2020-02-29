# 冒泡排序
import math
import random
from time import *


def get_list():
    # 生产随机数组
    a = [0] * 1000
    random.seed("abc")
    for i in range(0, len(a)):
        a[i] = random.randint(1, 100)
    return a


# 冒泡排序

def exchange(a_list, i, j):
    #  交换 a_list 列表的第i个元素 和 第 j个元素
    tmp = a_list[i]
    a_list[i] = a_list[j]
    a_list[j] = tmp


def BubbleSort(a_list):
    # 冒泡排序
    global num_b
    num_b = 0
    length = len(a_list)
    i_end = 0
    while i_end < length - 1:
        i_start = length - 1
        while i_start > i_end:
            if a_list[i_start] < a_list[i_start - 1]:
                num_b += 1
                exchange(a_list, i_start, i_start - 1)
            else:
                num_b += 1
                pass
            i_start -= 1
        i_end += 1




# print(a)


# merge_sort
def merge_list(a_list, b_list):
    """

    :param a_list:  有序数组 a
    :param b_list:  有序数组 b
    :return: 有序数组 c
    """
    c_list = []
    num_m = 0
    i_a = 0
    i_b = 0
    while i_a < len(a_list) and i_b < len(b_list):  # & 位与   &&
        if a_list[i_a] < b_list[i_b]:
            c_list.append(a_list[i_a])
            i_a += 1
            num_m += 1
        else:
            num_m += 1
            c_list.append(b_list[i_b])
            i_b += 1
    # 按照顺序 补充未比较的元素
    while i_b < len(b_list):
        c_list.append(b_list[i_b])
        i_b += 1
    while i_a < len(a_list):
        c_list.append(a_list[i_a])
        i_a += 1
    return c_list, num_m


# a = [1,2,4,8]
# b = [2,3,6,8]
# c = merge_list(a,b)
# print(c)

def mergeSort(a_list):
    """

    :rtype: list
    """
    num_m = 0
    step = 1  # 数组的基本长度
    while step < len(a_list):
        i_stop = 0
        tmp_list = []
        while i_stop < len(a_list):
            # i_stop 到 i_stop+step  1组  i_stop+step 到 i_stop+2*i_step
            if i_stop + step > len(a_list):
                c_list = a_list[i_stop: len(a_list)]
            elif i_stop + 2 * step > len(a_list):
                c_list, num_tmp = merge_list(a_list[i_stop:i_stop + step], a_list[i_stop + step:len(a_list)])
                num_m += num_tmp
            else:
                c_list, num_tmp = merge_list(a_list[i_stop:i_stop + step], a_list[i_stop + step:i_stop + 2 * step])
                num_m += num_tmp
            tmp_list.extend(c_list)
            i_stop += 2 * step
        a_list = tmp_list
        step *= 2
    return a_list, num_m





def binSort(a_list, max_value=100):
    """
    计数排序
    :param a_list:
    :return: c_list 有序数组
    """
    len0 = max_value + 1
    a = [0] * len0
    for element in a_list:
        a[element] += 1
    c_list = []
    for i in range(0, len0):
        while (a[i] > 0):
            c_list.append(i)
            a[i] -= 1
    return (c_list)

def getIndexNum(num, i):
    a = 10**i
    b = a*10
    return math.floor(num % b /a)


def binsort_part(a_list, i_index, max_value):
    """
    按照数字的某一位排序 并且为 稳定排序
    :param a_list:
    :param i_index:
    :param max_value:
    :return:
    """
    len0 = max_value + 1
    a = [0] * len0
    for element in a_list:
        a[getIndexNum(element,i_index)] += 1
    c_list = [0] * len(a_list)
    sum_list = []
    sum = 0
    for i in range(0, len(a)):
        sum_list.append(sum)
        sum += a[i]  # sum_list 第5个位置 表示： 个位数数小与5的数字一共有多少个
    for i in range(0, len(a_list)):
        index = getIndexNum(a_list[i], i_index)
        c_list[sum_list[index]] = a_list[i]
        sum_list[index] +=1
    return(c_list)


def radixSort(a_list, max_value=100):
    """
    数字的基数排序
    :param a_list:
    :return:
    """
    i_index = 0
    while(max_value>=1):
        a_list = binsort_part(a_list,i_index, max_value=9)
        max_value = math.floor(max_value/10)
        i_index += 1
    return a_list



a = get_list()
begin_time = time()
BubbleSort(a)
print(time()-begin_time)

a = get_list()
begin_time=time()
b, num_m = mergeSort(a)
print(time()-begin_time)


a = get_list()
begin_time = time()
a = binSort(a)
print(time()-begin_time)


a = get_list()
begin_time=time()
a = radixSort(a, 100)
print(time()-begin_time)

