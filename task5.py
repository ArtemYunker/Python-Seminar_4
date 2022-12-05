
# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import re

path = 'file_1.txt'
data = open(path, 'r')
for line1 in data:
    print(line1)
data.close()

string1 = str(line1)


path = 'file_2.txt'
data = open(path, 'r')
for line2 in data:
    print(line2)
data.close()

string2 = str(line2)

result1 = re.findall('[0-9]+', string1)

result1.pop(1)
result1.pop(-1)
print(result1)

result2 = re.findall('[0-9]+', string2)

result2.pop(1)
result2.pop(-1)
print(result2)


new_list=[]
for i in range(len(result1)):
    new_list.append((int(result1[i])) + (int(result2[i])))

print(new_list)

uravn = 0
for i in range(1,len(new_list)+1):
    uravn = (f' ({new_list[i-1]}x^{len(new_list)-i+1}) + {uravn} ')
    
    if i == len(new_list) :
        uravn = (f' {uravn} + {new_list[-1]} = {0}')
        
print(uravn)
