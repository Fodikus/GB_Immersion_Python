# Вручную создайте список с целыми числами, которые повторяются. 
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка. 
# Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

def print_words(text):
    words = text.lower().split()
    max_len = max(len(word) for word in words )

    for i, word in enumerate(sorted(words), start=1):
        line = f'{i}. {word:>{max_len}}'
        print(line)

text = "Вывести функцией каждое слово с новой строки"
print_words(text)