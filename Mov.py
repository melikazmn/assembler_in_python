import IsRegister


def Mov(register, i, buffer, eax, ebx, ecx, edx):
    # Flags:
    zf = 0

    while buffer[i] != ',':
        i += 1
    i += 1
    numberStartPoint = i

    isRegister, secondOp, i = IsRegister.isRegi(i, buffer, eax, ebx, ecx, edx)
    while i < len(buffer) and '0' <= buffer[i] <= '9':
        i += 1

    if isRegister:
        register = secondOp

    elif i < len(buffer) and buffer[i] == "b" and (
            i == len(buffer) - 1 or buffer[i + 1:i + 4] == "add" or buffer[i + 1:i + 4] == "and" or buffer[
                                                                                                    i + 1:i + 4] == "sub" or buffer[
                                                                                                                             i + 1:i + 4] == "mov" or buffer[
                                                                                                                                                      i + 1:i + 3] == "or" or buffer[
                                                                                                                                                                              i + 1:i + 4] == "test" or buffer[
                                                                                                                                                                                                        i + 1:i + 4] == "cmp" or buffer[
                                                                                                                                                                                                                                 i + 1:i + 4] == "xor"):

        lenNumber = i - numberStartPoint
        register = "0" * (len(register) - lenNumber) + buffer[numberStartPoint:i]

    elif i < len(buffer) and buffer[i] in "abcdefh" and buffer[i:i + 3] != "add" and buffer[
                                                                                     i:i + 3] != "and" and buffer[
                                                                                                           i:i + 3] != "cmp":
        hexNumber = "0x" + buffer[numberStartPoint:i]
        while buffer[i] != 'h':
            hexNumber += buffer[i]
            i += 1
        binValue = bin(int(hexNumber, 16))
        register = "0" * (len(register) - len(str(binValue[2:]))) + str(binValue[2:])

    else:
        if buffer[numberStartPoint] == '-':
            numberStartPoint += 1
            i += 1
            while i < len(buffer) and '0' <= buffer[i] <= '9':
                i += 1
            binNumber = bin(int(buffer[numberStartPoint:i]))
            register = "0" * (len(register) - len(binNumber) + 2) + binNumber[2:]
            register = register.replace("1", "x")
            register = register.replace("0", "1")
            register = register.replace("x", "0")
            register = bin(int(register, 2) + 1)[2:]
        else:
            binNumber = bin(int(buffer[numberStartPoint:i]))
            register = "0" * (len(register) - len(binNumber) + 2) + binNumber[2:]

    # setting flags:
    if register == len(register) * "0":
         zf = 1

    return register, i, zf
