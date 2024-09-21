# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
get_network = input("Введи ip адрес: ")
ip_octets = get_network.split(".")
ip_correct = True

if len(ip_octets) == 4:
    ip_correct = False
else:
    for octets in ip_octets:
        if not octets.isdigit() and int(octets) in range(0,255):
            ip_correct = False
            break

ip_parts = int(get_network.split(".")[0])  # ['10', '0', '1', '1']

if ip_parts < 223:
    print("unicast")
elif 224 <= ip_parts <= 239:
    print("multicast")
elif get_network == "255.255.255.255":
    print("local broadcast")
elif get_network == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
