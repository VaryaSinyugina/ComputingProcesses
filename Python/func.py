import math
import numpy as np

def input_numbs(n):
    """Функция ввода массива"""

    a = []	# массив действительных чисел

    for i in range(n):
    	a.append(float(input(f"[{i}] = ")))       
    return a

def random_numbs(n):
    """Функция создания массива рандомных чисел"""

    a = []	# массив действительных чисел

    for i in range(n):
    	a.append(np.random.randint(0, 50))       
    return a

def find_sum(a: list):
    """Функция расчета суммы квадратов разницы эл-ов массива a"""

    sum = 0
    for i in range(len(a)):
        sum += (math.sqrt(abs(a[i])) - a[i])**2
    return sum

def find_rsum(n :int, m :int):
	"""Функция нахождения суммы ряда"""

	sum = 0
	for k in range(n):
		for l in range(m):
			sum += (k**3) * ((k - l)**2)
	return sum

def find_odd(a: list):
	"""Функция нахождения кол-ва нечетных эл-ов массива а"""

	k = 0
	for i in range(len(a)):
		if a[i] % 2:
			k += 1
	return k