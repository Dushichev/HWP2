#Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.


number_sequence = int(input('Введите число\n'))
new_list =[]
summa_seq = 0
for i in range(1,number_sequence+1):
    summa_seq += (1+1/i)**i
    new_list.append(summa_seq)
print(f"список из числа {number_sequence}, последовательности 〖(1+1/{number_sequence})〗^{number_sequence} = {new_list}")
print(f"сумма чисел из списка {new_list} = {summa_seq}")