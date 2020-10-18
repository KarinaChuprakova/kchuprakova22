import math

ITERATIONS = 20

def my_cos(x):
    """
    Вычисление косинуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        x_pow = x**2  # В цикле постепенно считаем степень
        multiplier *= -1 / (2*n-1) / (2*n)  # (-1)^n и факториал
        partial_sum += x_pow * multiplier
    
    return partial_sum

print (math.cos(0.4))
print (my_cos(0.4))
