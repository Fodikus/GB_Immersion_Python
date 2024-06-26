# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

a = int(input("Введите число от 1 до 999 "))

while True:
    if 0 < a < 10:
        result = a ** 2

    elif 10 <= a < 100:
        b = a // 10
        c = a % 10
        result = b * c

    elif 100 <= a < 1000:
        b = a // 100
        c = a // 10 % 10
        d = a % 10
        result = d * 100 + c * 10 + b

    else:
        a = int(input("Вне диапозона, Введите число от 1 до 999"))
        continue
    break

print(result)