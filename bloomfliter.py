# -*- coding: utf-8 -*-
# created by axuanwu 2015.1.25
# key word: hash  count
import numpy as np
import math


def getseed(str1):
    """
    :param str1: 词条的utf8形式
    :return: 词条的hash指纹 256的位随机数
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


class Mcard():
    def __init__(self):
        self.M_num = 8
        self.N_max = 16777216  # 长度
        self.nummax2 = 24     # 数组长度取对数 2为底
        self.MCARD = [0]  # 大数组
        self._record = 1
        self.Opath = ""
        self.index = [0] * 8
        # self.__keys = ['first_NULL'first_NULL]/


    def getindex(self, str1):
        # 获取 词条的 8个随机位置
        seed = getseed(str1)
        for n in range(0, self.M_num):
            a = 0
            k = (n + 1)
            seed1 = seed
            if (seed >> 64) < 0:
                seed1 = seed * (n + 15048796327)
            while seed1 > 0:
                a ^= (seed1 & (self.N_max - 1)) + k
                a = ((a << k) & (self.N_max - 1)) | (a >> (self.nummax2 - k))  # 左循环移位
                seed1 >>= self.nummax2
                self.index[n] = a

    def update_card(self, str1):
        """
        :param str1: 词的utf-8编码形式
        :param num: 该词需要增加的value值
        """
        self.getindex(str1)
        for iii in self.index:
            if not self.MCARD[iii]:
                self.MCARD[iii] = True


    def read_card(self, str1, for_up=False):
        """
        :param str1: 词的utf-8编码形式
        :return: 输出该次条对应的value值
        """
        self.getindex(str1)
        aaa = self.MCARD[self.index]
        if sum(aaa==False)>=1:
            return False
        else:
            return True


    def setbase(self, num1=16777216, num2=8):
        """
        :param num1: 数组长度参数
        :param num2: 每个词条对应的hash位置数
        """
        self.nummax2 = int(math.ceil(math.log(num1, 2)))
        self.N_max = 2 ** self.nummax2  # self.nummax2 2的N次方
        self.M_num = num2
        self.index = [0] * num2
        self.index2 = [0] * num2

    def set_card(self, kk=-1, dd=8):
        """
        :param kk:  数组长度参数 -1表示取之前定义值
        """
        if -1 == kk:
            self.MCARD = np.repeat(False, self.N_max)
            return 0
            s1 = input('do you want to reset MCARD to zeros,all memory will be lost [y/n]:')
            if s1 == 'y':
                self.MCARD = np.repeat(False, self.N_max)
            else:
                print("no reset")
        else:
            self.setbase(kk, dd)
            self.MCARD = np.repeat(0, 2 ** self.nummax2)



    def card_test(self):
        """
        计算hash碰撞指数
        """
        aaa = self._record
        bbb = self.N_max
        ccc = 0
        for i in self.MCARD:
            ccc += int(i > 0)
        ddd = self.M_num
        print (math.log(1.0 * ccc / bbb, 10) * ddd, math.log((1.0 * aaa * ddd - ccc) / ccc, 10) * ddd)



if __name__ == '__main__':
    card = Mcard.Mcard()
    card.setbase(2 ** 28, 8)  # 参数设置
    card.set_card()  # 初始化hash桶
    for i in range(1, 200001):
        if i == 999:
            card.update_card('99901')
        else:
            card.update_card(str(i))
    for i in range(1, 2001):
        a = card.read_card(str(i))
        if card.get_keys(a) != str(i):
            print (i, a, card.get_keys(a))