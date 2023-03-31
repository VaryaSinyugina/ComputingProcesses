__author__ = "Варвара Синюгина ИВТ-20"
"""
Задача №2 (44)
https://ivtipm.github.io/Programming/Glava02/index02.htm#z44"""

x = float(input("Введите действительное число x:"))
y = float(input("Введите действительное число y:"))
z = float(input("Введите действительное число z:"))

sum = x + y + z

if (sum < 1):
    # x - min
    if (x < y) and (x < z):
        x = (y + z) / 2

    # y - min
    elif (y < x) and (y < z):
        y = (x + z) / 2
        
    # z - min
    elif (z < x) and (z < y):
        z = (x + y) / 2
else:
    if (x < y):
        x = (y + z) / 2
    elif (y < x):
        y = (x + z) / 2

print("Измененные значения")
print(f"x: {x:.3f}")
print(f"y: {y:.3f}")
print(f"z: {z:.3f}")