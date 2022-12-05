
# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

list = []

k = int(input('Введите степень К=  '))
uravnenie = 0

for i in range(1, k + 2):
    i = randint(1, 100)
    list.append(i)


print(list)

for i in range(1, k + 1):
    uravnenie = (f' ({list[i-1]}x^{k-i+1}) + {uravnenie} ')
    
    if i == k :
        uravnenie = (f' {uravnenie} + {list[-1]} = {0}')
        
print(uravnenie)


data = open('file.txt','w')
data.write(uravnenie)
data.close

