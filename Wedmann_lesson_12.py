# 1. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит пустая строка.
# f = open('C:/Users/Admin/PycharmProjects/group/task1.txt', 'w', encoding='utf-8')
# a = input("Введите данные: ")
# f.write(a)

#2. В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов.
# s = open('C:/Users/Admin/PycharmProjects/group/task2.txt', 'r', encoding='utf-8')
# print(len(s.readlines()))
# s.close()
# with open('C:/Users/Admin/PycharmProjects/group/task2.txt','r') as s:
#     for i in s.readlines():
#         print(f"В {i} строке -- {len(i)-1}")

# 3. Есть список состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.

# 4. Добавьте на свой РАБОЧИЙ СТОЛ папку my_name, в ней создайте 3 текстовых файла через цикл: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os
import os
os.mkdir('C:/Users/Admin/Desktop/my_name')
print(os.getcwd())
for i in