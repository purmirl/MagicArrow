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
def isHexData(_data):
    result = 0
    tempKey = 0
    hexData = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    if _data in hexData:
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
def isHardwareAddress(_hardwareAddress):
    result = 1 # if hardware address : 1,   else : 0
    length = len(_hardwareAddress)

    if length != 17:
        result = 0
        return result

    for i in range(1, length + 1):
        if (i % 3) == 0:
            if _hardwareAddress[i - 1] != ':':
                result = 0
                return result
        elif isHexData(_hardwareAddress[i - 1]) == 0:
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
def parseProtocolAddress(_protocolAddress):
    length = len(_protocolAddress)
    a = ""
    b = ""
    c = ""
    d = ""

    # return value : Integer a, b, c, d
    for i in range(0, length):
        if _protocolAddress[i] == '.':
            flags = i
            break
        a = a + _protocolAddress[i]

    for i in range(flags + 1, length):
        if _protocolAddress[i] == '.':
            flags = i
            break
        b = b + _protocolAddress[i]

    for i in range (flags + 1, length):
        if _protocolAddress[i] == '.':
            flags = i
            break
        c = c + _protocolAddress[i]

    for i in range (flags + 1, length):
        d = d + _protocolAddress[i]

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
def isProtocolAddress(_protocolAddress):
    result = 1 # if protocol address : 1,   else : 0
    length = len(_protocolAddress)
    protocolAddressData = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # check length
    # example : 127.0.0.1.2.3.4214214123123
    if length < 7 | length > 15:
        result = 0
        return result

    # check another character
    # example : 127.0:0.1
    for i in range(0, length):
        if _protocolAddress[i] not in protocolAddressData:
            result = 0
            return result

    # check dot position
    # example : .127.0.0.1
    if _protocolAddress[0] == '.':
        result = 0
        return result
    elif _protocolAddress[length - 1] == '.':
        result = 0
        return result

    dotCount = 0
    for i in range(1, length + 1):
        if _protocolAddress[i - 1] == '.':
            dotCount += 1
    if dotCount == 0 | dotCount > 3:
        result = 0
        return result

    isPreDot = 0
    for i in range(0, length):
        if _protocolAddress[i] == '.':
            if isPreDot == 1:
                result = 0
                return result
            else:
                isPreDot = 1
        else:
            isPreDot = 0

    parseResult = parseProtocolAddress(_protocolAddress)
    if (len(parseResult[0]) > 1) & (parseResult[0][0] == '0'):
        result = 0
        return result
    elif (len(parseResult[1]) > 1) & (parseResult[1][0] == '0'):
        result = 0
        return result
    elif (len(parseResult[2]) > 1) & (parseResult[2][0] == '0'):
        result = 0
        return result
    elif (len(parseResult[3]) > 1) & (parseResult[3][0] == '0'):
        result = 0
        return result

    if (int(parseResult[0]) < 0) | (int(parseResult[0]) > 255):
        result = 0
        return result
    elif (int(parseResult[1]) < 0) | (int(parseResult[1]) > 255):
        result = 0
        return result
    elif (int(parseResult[2]) < 0) | (int(parseResult[2]) > 255):
        result = 0
        return result
    elif (int(parseResult[3]) < 0) | (int(parseResult[3]) > 255):
        result = 0
        return result

    return result