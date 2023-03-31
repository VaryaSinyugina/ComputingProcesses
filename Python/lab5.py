__author__ = "Варвара Синюгина ИВТ-20"
"""
Задача №5 (136н)
https://ivtipm.github.io/Programming/Glava06/index06.htm#z136"""

from func import input_numbs, find_sum

n = int(input("Введите натуральное число n: "))

print(f"Введите {n} действительных чисел :")

arr = input_numbs(n)    # ввод чисел пользователя
res = find_sum(arr)	# вычисление результата 

print(f"Результат: {res:.5f}")