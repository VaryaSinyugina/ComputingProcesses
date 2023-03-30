__author__ = "Варвара Синюгина ИВТ-20"
""" 
Задача №3 (66)
https://ivtipm.github.io/Programming/Glava03/index03.htm#z66"""

k = int(input("Введите целое k: "))
m = int(input("Введите целое m: "))

x = float(input("Введите действительное x: "))
y = float(input("Введите действительное y: "))
z = float(input("Введите действительное z: "))

if k < m*m :
    x = abs(x)
    y -= 0.5
    z -= 0.5
elif k == m*m :
    y = abs(y)
    x -= 0.5
    z -= 0.5
else:
    z = abs(z)
    y -= 0.5
    x -= 0.5

print(f"Значение x: {x:.5f}")
print(f"Значение y: {y:.5f}")
print(f"Значение z: {z:.5f}")

