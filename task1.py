#1. Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

n = int(input('Введите d   '))

c = round(pi,n)
print (c)