# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a1 = 0
    b1 = 1
    c1 = 0
    while c1 < m:
        a1 = a1 + b1
        b1 = a1 - b1
        c1 += 1
        if c1 >= n:
            print(a1)
        else:
            continue

fibonacci(1, 10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for n in range(len(origin_list)):
        for i in range(len(origin_list) - 1, n, -1):
            if origin_list[i] < origin_list[i - 1]:
                origin_list[i], origin_list[i - 1] = origin_list[i - 1], origin_list[i]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(f, l):
    result_l = []
    for item in l:
        if f(item):
            result_l.append(item)
    return result_l

print(my_filter(lambda x: x > 100, [10, 60, 150, 100, 200, 90]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

x1, y1 = (4, 6) # A1
x2, y2 = (11, 6) # A2
x3, y3 = (10, 2) # A3
x4, y4 = (3, 2)# A4

xc0 = (x1 + x3) / 2
xc1 = (x2 + x4) / 2
yc0 = (y1 + y3) / 2
yc1 = (y2 + y4) / 2

if xc0 == xc1 and yc0 == yc1:
    print('Вершины параллелограмма ')
elif  y1 != y2 and y3 != y4 and x2 - x1 != x3 - x4:
    print('Параллелограмма не существует')


