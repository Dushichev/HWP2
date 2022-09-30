# Задайте список из n чисел последовательности : [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции (случайные) хранятся в файле file.txt
#  (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
#Пример:
#Файл:
#4
#5
#2
#N = 3 => [-3, -2, -1, 0, 1, 2, 3]
#Результат: 1*2*(-1) = -2
import math
import random

number_n = int(input('Введите число\n'))
new_list = []
for i in range(-number_n,number_n+1):
    if i !=0:
        new_list.append(i)
print(f"список чисел от {-number_n} до {number_n} = {new_list}")
    

def Mult_get():
    with open('chisla.txt','w') as Task:
        new_list_2 =[] 
        composition_elem = 1                                             
        for i in range(0,number_n):                     
            num_spisok = int(random.randint(0,number_n*2-1))
            Task.write(str(num_spisok) + '\n')
            new_list_2.append(new_list[num_spisok])
            print(f"случайно сформированное число = {new_list[num_spisok]}")
            composition_elem = math.prod(new_list_2)
        return  composition_elem
           
print (f"произведение элементов находящихся под индексами из файла txt = {Mult_get()}")








