# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

lst = ["р", "е", "ш", "е", "н", "и", "е", "з", "а", "д", "а", "ч", "и"]
new_lst = set()

for i in lst:
    if lst.count(i) > 1:
        new_lst.add(i)

print(f"Первый список: ", lst)
print(f"Список дублирующих элементов без дубликатов: ", new_lst)