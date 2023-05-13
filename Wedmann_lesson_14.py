#ДЗ на понедельник (Ivanov_Lesson_14.py):
# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
# Работу загружаем в репозиторий гита. Скидываем ссылку НА ФАЙЛ!

while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = input('Введите знак: ')
    def plus(a,b):
        return a+b
    def minus(a,b):
        return a-b
    def zerrodiv(a,b):
        try: a/b
        except ZeroDivisionError: print("На ноль делить нельзя!")
    def div(a,b):
        if b==0:
            try: a/b
            except ZeroDivisionError: print("На ноль делить нельзя!")
        else:
            return a/b
    def multi(a,b):
        return a*b
    def zerro():
        return "Выход из программы"
    if c=='+':
        print(plus(a,b))
    if c=='-':
        print(minus(a,b))
    if c=='*':
        print(multi(a,b))
    if c=='/':
        print(div(a,b))
    if c=='0':
        print(zerro())
        break