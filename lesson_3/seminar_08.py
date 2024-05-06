# Три друга взяли вещи в поход. 
# Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:  
# Какие вещи взяли все три друга;  
# Какие вещи уникальны, есть только у одного друга;  
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует;  
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.  

from os import name

def change_val():
    " Работа с именами переменных"
    my_var_name = [k for k in globals().keys() if not k.startswith('__')]
    print("Список без магических имен ", my_var_name, sep='\n')
    for i in my_var_name:
        if i[-1] =='s' and len(i) != 1:
            globals()[i[:-1]] = globals()[i]
            globals()[i] = None
    my_var_name_1 = [k for k in globals().keys() if not k.startswith('__')]
    print(my_var_name_1)
    print(globals())

def check_names() -> None:
    all_vars = ([(var, values) for var, values in globals().items() if not var.startswith('--')]) #  все глобальныу переменныe и их заначений в в иде кортежа: переменная - значение
    changed = {}
    for var in all_vars:
        if var[0] == 's':
            continue
        elif var[0].endswith('s') and len(var[0]) > 1:
            changed[var[0][:-1]] = var[1]      # var[0]:-1] - имя переменной без последней буквы, var[1] - значение перемнной
            changed[var[0]] = None
    for key in changed:
        globals()[key] = changed.get(key)

num, tasks, s = 1, 2, 3
change_val()
print(tasks, tasks)

# Другой вариант:
names, files, s = '1', 2, 3

print([var for var in globals() if not var.startswith('--')]) # печать по ключу всех наших переменных откидывая перемен6ные __
print(globals())
check_names()
print(globals())

print(names, name)      # переменная name создалась через globals  хотя и не обьявляясь в коде