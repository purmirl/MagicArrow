"""
 Copyright 2020 PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Magic Arrow Project by PeTrA. 2020
 MagicArrow 1.0
 Language : Python3.8.2
 Library : Scapy2.4.3

 Packet Launcher :: ARP (Address Resolution Protocol)
 ------
 @ function.py
    * function python code -> my utility function's code
"""

# MagicArrow/src/function.py


""" isHexData function
        check that is hex data
        :parameter
            _data : hex data
        :return
            if hex data : return 1
            else : return 0
"""
def is_hex_data(_data):
    result = 0
    temp_key = 0
    hex_data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    if _data in hex_data:
        result = 1
        return result
    else:
        result = 0
        return result

    return result

""" isHardwareAddress function
        check that is hardware address (mac address)
        :parameter
            _hardwareAddress
        :return
            if hardware address : return 1
            else : return 0
"""
def is_hardware_address(_hardware_address):
    result = 1 # if hardware address : 1,   else : 0
    length = len(_hardware_address)

    if length != 17:
        result = 0
        return result

    for i in range(1, length + 1):
        if (i % 3) == 0:
            if _hardware_address[i - 1] != ':':
                result = 0
                return result
        elif is_hex_data(_hardware_address[i - 1]) == 0:
            result = 0
            return result

    return result

""" parseProtocolAddress function
        parse protocol address (ip address)
        :parameter
            _protocolAddress : ip address
        :return
            Integer list [a, b, c, d]
"""
def parse_protocol_address(_protocol_address):
    length = len(_protocol_address)
    a = ""
    b = ""
    c = ""
    d = ""

    # return value : Integer a, b, c, d
    for i in range(0, length):
        if _protocol_address[i] == '.':
            flags = i
            break
        a = a + _protocol_address[i]

    for i in range(flags + 1, length):
        if _protocol_address[i] == '.':
            flags = i
            break
        b = b + _protocol_address[i]

    for i in range (flags + 1, length):
        if _protocol_address[i] == '.':
            flags = i
            break
        c = c + _protocol_address[i]

    for i in range (flags + 1, length):
        d = d + _protocol_address[i]

    result = [a, b, c, d]
    return result
        
""" isProtocolAddress function
        check that is protocol address (ip address)
        :parameter
            _protocolAddress : ip address
        :return
            if protocol address : return 1
            else : return 0
"""
def is_protocol_address(_protocol_address):
    result = 1 # if protocol address : 1,   else : 0
    length = len(_protocol_address)
    protocol_address_data = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # check length
    # example : 127.0.0.1.2.3.4214214123123
    if length < 7 | length > 15:
        result = 0
        return result

    # check another character
    # example : 127.0:0.1
    for i in range(0, length):
        if _protocol_address[i] not in protocol_address_data:
            result = 0
            return result

    # check dot position
    # example : .127.0.0.1
    if _protocol_address[0] == '.':
        result = 0
        return result
    elif _protocol_address[length - 1] == '.':
        result = 0
        return result

    # check dot count
    # example : 127.0.0....1
    dot_count = 0
    for i in range(1, length + 1):
        if _protocol_address[i - 1] == '.':
            dot_count += 1
    if dot_count == 0 | dot_count > 3:
        result = 0
        return result

    # check continued dot
    # example : 127..0.0.1
    is_pre_dot = 0
    for i in range(0, length):
        if _protocol_address[i] == '.':
            if is_pre_dot == 1:
                result = 0
                return result
            else:
                is_pre_dot = 1
        else:
            is_pre_dot = 0

    # check 0 started number
    # example : 127.0.0.01
    parse_result = parse_protocol_address(_protocol_address)
    if (len(parse_result[0]) > 1) & (parse_result[0][0] == '0'):
        result = 0
        return result
    elif (len(parse_result[1]) > 1) & (parse_result[1][0] == '0'):
        result = 0
        return result
    elif (len(parse_result[2]) > 1) & (parse_result[2][0] == '0'):
        result = 0
        return result
    elif (len(parse_result[3]) > 1) & (parse_result[3][0] == '0'):
        result = 0
        return result

    # check number range
    # example : 256.255.255.255
    if (int(parse_result[0]) < 0) | (int(parse_result[0]) > 255):
        result = 0
        return result
    elif (int(parse_result[1]) < 0) | (int(parse_result[1]) > 255):
        result = 0
        return result
    elif (int(parse_result[2]) < 0) | (int(parse_result[2]) > 255):
        result = 0
        return result
    elif (int(parse_result[3]) < 0) | (int(parse_result[3]) > 255):
        result = 0
        return result

    return result