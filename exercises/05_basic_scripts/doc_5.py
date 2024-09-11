from sys import argv

interface = input('Enter interface type and number: ')
vlan = input('Enter VLAN number: ')

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))

##################

# argv = ['access_template_argv.py', 'Gi0/7', '4']
#
# interface = argv[1]
# vlan = argv[2]
#
# access_template = ['switchport mode access',
#                    'switchport access vlan {}',
#                    'switchport nonegotiate',
#                    'spanning-tree portfast',
#                    'spanning-tree bpduguard enable']
#
# print('interface {}'.format(interface))
# print('\n'.join(access_template).format(vlan))

####################
# access_template = ['switchport mode access',
#                    'switchport access vlan {}',
#                    'switchport nonegotiate',
#                    'spanning-tree portfast',
#                    'spanning-tree bpduguard enable']
#
# print('\n'.join(access_template).format(3))