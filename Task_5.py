 #Реализуйте алгоритм перемешивания списка.

import random

list_algoritm = [random.randint(0,5) for i in range(random.randint(0,10))]
print(f"заданный  список:   {list_algoritm}")
random.shuffle(list_algoritm)
print(f"список после перемешивания:   {list_algoritm}")

