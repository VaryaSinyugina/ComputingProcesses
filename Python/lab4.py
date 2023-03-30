__author__ = "Варвара Синюгина ИВТ-20"
"""
Задача №4 (114б)
https://ivtipm.github.io/Programming/Glava04/index04.htm#z114"""

n = int(input("Введите n: "))
m = 0
for i in range(1, n):
    m += 1/i**3

print(f"Сумма: {m:.5f}")