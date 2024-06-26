# Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки:  
# Строки нумеруются начиная с единицы;  
# Слова выводятся отсортированными согласно кодировки Unicode.  
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.  

def print_words(text):
    words = text.lower().split()
    max_len = max(len(word) for word in words )
    for i, word in enumerate(sorted(words), start=1):
        line = f'{i}. {word:>{max_len}}'
        print(line)

text = "Вывести функцией каждое слово с новой строки"
print_words(text)