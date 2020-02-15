from randomFun import *

a = list(range(100))
# 遍历法
for item in a:
    if item ==38:
        print(item)
# 元素与下标 之间的映射
print(a[38])


#
# a[34] = 101
#
# list_length = 120
# denominator = 97
# list_hash = [-1] * list_length

#
# def get_index(item, list_hash):
#     mark = True  # 是佛需要去找下一个位置
#     i = 0
#     list_length = len(list_hash)
#     while mark:
#         if i>10:
#             index += 1
#             index = index % list_length
#             if list_hash[index] == -1:
#                 mark = False
#             else:
#                 if list_hash[index] == item:
#                     mark = False
#                 else:
#                     print(i)
#                     i += 1
#         else:
#             index = rand_double(item, i, list_length)
#             # print(index)
#             if list_hash[index] == -1:
#                 mark = False
#             else:
#                 if list_hash[index] == item:
#                     mark = False
#                 else:
#                     # print(i)
#                     i += 1
#     return (index)
#
#
# for item in a:
#     index = get_index(item, list_hash)
#     # if index==-1:
#     #     pass
#     list_hash[index] = item
#
# index = get_index(41, list_hash)
# index = get_index(101, list_hash)
# print(list_hash[index])
#
