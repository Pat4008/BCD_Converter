def add_space(binary):
    temp = ''
    spaced = ''

    while len(binary) % 4 != 0:
        binary = '0' + binary

    for bit in binary:
        temp = temp + bit
        if len(temp) == 4:
            spaced = spaced + temp + ' '
            temp = ''
    return spaced


def unsigned_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = chr((decimal & 1) + 0x30) + binary
        decimal = decimal >> 1
    return binary


def unpacked_bcd(decimal):
    bcd = ''
    for unit in decimal:
        temp = unsigned_binary(int(unit))
        while len(temp) < 8:
            temp = '0' + temp
        bcd = bcd + temp
    return bcd


def packed_bcd(decimal):
    bcd = ''
    for unit in decimal:
        temp = unsigned_binary(int(unit))
        while len(temp) < 4:
            temp = '0' + temp
        bcd = bcd + temp
    return bcd


def densely_packed(packed):
    bcd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checker = []

    checker = [packed[0], packed[4], packed[8]]
    bcd[0] = checker[0]
    bcd[1] = checker[1]
    bcd[2] = checker[2]
    if checker == ['0', '0', '0']:
        bcd[9] = '0'

        bcd[3] = packed[1]
        bcd[4] = packed[2]
        bcd[5] = packed[3]

        bcd[6] = packed[5]
        bcd[7] = packed[6]
        bcd[8] = packed[7]

        bcd[10] = packed[9]
        bcd[11] = packed[10]
        bcd[12] = packed[11]

    elif checker == ['0', '0', '1']:
        bcd[9] = '1'
        bcd[5] = packed[3]
        bcd[8] = packed[7]
        bcd[12] = packed[11]

        bcd[3] = packed[1]
        bcd[4] = packed[2]

        bcd[6] = packed[5]
        bcd[7] = packed[6]

        bcd[10] = '0'
        bcd[11] = '0'

    elif checker == ['0', '1', '0']:
        bcd[9] = '1'
        bcd[5] = packed[3]
        bcd[8] = packed[7]
        bcd[12] = packed[11]

        bcd[3] = packed[1]
        bcd[4] = packed[2]

        bcd[6] = packed[9]
        bcd[7] = packed[10]

        bcd[10] = '0'
        bcd[11] = '1'

    elif checker == ['1', '0', '0']:
        bcd[9] = '1'
        bcd[5] = packed[3]
        bcd[8] = packed[7]
        bcd[12] = packed[11]

        bcd[3] = packed[9]
        bcd[4] = packed[10]

        bcd[6] = packed[5]
        bcd[7] = packed[6]

        bcd[10] = '1'
        bcd[11] = '0'

    elif checker == ['0', '1', '1']:
        bcd[9] = '1'
        bcd[5] = packed[3]
        bcd[8] = packed[7]
        bcd[12] = packed[11]

        bcd[3] = packed[1]
        bcd[4] = packed[2]

        bcd[6] = '1'
        bcd[7] = '0'

        bcd[10] = '1'
        bcd[11] = '1'

    elif checker == ['1', '0', '1']:
        bcd[9] = '1'
        bcd[5] = packed[3]
        bcd[8] = packed[7]
        bcd[12] = packed[11]

        bcd[3] = packed[5]
        bcd[4] = packed[6]

        bcd[6] = '0'
        bcd[7] = '1'

        bcd[10] = '1'
        bcd[11] = '1'

    elif checker == ['1', '1', '0']:
        bcd[9] = '1'
        bcd[5] = packed[3]
        bcd[8] = packed[7]
        bcd[12] = packed[11]

        bcd[3] = packed[9]
        bcd[4] = packed[10]

        bcd[6] = '0'
        bcd[7] = '0'

        bcd[10] = '1'
        bcd[11] = '1'

    elif checker == ['1', '1', '1']:
        bcd[9] = '1'
        bcd[5] = packed[3]
        bcd[8] = packed[7]
        bcd[12] = packed[11]

        bcd[3] = '0'
        bcd[4] = '0'

        bcd[6] = '1'
        bcd[7] = '1'

        bcd[10] = '1'
        bcd[11] = '1'

    del (bcd[0])
    del (bcd[0])
    del (bcd[0])
    return bcd


def densely_fixer(decimal):
    bcd = ''
    str1 = ''
    while len(decimal) % 3 != 0:
        decimal = '0' + decimal

    templist = [decimal[i:i + 3] for i in range(0, len(decimal), 3)]

    for part in templist:
        temp = densely_packed(packed_bcd(part))
        str1 = str1.join(temp)
        bcd = bcd + ' ' +str1
        str1 = ''

    return bcd

########################################################################################################################


while True:
    decimal = input("Decimal Input: ")
    # print(decimal)
    try:
        number = int(decimal)
    except ValueError:
        print("I am afraid " + decimal + " is not a number")
    else:
        if number >= 0:
            print('Unsigned Binary: ' + unsigned_binary(int(decimal)))
            print('Unpacked BCD: ' + add_space(unpacked_bcd(decimal)))
            print('Packed BCD: ' + add_space(packed_bcd(decimal)))
            print('Densely Packed BCD: ' + densely_fixer(decimal))
        else:
            print("Please enter a positive integer")
