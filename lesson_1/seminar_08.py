# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата: Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

heigh = int(input("Введите количество рядов елки: "))

#1вариант с интерпаляцией
for i in range(heigh):
    print(f'{"*" * (2*i+1):^{heigh*2}}')    # формат команды (f'{имя переменной}:^отступ  ')

print("")

for i in range(heigh):
    print(f'{"*" * (2 * i + 1):/^{heigh * 2}}')

print("")

#2 вариант интерпаляцией:
n = 1
while n <= heigh*2:
    print(("*" * n).center(heigh*2))
    n += 2

print("")

# 3вариант обычный
i = 0
while i < heigh:
    j = 0

    while j < heigh - 1 - i:
        print(" ", end="")
        j += 1
    j = 0
    while j < 2*i+1:
        print("*", end="")
        j += 1
    print("")
    i += 1