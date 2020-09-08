"""
 Copyright 2020 PeTrA. All rights reserved.
 . Python Project Structure Repository;
"""
# PythonProjectStructure/tests/package/main.py;

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

def isProtocolAddress(_protocolAddress):
    result = 1 # if protocol address : 1,   else : 0
    length = len(_protocolAddress)
    protocolAddressData = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if length < 7 | length > 15:
        result = 0
        return result

    for i in range(0, length):
        if _protocolAddress[i] not in protocolAddressData:
            result = 0
            return result

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
    if int(parseResult[0]) < 0 | int(parseResult[0]) > 255:
        result = 0
        return result
    elif int(parseResult[1]) < 0 | int(parseResult[1]) > 255:
        result = 0
        return result
    elif int(parseResult[2]) < 0 | int(parseResult[2]) > 255:
        result = 0
        return result
    elif int(parseResult[3]) < 0 | int(parseResult[3]) > 255:
        result = 0
        return result

    return result
##################################################################################################

sampleData = "00.0.0.0"
result1 = parseProtocolAddress(sampleData)
print(result1)

result2 = isProtocolAddress(sampleData)
# print(len(sampleData))
print(result2)






