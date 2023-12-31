# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого
# множества. m — кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.

# import random

n = int(input('Введите кол-во элементов первого множества: '))
lst_1 = [int(input(f'Введите {i+1}-й элемент первого множества: ')) for i in range(n)]
# lst_1 = [random.randint(-10, 10) for i in range(n)]
# print(lst_1)


m = int(input('Введите кол-во элементов второго множества: '))
lst_2 = [int(input(f'Введите {i+1}-й элемент второго множества: ')) for i in range(m)]
# lst_2 = [random.randint(-10, 10) for i in range(m)]
# print(lst_2)

res_lst = [i for i in lst_1 if i in lst_2]

# for i in lst_1:
#     if i in lst_2:
#         res_lst.append(i)

res_lst.sort()

if len(res_lst) > 0:
    print(*set(res_lst))
else:
    print('Нет общих элементов!')