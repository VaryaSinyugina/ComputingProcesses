__author__ = "Варвара Синюгина ИВТ-20"
"""
Задача №7 (320)
https://ivtipm.github.io/Programming/Glava10/index10.htm#z320
"""
from func import find_rsum

n = int(input("Введите натуральное число n: ")) # ввод верхней границы первой суммы ряда
m = int(input("Введите натуральное число m: ")) # ввод верхней границы второй суммы ряда

sum = find_rsum(n, m) # нахождение суммы ряда 

print("Результат: " + str(sum))