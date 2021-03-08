# Task 1
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# print(min(list))

# Task 2
# list_ = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# index = len(list_)-1
# while index:
#     item = list_[index]
#     if list_.count(item) >1:
#         while list_.count(item)>0:
#             list_.remove(item)
#             index-=1
#     else:
#         index-=1
#
# print(list_)

# Task 2 (alternative)
# list_ = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# index = len(list_)-1
# while index:
#     item = list_[index]
#     if list_.count(item) >1:
#         while list_.count(item)>1:
#             list_.remove(item)
#             index-=1
#     else:
#         index-=1
#
# print(list_)

# Task 3
# list_ = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5, 6, 7, 10, 11]
#
# for i in range(3,len(list_),4):
#    list_[i]='X'
# print(list_)

# #Task 4
# list_ = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# l = list_.copy()
# for i in range(3, len(l), 4):
#     l[i] = 'X'
#     print(l)

# Task 5
# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# print('List=', l)
# l.sort()
# sum=0
# for i in l:
#     sum+=1
# avg = sum/len(l)
#
# candidates=[]
#
# for i in range(len(l)):
#     if l[i] > avg:
#         candidates.append(l[i])
#         candidates.append(l[i] - 1)
#         break
#     print("avg=", avg)
#
# if not len(candidates):
#     print('result=', avg)
# else:
#     print('result=', candidates[0] if avg > (candidates[0] + candidates[1]) / 2 else candidates[1])

# # create order list for our list_
#
# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# while True:
#     print('1. найти min число в листе')
#     print('2. удалить все одинаковые значения')
#     print('3. заменить каждое четвертое значение на "Х"')
#     print('4. вывести элемент листа, значение которого ближе всего к среднему арифметическому всех елементов в листе')
#     print('5. выход')
#
#     choice = input('Сделайте свой выбор: ')
#     if choice not in '123456':
#         continue
#
#     elif choice == '1':
#         min_num = l[0]
#         for item in l:
#             if min_num > item:
#                 min_num = item
#         print(l)
#         print('min_num: ', min_num)
#
#     elif choice == '2':
#         l2 = l.copy()
#         for i in range(len(l2) - 1, -1, -1):
#             if l2.count(l2[i]) > 1:
#                 del l2[i]
#
#         print(l)
#         print(l2)
#
#     elif choice == '3':
#         l2 = l.copy()
#         for i in range(3, len(l2), 4):
#             l2[i] = 'X'
#         print(l2)
#
#     elif choice == '4':
#         print('List =', l)
#         l.sort()
#         sum = 0
#         for i in l:
#             sum += i
#         avg = sum / len(l)
#
#         candidates = []
#
#         for i in range(len(l)):
#             if l[i] > avg:
#                 candidates.append(l[i])
#                 candidates.append(l[i - 1])
#                 break
#         print("Avg =", avg)
#
#         if not len(candidates):
#             print('result:', avg)
#         else:
#             print('result = ', candidates[0] if avg > (candidates[0] + candidates[1]) / 2 else candidates[1])
#
#     elif choice == '5':
#         break

# multiplication table

# i = 1
# size = 10
# while i <= size:
#     j = 1
#     while j <= size:
#         res = i * j
#         if res // 10:
#             print(res , end='  ')
#         else:
#             print(res, end= '    ')
#         j += 1
#         print()
#         i += 1

# square of star*

# a = 5
# i = 1
# while i >= 1:
#     if i == a or i == 1:
#         j = a
#         while j > 0:
#             print('*', end = ' ')
#             j -= 1
#         print()
#     else:
#         j = a - 2
#         print('*', end= ' ')
#         while j > 0:
#             print(' ', end= ' ')
#             j -= 1
#         print('*')
#     i -= 1








