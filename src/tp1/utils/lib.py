from scapy.all import *

def choose_interface() -> str:
    """
    Return network interface and input user choice

    :return: network interface
    """
    print('Select the number of the network interface to capture on.')
    relevant_interfaces = list_relevant_interfaces()
    for i, (iface ,ip) in enumerate (relevant_interfaces):
        print(f'{i}: {iface} : {ip}')
    is_valid = False
    while is_valid != True :
        interface_index = int(input('Network interface: '))
        if interface_index == '':
            print('Blank ?')
        elif interface_index > (len(relevant_interfaces) - 1) or interface_index < 0:
            print('Invalid network interface')
        else :
            interface = relevant_interfaces[interface_index]
            is_valid = True
    return interface

def list_relevant_interfaces() -> list[tuple[str, str]]:

    all_interfaces = get_if_list()

    relevant_interfaces = [
        (iface, ip)
        for iface in all_interfaces
        if (ip := get_if_addr(iface)) is not None
        and ip != '0.0.0.0' and ip != '127.0.0.1'
    ]

    return relevant_interfaces