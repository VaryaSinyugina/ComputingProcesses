import math

def input_numbs(n, a):
    """Функция ввода массива"""

    for i in range(n):
    	a.append(float(input(f"[{i}] = ")))       
    return a

def find_sum(n, a):
    """Функция расчета суммы квадратов разницы эл-ов массива"""

    sum = 0
    for i in range(n):
        sum += (math.sqrt(abs(a[i])) - a[i])**2
    return sum