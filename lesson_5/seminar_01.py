# Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”. Сформируйте словарь, где:
# второе и третье число являются ключами;  
# первое число является значением для первого ключа;  
# четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.

string = input('введите строку из четырёх или более целых чисел, разделённых символом “/”')
a, b, c, *d = string.split('/')
my_dict = {b:a, c:d}
my_dict1 = {b:a, c:tuple(d)}

print(my_dict)
print(my_dict1)