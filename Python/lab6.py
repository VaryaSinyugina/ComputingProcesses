__author__ = "Варвара Синюгина ИВТ-20"
"""
Задача №6 (178а)
https://ivtipm.github.io/Programming/Glava07/index07.htm#z178
"""
from func import random_numbs, find_odd

n = int(input("Введите натуральное n: "))
k = 0

print(f"Массив {n} натуральных чисел :")

arr = random_numbs(n)    # массив рандомных чисел
print(arr)
res = find_odd(arr)     # вычисление результата
        
print(f"Результат: {res:.1f}")
