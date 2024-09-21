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
result = []

for line in f:
    get_list = line.rstrip("\n").split()[1:]
    result.append(get_list)

    prefix = get_list[0]
    ad_metric = get_list[1].strip('[]')
    next_hop = get_list[3].rstrip(',')
    last_update = get_list[4].rstrip(',')
    outbound_interface = get_list[5]

    formatted_output = template.format(prefix, ad_metric, next_hop, last_update, outbound_interface)
    print(formatted_output)



# # ['10.0.24.0/24', '[110/41]', 'via', '10.0.13.3,', '3d18h,', 'FastEthernet0/0']
# get_list = f.readline().rstrip("\n").split()[1::]
#
# prefix = get_list[0]
# ad_metric = get_list[1].strip('[]')
# next_hop = get_list[3].rstrip(',')
# last_update = get_list[4].rstrip(',')
# outbound_interface = get_list[5]
#
# result = template.format(prefix, ad_metric, next_hop, last_update, outbound_interface)
#
# # Prefix                10.0.24.0/24
# # AD/Metric             110/41
# # Next-Hop              10.0.13.3
# # Last update           3d18h
# # Outbound Interface    FastEthernet0/0
# print(result)



