# Objetivo: Organizar os números inseridos em ordem crescente

import os

os.system('cls')

list = []
list1 = []

x = int(input('Valor:'))
y = int(input('Valor:'))
z = int(input('Valor:'))

list.append(x)
list.append(y)
list.append(z)

l = list.copy()

for n in list:
    aa = max(list)
    list1.append(max(list))
    list.pop(list.index(aa))

    if len(list) == 1:
        list1.append(min(list))
        list1.reverse()

    os.system('cls')

    print('Numeros inseridos: {}\nResultado final:   {}\n\n'.format(l,list1))

