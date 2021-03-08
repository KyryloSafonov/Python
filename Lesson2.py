# Task 1
# написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        вивело в консолі

# st = 'as 23 fdfdg544'
#
# result = ''
# for ch in st:
#     if ch.isdecimal():
#         result += ch
# result = ', '.join(result)
# print(result)
#
# # Task 2
# написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' введена строка
#   23, 544, 34              вивело в консолі

# st = 'as 23 fdfdg544 34 !!12243234234!'
#
# result =''
# for ch in st:
#     if ch.isdigit():
#         result += ch
#     else: result += ''
# result += ch if ch.isdecimal() else ''
# result = ', '.join(result.split())
# print(result)

# Task 3
# есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
#
# chars = [item.upper() for item in greeting]
# print(chars)

# Task 4
# с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# # пример:
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# numbers = [number ** 2 for number in range(50) if number % 2 != 0]
# print(numbers)

# # Task 5
# l = [1, 2, 3, 4, 5, 6]
#
# def list_func(l):
#     for i in range(len(l)):
#         print(f'{i} -> {l[i]}')
#
# list_func(l)

# Task 6
# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def min_number(a, b, c):
#     res = min(a, b, c)
#     print(res)
#     return res
#
# min1 = min_number(6, 0.22548451, 567)
# print(min1)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_number(a, b, c):
#     res = max(a, b, c)
#     print(res)
#     return res
#
# max_number(125, 17, 84)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def min_max_number(*args):
#     print(max(args))
#     return min(args)
#
# min = min_max_number(3, 5, 6, 8, 1234, 908 )
# print(min)

#  створити функцію яка повертає найбільше число з ліста

l = [1, 3, 5, 6, 7, 95, 781, 258, 3695, 2018, 2021]

# def max_from_list(l):
#     return max(l)
#
# print(max_from_list(l))

# творити функцію яка повертає найменьше число з ліста

# def min_from_list(l):
#     return min(l)
#
# print(min_from_list(l))

# створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sum_from_list(l):
#     return sum(l)
#
# print(sum_from_list(l))

# творити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def avg_from_list(l):
#     return sum(l) // len(l)
#
# print(avg_from_list(l))

# -функція: def pr(): return 'Hello_boss_!!!'
#  написати декоратор який замінює нижні підчеркування на пробіли і повертає це значення



def decor(func):
    def wrap():
        return func().replace('_', ' ')

    return wrap()

@decor
def pr():
    return 'Hello_boss_!!!'

print(pr)



