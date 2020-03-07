import random

random.seed(100)
tList=[]
for a in range(0,10):
    tList.append(a)

random.shuffle(tList)
print(tList)
ind_list = [1, 5, 9, 4, 0, 2,6,8,7,3]
# tList[ind_list[1]]=1   tList[1]=1

def b_search(sList, element):
    """

    :param sList: 需要查找的列表
    :param element:  需要查找 的 元素
    :return:  element 在 sList种的下标  -1表示没找到
    """
    length = len(sList)
    index = length*0.5
    step = length*0.5
    while(step >= 0.5):
        int_index =int(index)
        step *= 0.5
        if sList[int_index]>element:   #sList[ind_list[int_index] ]>element
            index -= step
        elif sList[int_index]<element:
            index += step
        else:
            return int_index
    return -1


def b_search2(sList, ind_list, element):
    """

    :param sList: 需要查找的列表
    :param element:  需要查找 的 元素
    :return:  element 在 sList种的下标  -1表示没找到
    """
    length = len(sList)
    index = length*0.5
    step = length*0.5
    while(step >= 0.5):
        int_index =int(index)
        step *= 0.5
        if sList[ind_list[int_index] ]>element:
            index -= step
        elif sList[ind_list[int_index]]<element:
            index += step
        else:
            return ind_list[int_index]
    return -1

print(b_search2(tList, ind_list ,10))
