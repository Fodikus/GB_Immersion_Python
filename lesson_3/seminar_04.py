# Создайте вручную список с повторяющимися элементами. 
# Удалите из него все элементы, которые встречаются дважды.

def my_sort(data: list[int | float]):
    for i in range(len(data) - 1):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[min_idx], data[i] = data[i], data[min_idx]

data = [2, 6, 7.5, 6, 10, -10]

print(data)
my_sort(data)
print(data)