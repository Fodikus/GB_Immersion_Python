# Напишите функцию, которая принимает строку текста. 
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.  

def uni_code(txt):
    "Формирует список используемых символов по убываению"
    return sorted([ord(i) for i in set(txt)], reverse=True)

txt = "Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого"

print(uni_code(txt))