# Пользователь вводит строку текста:  
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним;  
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке;  
# Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.  

# Вариант 1
def income(input_dict: dict[str, list[int]]) -> bool:
    dict2 = {}
    for value, key in enumerate(input_dict):
        dict2[key] = sum(input_dict[key])
    print(dict2)
    if all(map(lambda x: x > 0, dict2.values())):
        return True
    else:
        return False

# Вариант 2
def income1 (input_dict: dict[str, list[int]]) -> bool:
        for key in input_dict:
            if sum(input_dict[key]) <= 0:
                return False
        return True

dict1 = {"company_1":[1, 2, 5, -8, 10, 36],
        "company_2":[-10, 2, -19, 7, -15, 36],
        "company_3":[10, 2, 19, -7, 11, 36]}

print(income(dict1))
print(income1(dict1))