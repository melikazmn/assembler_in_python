import IsRegister


def Sub(register, i, buffer, eax, ebx, ecx, edx):
    # Flags:
    zf = 0
    sf = 0
    cf = 0
    of = 0
    pf = 0

    while buffer[i] != ',':
        i += 1
    i += 1
    numberStartPoint = i

    isRegister, secondOp, i = IsRegister.isRegi(i, buffer, eax, ebx, ecx, edx)
    while i < len(buffer) and '0' <= buffer[i] <= '9':
        i += 1
    intReg = int("0b" + register, 2)

    if isRegister:
        intImi = int("0b" + secondOp, 2)

    elif i < len(buffer) and buffer[i] == "b" and (
            i == len(buffer) - 1 or buffer[i + 1:i + 4] == "add" or buffer[i + 1:i + 4] == "and" or buffer[
                                                                                                    i + 1:i + 4] == "sub" or buffer[
                                                                                                                             i + 1:i + 4] == "mov" or buffer[
                                                                                                                                                      i + 1:i + 3] == "or" or buffer[
                                                                                                                                                                              i + 1:i + 4] == "test" or buffer[
                                                                                                                                                                                                        i + 1:i + 4] == "cmp" or buffer[
                                                                                                                                                                                                                                 i + 1:i + 4] == "xor"):
        intImi = int("0b" + buffer[numberStartPoint:i], 2)

    elif i < len(buffer) and buffer[i] in "abcdefh" and buffer[i:i + 3] != "add" and buffer[
                                                                                     i:i + 3] != "and" and buffer[
                                                                                                           i:i + 3] != "cmp":
        hexNumber = "0x" + buffer[numberStartPoint:i]
        while buffer[i] != 'h':
            hexNumber += buffer[i]
            i += 1
        intImi = int(hexNumber, 16)

    else:
        if buffer[numberStartPoint] == '-':
            numberStartPoint += 1
            i += 1
            while i < len(buffer) and '0' <= buffer[i] <= '9':
                i += 1
            intImi = -1 * int(buffer[numberStartPoint:i])

        else:
            intImi = int(buffer[numberStartPoint:i])

    if intReg - intImi < 0:
        binNumber = bin(-1 * (intReg - intImi))[2:]
        if len(binNumber) <= len(register):
            register = "0" * (len(register) - len(binNumber)) + binNumber
        else:
            register = binNumber[(len(binNumber) - len(register)):]
        register = register.replace("1", "x")
        register = register.replace("0", "1")
        register = register.replace("x", "0")
        if len(bin(int(register, 2) + 1)[2:]) >= len(register):
            register = bin(int(register, 2) + 1)[2 - len(register) + len(bin(int(register, 2) + 1)[2:]):]
        else:
            register = "0" * (len(register) - len(bin(int(register, 2) + 1)[2:])) + bin(int(register, 2) + 1)[2:]

    else:
        binNumber = bin(intReg - intImi)[2:]
        if len(binNumber) <= len(register):
            register = "0" * (len(register) - len(binNumber)) + binNumber
        else:
            register = binNumber[(len(binNumber) - len(register)):]

    # setting flags:
    if register == len(register) * "0":
        zf = 1

    if intReg - intImi < 0:
        sf = 1

    if len(binNumber) > len(register) and intReg >= 0 and intImi >= 0:
        cf = 1

    if (intReg > 0 and intImi > 0 and register[0] == "1") or (intReg < 0 and intImi < 0 and register[0] == "0"):
        of = 1

    if register.count('1') % 2 == 0:
        pf = 1

    return register, i, zf, sf, cf, of, pf
