# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

list = []
new_list = []

number = int(input('Задайте длину списка  '))

while True:
    for i in range(number):
        list.append(int(input('Введите число  ')))
    break


for i in range(number):

    if list.count(list[i]) == 1:
        new_list.append(list[i])


print(list)
print(new_list)
