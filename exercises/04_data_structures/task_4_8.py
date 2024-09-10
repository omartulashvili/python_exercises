# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный
поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ip = "192.168.3.1"

ip_split = ip.split('.') # ['192', '168', '3', '1']

bin_10 = '{0:<8} {1:<8} {2:<8} {3:<8}'.format(
    int(ip_split[0]),
    int(ip_split[1]),
    int(ip_split[2]),
    int(ip_split[3])
)

print(bin_10)

bin_2 = '{0:08b} {1:08b} {2:08b} {3:08b}'.format(
    int(ip_split[0]),
    int(ip_split[1]),
    int(ip_split[2]),
    int(ip_split[3])
) # 11000000 10101000 00000011 00000001

# bin_2 = '{0:8b} {1:8b} {2:8b} {3:8b}'.format(
#     int(ip_split[0]),
#     int(ip_split[1]),
#     int(ip_split[2]),
#     int(ip_split[3])
# ) # 11000000 10101000       11        1

print(bin_2)


