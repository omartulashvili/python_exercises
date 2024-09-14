# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network_input = input('Enter network: ')
mask_input = input('Enter mask: ')

# network_format = 'Network:' + '\n' '{}'.format(network_input)
# mask_format = 'Mask:' + '\n' '{}'.format(mask_input)

network_split = network_input.split('.')

network_bin_10 = '{0:<10} {1:<10} {2:<10} {3:<10}'.format(
    (network_split[0]),
    (network_split[1]),
    (network_split[2]),
    (network_split[3])
)

network_bin_2 = '{0:010b} {1:010b} {2:010b} {3:010b}'.format(
    int(network_split[0]),
    int(network_split[1]),
    int(network_split[2]),
    int(network_split[3])
)

mask_bin_10 = '{0:010b}'.format(int(mask_input))
mask_bin_2 = int(mask_input) * ("1" * 28 + "0" * 4)
print(mask_bin_2)

print('\n' + '-' * 30)

print('Network:' + '\n' + network_bin_10)
print(network_bin_2)





####### 10.1.1.0 #####