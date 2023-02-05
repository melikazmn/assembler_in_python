def isRegi(i, buffer, eax, ebx, ecx, edx):
    if buffer[i:i + 3] == "eax":
        return True, eax, i + 3

    elif buffer[i:i + 2] == "ah":
        return True, eax[16:24], i + 2

    elif buffer[i:i + 2] == "ax":
        return True, eax[16:32], i + 2

    elif buffer[i:i + 2] == "al":
        return True, eax[24:32], i + 2


    elif buffer[i:i + 3] == "ebx":
        return True, ebx, i + 3

    elif buffer[i:i + 2] == "bh":
        return True, ebx[16:24], i + 2

    elif buffer[i:i + 2] == "bx":
        return True, ebx[16:33], i + 2

    elif buffer[i:i + 2] == "bl":
        return True, ebx[24:32], i + 2


    elif buffer[i:i + 3] == "ecx":
        return True, ecx, i + 3

    elif buffer[i:i + 2] == "ch":
        return True, ecx[16:24], i + 2

    elif buffer[i:i + 2] == "cx":
        return True, ecx[16:32], i + 2

    elif buffer[i:i + 2] == "cl":
        return True, ecx[24:32], i + 2


    elif buffer[i:i + 3] == "edx":
        return True, edx, i + 3

    elif buffer[i:i + 2] == "dh":
        return True, edx[16:24], i + 2

    elif buffer[i:i + 2] == "dx":
        return True, edx[16:32], i + 2

    elif buffer[i:i + 2] == "dl":
        return True, edx[24:32], i + 2
    else:
        return False, eax, i
