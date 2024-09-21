# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

f = open("ospf.txt")

# ['10.0.24.0/24', '[110/41]', 'via', '10.0.13.3,', '3d18h,', 'FastEthernet0/0']
get_list = f.readline().rstrip("\n").split()[1::]

result = template.format(*del_tab_ospf[0:1], *del_tab_ospf[1:2],
                         *del_tab_ospf[3:4],
                         *del_tab_ospf[4:5], *del_tab_ospf[5:6]
                         )

# f.readline - читаем каждую строку
# убираем спец символ \n с помощью rstrip
# убираем 0 и пробелы слева: как????
# затем разбиваем строку и с помощью format раскидываем
# кладем это все в цикл for