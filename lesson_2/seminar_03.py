# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.  
# Функции bin и oct используйте для проверки своего результата, а не для решения.  
# Дополнительно:  
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления;  
# Избегайте магических чисел;  
# Добавьте аннотацию типов где это возможно.  

number: int = int(input ("Введите число: "))
base = int(input("Введите основание: "))
num = number

numbers = []
remained = base

while remained <= num:
    numbers.append(num % base)
    num = num // base
    
numbers.append(num)
numbers.reverse()

print(f'число {number} в {base} системе = {numbers}')
print(f"Двоичное число: {bin(number)}")
print(f"Восьмеричное число: {oct(number)}")