
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

float_number = input('Введите число\n')

summa = 0
for i in float_number:
    if i != ',':
        summa += int(i)
print(f"сумма элементов числа {float_number} = {summa}")