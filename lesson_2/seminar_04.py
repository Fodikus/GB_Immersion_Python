# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.  
# Диаметр не превышает 1000 у.е.  
# Точность вычислений должна составлять не менее 42 знаков после запятой.  

from decimal import Decimal
import decimal
import math

while True:
    d = Decimal(input("введите диаметр окружности не более 1000\n"))
    if d > 1000 or d < 0:
        print("введите корректный диаметр от 0 до 1000")
    else:
        break

decimal.getcontext().prec = 42
l = 2 *Decimal(math.pi) * Decimal(d/2)
s = Decimal(math.pi) * Decimal(d/2**2)

print (f'длина окружности = {l}, площадь окружности = {s}')
print(len(str(l)), len(str(s)))