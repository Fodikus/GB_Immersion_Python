# Пользователь вводит строку текста. 
# Вывести каждое слово с новой строки:
# Строки нумеруются начиная с единицы;  
# Слова выводятся отсортированными согласно кодировки Unicode;  
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.  

num_list = [1, 5, 7, -9, 0]

def sunnator(num_list: list[int], index_1: int, index_2: int) :
    if index_1 > index_2:
        return 0
    return sum(num_list[max(index_1, 0):min(index_2+1, len(num_list))])

print(sunnator(num_list, -3, 10))