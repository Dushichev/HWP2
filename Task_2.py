
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number_seq = int(input("введите число\n"))
multiplications = 1
for i in range(1, number_seq+1):
     multiplications *= i
     print(f"произведение = {multiplications}")     
    