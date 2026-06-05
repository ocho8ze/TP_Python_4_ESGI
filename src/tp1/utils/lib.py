from scapy.all import *
from tp1.utils.config import logger

def choose_interface() -> str:
    """
    Return network interface and input user choice

    :return: network interface
    """
    print('Select the number of the network interface to capture on.')

    relevant_interfaces = list_relevant_interfaces()
    for i, (iface ,ip) in enumerate (relevant_interfaces):
        print(f'{i}: {iface} : {ip}')

    while True :
        interface_index_raw = input('Network interface: ').strip()
        if interface_index_raw == '':
            logger.warning('Blank ?')
            continue
        try :
            interface_index = int(interface_index_raw)
        except ValueError:
            logger.warning('Not an integer')
            continue
        if interface_index > (len(relevant_interfaces) - 1) or interface_index < 0:
            logger.warning('Invalid network interface')
            continue
        return relevant_interfaces[interface_index][0]

def list_relevant_interfaces() -> list[tuple[str, str]]:

    all_interfaces = get_if_list()

    relevant_interfaces = [
        (iface, ip)
        for iface in all_interfaces
        if (ip := get_if_addr(iface)) is not None
        and ip != '0.0.0.0' and ip != '127.0.0.1'
    ]

    return relevant_interfaces