import ADD
import AND
import Mov
import OR
import SUB
import XOR
#instructions : add sub and or xor test cmp mov
eax = 32 * '0'
intEax = 0
ebx = 32 * '0'
intEbx = 0
ecx = 32 * '0'
intEcx = 0
edx = 32 * '0'
intEdx = 0

zeroFlag = 0
signFlag = 0
carryFlag = 0
overflowFlag = 0
parityFlag = 0


def readBuffer():
    f = open("buffer.txt", "r")
    buff = f.read().replace(' ', '').replace("\n", "").lower()
    return buff


buffer = readBuffer()
print(buffer)

for i in range(len(buffer)):
    instruction = buffer[i:i + 3]

    if instruction == "mov":  #################### MOV
        i += 3
        if buffer[i:i + 3] == "eax":
            eax, i, zeroFlag = Mov.Mov(eax, i, buffer, eax, ebx, ecx, edx)
            print("Mov instruction ,eax:", eax)

        elif buffer[i:i + 2] == "ah":
            ah, i, zeroFlag = Mov.Mov(eax[16:24], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ah + eax[24:32]
            print("Mov instruction ,ah: ", ah)

        elif buffer[i:i + 2] == "ax":
            ax, i, zeroFlag = Mov.Mov(eax[16:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ax
            print("Mov instruction ,ax: ", ax)

        elif buffer[i:i + 2] == "al":
            al, i, zeroFlag = Mov.Mov(eax[24:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:24] + al
            print("Mov instruction ,al: ", al)


        elif buffer[i:i + 3] == "ebx":
            ebx, i, zeroFlag = Mov.Mov(ebx, i, buffer, eax, ebx, ecx, edx)
            print("Mov instruction ,ebx:", ebx)

        elif buffer[i:i + 2] == "bh":
            bh, i, zeroFlag = Mov.Mov(eax[16:24], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bh + ebx[24:32]
            print("Mov instruction ,bh: ", bh)

        elif buffer[i:i + 2] == "bx":
            bx, i, zeroFlag = Mov.Mov(ebx[16:33], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bx
            print("Mov instruction ,bx: ", bx)

        elif buffer[i:i + 2] == "bl":
            bl, i, zeroFlag = Mov.Mov(ebx[24:32], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:24] + bl
            print("Mov instruction ,bl: ", bl)


        elif buffer[i:i + 3] == "ecx":
            ecx, i, zeroFlag = Mov.Mov(ecx, i, buffer, eax, ebx, ecx, edx)
            print("Mov instruction ,ecx:", ecx)

        elif buffer[i:i + 2] == "ch":
            ch, i, zeroFlag = Mov.Mov(ecx[16:24], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + ch + ecx[24:32]
            print("Mov instruction ,ch: ", ch)

        elif buffer[i:i + 2] == "cx":
            cx, i, zeroFlag = Mov.Mov(ecx[16:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + cx
            print("Mov instruction ,cx: ", cx)

        elif buffer[i:i + 2] == "cl":
            cl, i, zeroFlag = Mov.Mov(ecx[24:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:24] + cl
            print("Mov instruction ,cl: ", cl)


        elif buffer[i:i + 3] == "edx":
            edx, i, zeroFlag = Mov.Mov(edx, i, buffer, eax, ebx, ecx, edx)
            print("Mov instruction ,edx:", edx)

        elif buffer[i:i + 2] == "dh":
            dh, i, zeroFlag = Mov.Mov(edx[16:24], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dh + edx[24:32]
            print("Mov instruction ,dh: ", dh)

        elif buffer[i:i + 2] == "dx":
            dx, i, zeroFlag = Mov.Mov(edx[16:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dx
            print("Mov instruction ,dx: ", dx)

        elif buffer[i:i + 2] == "dl":
            dl, i, zeroFlag = Mov.Mov(edx[24:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:24] + dl
            print("Mov instruction ,dl: ", dl)



    elif instruction == "add":  #################### ADD
        i += 3
        if buffer[i:i + 3] == "eax":
            eax, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(eax, i, buffer, eax, ebx, ecx, edx)
            print("Add instruction ,eax:", eax)

        elif buffer[i:i + 2] == "ah":
            ah, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(eax[16:24], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ah + eax[24:32]
            print("Add instruction ,ah: ", ah)

        elif buffer[i:i + 2] == "ax":
            ax, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(eax[16:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ax
            print("Add instruction ,ax: ", ax)

        elif buffer[i:i + 2] == "al":
            al, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(eax[24:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:24] + al
            print("Add instruction ,al: ", al)


        elif buffer[i:i + 3] == "ebx":
            ebx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(ebx, i, buffer, eax, ebx, ecx, edx)
            print("Add instruction ,ebx:", ebx)

        elif buffer[i:i + 2] == "bh":
            bh, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(ebx[16:24], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bh + ebx[24:32]
            print("Add instruction ,bh: ", bh)

        elif buffer[i:i + 2] == "bx":
            bx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(ebx[16:32], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bx
            print("Add instruction ,bx: ", bx)

        elif buffer[i:i + 2] == "bl":
            bl, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(ebx[24:32], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:24] + bl
            print("Add instruction ,bl: ", bl)


        elif buffer[i:i + 3] == "ecx":
            ecx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(ecx, i, buffer, eax, ebx, ecx, edx)
            print("Add instruction ,ecx:", ecx)

        elif buffer[i:i + 2] == "ch":
            ch, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(ecx[16:24], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + ch + ecx[24:32]
            print("Add instruction ,ch: ", ch)

        elif buffer[i:i + 2] == "cx":
            cx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(ecx[16:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + cx
            print("Add instruction ,cx: ", cx)

        elif buffer[i:i + 2] == "cl":
            cl, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(ecx[24:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:24] + cl
            print("Add instruction ,cl: ", cl)


        elif buffer[i:i + 3] == "edx":
            edx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(edx, i, buffer, eax, ebx, ecx, edx)
            print("Add instruction ,edx:", edx)

        elif buffer[i:i + 2] == "dh":
            dh, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(edx[16:24], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dh + edx[24:32]
            print("Add instruction ,dh: ", dh)

        elif buffer[i:i + 2] == "dx":
            dx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(edx[16:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dx
            print("Add instruction ,dx: ", dx)

        elif buffer[i:i + 2] == "dl":
            dl, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = ADD.Add(edx[24:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:24] + dl
            print("Add instruction ,dl: ", dl)


    elif instruction == "sub":  ################# SUB
        i += 3
        if buffer[i:i + 3] == "eax":
            eax, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(eax, i, buffer, eax, ebx, ecx, edx)
            print("Sub instruction ,eax:", eax)

        elif buffer[i:i + 2] == "ah":
            ah, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(eax[16:24], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ah + eax[24:32]
            print("Sub instruction ,ah: ", ah)

        elif buffer[i:i + 2] == "ax":
            ax, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(eax[16:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ax
            print("Sub instruction ,ax: ", ax)

        elif buffer[i:i + 2] == "al":
            al, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(eax[24:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:24] + al
            print("Sub instruction ,al: ", al)


        elif buffer[i:i + 3] == "ebx":
            ebx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ebx, i, buffer, eax, ebx, ecx, edx)
            print("Sub instruction ,ebx:", ebx)

        elif buffer[i:i + 2] == "bh":
            bh, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ebx[16:24], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bh + ebx[24:32]
            print("Sub instruction ,bh: ", bh)

        elif buffer[i:i + 2] == "bx":
            bx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ebx[16:33], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bx
            print("Sub instruction ,bx: ", bx)

        elif buffer[i:i + 2] == "bl":
            bl, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ebx[24:32], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:24] + bl
            print("Sub instruction ,bl: ", bl)


        elif buffer[i:i + 3] == "ecx":
            ecx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ecx, i, buffer, eax, ebx, ecx, edx)
            print("Sub instruction ,ecx:", ecx)

        elif buffer[i:i + 2] == "ch":
            ch, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ecx[16:24], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + ch + ecx[24:32]
            print("Sub instruction ,ch: ", ch)

        elif buffer[i:i + 2] == "cx":
            cx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ecx[16:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + cx
            print("Sub instruction ,cx: ", cx)

        elif buffer[i:i + 2] == "cl":
            cl, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ecx[24:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:24] + cl
            print("Sub instruction ,cl: ", cl)


        elif buffer[i:i + 3] == "edx":
            edx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(edx, i, buffer, eax, ebx, ecx, edx)
            print("Sub instruction ,edx:", edx)

        elif buffer[i:i + 2] == "dh":
            dh, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(edx[16:24], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dh + edx[24:32]
            print("Sub instruction ,dh: ", dh)

        elif buffer[i:i + 2] == "dx":
            dx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(edx[16:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dx
            print("Sub instruction ,dx: ", dx)

        elif buffer[i:i + 2] == "dl":
            dl, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(edx[24:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:24] + dl
            print("Sub instruction ,dl: ", dl)


    elif instruction == "and":  ################ AND  , zf, sf, pf
        carryFlag = 0
        overflowFlag = 0
        i += 3
        if buffer[i:i + 3] == "eax":
            eax, i, zeroFlag, signFlag, parityFlag = AND.And(eax, i, buffer, eax, ebx, ecx, edx)
            print("And instruction ,eax:", eax)

        elif buffer[i:i + 2] == "ah":
            ah, i, zeroFlag, signFlag, parityFlag = AND.And(eax[16:24], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ah + eax[24:32]
            print("And instruction ,ah: ", ah)

        elif buffer[i:i + 2] == "ax":
            ax, i, zeroFlag, signFlag, parityFlag = AND.And(eax[16:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ax
            print("And instruction ,ax: ", ax)

        elif buffer[i:i + 2] == "al":
            al, i, zeroFlag, signFlag, parityFlag = AND.And(eax[24:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:24] + al
            print("And instruction ,al: ", al)


        elif buffer[i:i + 3] == "ebx":
            ebx, i, zeroFlag, signFlag, parityFlag = AND.And(ebx, i, buffer, eax, ebx, ecx, edx)
            print("And instruction ,ebx:", ebx)

        elif buffer[i:i + 2] == "bh":
            bh, i, zeroFlag, signFlag, parityFlag = AND.And(ebx[16:24], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bh + ebx[24:32]
            print("And instruction ,bh: ", bh)

        elif buffer[i:i + 2] == "bx":
            bx, i, zeroFlag, signFlag, parityFlag = AND.And(ebx[16:32], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bx
            print("And instruction ,bx: ", bx)

        elif buffer[i:i + 2] == "bl":
            bl, i, zeroFlag, signFlag, parityFlag = AND.And(ebx[24:32], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:24] + bl
            print("And instruction ,bl: ", bl)


        elif buffer[i:i + 3] == "ecx":
            ecx, i, zeroFlag, signFlag, parityFlag = AND.And(ecx, i, buffer, eax, ebx, ecx, edx)
            print("And instruction ,ecx:", ecx)

        elif buffer[i:i + 2] == "ch":
            ch, i, zeroFlag, signFlag, parityFlag = AND.And(ecx[16:24], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + ch + ecx[24:32]
            print("And instruction ,ch: ", ch)

        elif buffer[i:i + 2] == "cx":
            cx, i, zeroFlag, signFlag, parityFlag = AND.And(ecx[16:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + cx
            print("And instruction ,cx: ", cx)

        elif buffer[i:i + 2] == "cl":
            cl, i, zeroFlag, signFlag, parityFlag = AND.And(ecx[24:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:24] + cl
            print("And instruction ,cl: ", cl)


        elif buffer[i:i + 3] == "edx":
            edx, i, zeroFlag, signFlag, parityFlag = AND.And(edx, i, buffer, eax, ebx, ecx, edx)
            print("And instruction ,edx:", edx)

        elif buffer[i:i + 2] == "dh":
            dh, i, zeroFlag, signFlag, parityFlag = AND.And(edx[16:24], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dh + edx[24:32]
            print("And instruction ,dh: ", dh)

        elif buffer[i:i + 2] == "dx":
            dx, i, zeroFlag, signFlag, parityFlag = AND.And(edx[16:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dx
            print("And instruction ,dx: ", dx)

        elif buffer[i:i + 2] == "dl":
            dl, i, zeroFlag, signFlag, parityFlag = AND.And(edx[24:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:24] + dl
            print("And instruction ,dl: ", dl)


    elif instruction[0:2] == "or":
        carryFlag = 0
        overflowFlag = 0
        i += 2
        if buffer[i:i + 3] == "eax":
            eax, i, zeroFlag, signFlag, parityFlag = OR.Or(eax, i, buffer, eax, ebx, ecx, edx)
            print("Or instruction ,eax:", eax)

        elif buffer[i:i + 2] == "ah":
            ah, i, zeroFlag, signFlag, parityFlag = OR.Or(eax[16:24], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ah + eax[24:32]
            print("Or  instruction ,ah: ", ah)

        elif buffer[i:i + 2] == "ax":
            ax, i, zeroFlag, signFlag, parityFlag = OR.Or(eax[16:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ax
            print("Or  instruction ,ax: ", ax)

        elif buffer[i:i + 2] == "al":
            al, i, zeroFlag, signFlag, parityFlag = OR.Or(eax[24:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:24] + al
            print("Or  instruction ,al: ", al)


        elif buffer[i:i + 3] == "ebx":
            ebx, i, zeroFlag, signFlag, parityFlag = OR.Or(ebx, i, buffer, eax, ebx, ecx, edx)
            print("Or  instruction ,ebx:", ebx)

        elif buffer[i:i + 2] == "bh":
            bh, i, zeroFlag, signFlag, parityFlag = OR.Or(ebx[16:24], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bh + ebx[24:32]
            print("Or  instruction ,bh: ", bh)

        elif buffer[i:i + 2] == "bx":
            bx, i, zeroFlag, signFlag, parityFlag = OR.Or(ebx[16:33], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bx
            print("Or  instruction ,bx: ", bx)

        elif buffer[i:i + 2] == "bl":
            bl, i, zeroFlag, signFlag, parityFlag = OR.Or(ebx[24:32], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:24] + bl
            print("Or  instruction ,bl: ", bl)


        elif buffer[i:i + 3] == "ecx":
            ecx, i, zeroFlag, signFlag, parityFlag = OR.Or(ecx, i, buffer, eax, ebx, ecx, edx)
            print("Or  instruction ,ecx:", ecx)

        elif buffer[i:i + 2] == "ch":
            ch, i, zeroFlag, signFlag, parityFlag = OR.Or(ecx[16:24], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + ch + ecx[24:32]
            print("Or  instruction ,ch: ", ch)

        elif buffer[i:i + 2] == "cx":
            cx, i, zeroFlag, signFlag, parityFlag = OR.Or(ecx[16:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + cx
            print("Or  instruction ,cx: ", cx)

        elif buffer[i:i + 2] == "cl":
            cl, i, zeroFlag, signFlag, parityFlag = OR.Or(ecx[24:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:24] + cl
            print("Or  instruction ,cl: ", cl)


        elif buffer[i:i + 3] == "edx":
            edx, i, zeroFlag, signFlag, parityFlag = OR.Or(edx, i, buffer, eax, ebx, ecx, edx)
            print("Or  instruction ,edx:", edx)

        elif buffer[i:i + 2] == "dh":
            dh, i, zeroFlag, signFlag, parityFlag = OR.Or(edx[16:24], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dh + edx[24:32]
            print("Or  instruction ,dh: ", dh)

        elif buffer[i:i + 2] == "dx":
            dx, i, zeroFlag, signFlag, parityFlag = OR.Or(edx[16:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dx
            print("Or  instruction ,dx: ", dx)

        elif buffer[i:i + 2] == "dl":
            dl, i, zeroFlag, signFlag, parityFlag = OR.Or(edx[24:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:24] + dl
            print("Or  instruction ,dl: ", dl)

    elif instruction + buffer[i+3:i+4] == "test":  ################ test  , zf, sf, pf
        carryFlag = 0
        overflowFlag = 0
        i += 4
        if buffer[i:i + 3] == "eax":
            notImportant, i, zeroFlag, signFlag, parityFlag = AND.And(eax, i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,eax:", eax)

        elif buffer[i:i + 2] == "ah":
            ah, i, zeroFlag, signFlag, parityFlag = AND.And(eax[16:24], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,ah: ", eax[16:24])

        elif buffer[i:i + 2] == "ax":
            ax, i, zeroFlag, signFlag, parityFlag = AND.And(eax[16:32], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,ax: ", eax[16:32])

        elif buffer[i:i + 2] == "al":
            al, i, zeroFlag, signFlag, parityFlag = AND.And(eax[24:32], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,al: ", eax[24:32])


        elif buffer[i:i + 3] == "ebx":
            notImportant, i, zeroFlag, signFlag, parityFlag = AND.And(ebx, i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,ebx:", ebx)

        elif buffer[i:i + 2] == "bh":
            bh, i, zeroFlag, signFlag, parityFlag = AND.And(ebx[16:24], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,bh: ", ebx[16:24])

        elif buffer[i:i + 2] == "bx":
            bx, i, zeroFlag, signFlag, parityFlag = AND.And(ebx[16:33], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,bx: ", ebx[16:32])

        elif buffer[i:i + 2] == "bl":
            bl, i, zeroFlag, signFlag, parityFlag = AND.And(ebx[24:32], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,bl: ", ebx[24:32])


        elif buffer[i:i + 3] == "ecx":
            notImportant, i, zeroFlag, signFlag, parityFlag = AND.And(ecx, i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,ecx:", ecx)

        elif buffer[i:i + 2] == "ch":
            ch, i, zeroFlag, signFlag, parityFlag = AND.And(ecx[16:24], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,ch: ", ecx[16:24])

        elif buffer[i:i + 2] == "cx":
            cx, i, zeroFlag, signFlag, parityFlag = AND.And(ecx[16:32], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,cx: ", ecx[16:32])

        elif buffer[i:i + 2] == "cl":
            cl, i, zeroFlag, signFlag, parityFlag = AND.And(ecx[24:32], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,cl: ", ecx[24:32])


        elif buffer[i:i + 3] == "edx":
            notImportant, i, zeroFlag, signFlag, parityFlag = AND.And(edx, i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,edx:", edx)

        elif buffer[i:i + 2] == "dh":
            dh, i, zeroFlag, signFlag, parityFlag = AND.And(edx[16:24], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,dh: ", edx[16:24])

        elif buffer[i:i + 2] == "dx":
            dx, i, zeroFlag, signFlag, parityFlag = AND.And(edx[16:32], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,dx: ", edx[16:32])

        elif buffer[i:i + 2] == "dl":
            dl, i, zeroFlag, signFlag, parityFlag = AND.And(edx[24:32], i, buffer, eax, ebx, ecx, edx)
            print("Test instruction,dl: ", edx[24:32])

    elif instruction == "cmp":  ################# CMP
        i += 3
        if buffer[i:i + 3] == "eax":
            notImportant, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(eax, i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,eax:", eax)

        elif buffer[i:i + 2] == "ah":
            ah, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(eax[16:24], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,ah: ", eax[16:24])

        elif buffer[i:i + 2] == "ax":
            ax, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(eax[16:32], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,ax: ", eax[16:32])

        elif buffer[i:i + 2] == "al":
            al, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(eax[24:32], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,al: ", eax[24:32])


        elif buffer[i:i + 3] == "ebx":
            notImportant, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ebx, i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,ebx:", ebx)

        elif buffer[i:i + 2] == "bh":
            bh, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ebx[16:24], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,bh: ", ebx[16:24])

        elif buffer[i:i + 2] == "bx":
            bx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ebx[16:33], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,bx: ", ebx[16:32])

        elif buffer[i:i + 2] == "bl":
            bl, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ebx[24:32], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,bl: ", ebx[24:32])


        elif buffer[i:i + 3] == "ecx":
            notImportant, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ecx, i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,ecx:", ecx)

        elif buffer[i:i + 2] == "ch":
            ch, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ecx[16:24], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,ch: ", ecx[16:24])

        elif buffer[i:i + 2] == "cx":
            cx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ecx[16:32], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,cx: ", ecx[16:32])

        elif buffer[i:i + 2] == "cl":
            cl, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(ecx[24:32], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,cl: ", ecx[24:32])


        elif buffer[i:i + 3] == "edx":
            notImportant, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(edx, i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,edx:", edx)

        elif buffer[i:i + 2] == "dh":
            dh, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(edx[16:24], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,dh: ", edx[16:24])

        elif buffer[i:i + 2] == "dx":
            dx, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(edx[16:32], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,dx: ", edx[16:32])

        elif buffer[i:i + 2] == "dl":
            dl, i, zeroFlag, signFlag, carryFlag, overflowFlag, parityFlag = SUB.Sub(edx[24:32], i, buffer, eax, ebx, ecx, edx)
            print("Cmp instruction ,dl: ", edx[24:32])

    elif instruction == "xor":##############XOR
        carryFlag = 0
        overflowFlag = 0
        i += 3
        if buffer[i:i + 3] == "eax":
            eax, i, zeroFlag, signFlag, parityFlag = XOR.Xor(eax, i, buffer, eax, ebx, ecx, edx)
            print("Xor instruction ,eax:", eax)

        elif buffer[i:i + 2] == "ah":
            ah, i, zeroFlag, signFlag, parityFlag = XOR.Xor(eax[16:24], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ah + eax[24:32]
            print("Xor instruction ,ah: ", ah)

        elif buffer[i:i + 2] == "ax":
            ax, i, zeroFlag, signFlag, parityFlag = XOR.Xor(eax[16:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:16] + ax
            print("Xor instruction ,ax: ", ax)

        elif buffer[i:i + 2] == "al":
            al, i, zeroFlag, signFlag, parityFlag = XOR.Xor(eax[24:32], i, buffer, eax, ebx, ecx, edx)
            eax = eax[:24] + al
            print("Xor instruction ,al: ", al)


        elif buffer[i:i + 3] == "ebx":
            ebx, i, zeroFlag, signFlag, parityFlag = XOR.Xor(ebx, i, buffer, eax, ebx, ecx, edx)
            print("Xor instruction ,ebx:", ebx)

        elif buffer[i:i + 2] == "bh":
            bh, i, zeroFlag, signFlag, parityFlag = XOR.Xor(ebx[16:24], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bh + ebx[24:32]
            print("Xor instruction ,bh: ", bh)

        elif buffer[i:i + 2] == "bx":
            bx, i, zeroFlag, signFlag, parityFlag = XOR.Xor(ebx[16:33], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:16] + bx
            print("Xor instruction ,bx: ", bx)

        elif buffer[i:i + 2] == "bl":
            bl, i, zeroFlag, signFlag, parityFlag = XOR.Xor(ebx[24:32], i, buffer, eax, ebx, ecx, edx)
            ebx = ebx[:24] + bl
            print("Xor instruction ,bl: ", bl)


        elif buffer[i:i + 3] == "ecx":
            ecx, i, zeroFlag, signFlag, parityFlag = XOR.Xor(ecx, i, buffer, eax, ebx, ecx, edx)
            print("Xor instruction ,ecx:", ecx)

        elif buffer[i:i + 2] == "ch":
            ch, i, zeroFlag, signFlag, parityFlag = XOR.Xor(ecx[16:24], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + ch + ecx[24:32]
            print("Xor instruction ,ch: ", ch)

        elif buffer[i:i + 2] == "cx":
            cx, i, zeroFlag, signFlag, parityFlag = XOR.Xor(ecx[16:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:16] + cx
            print("Xor instruction ,cx: ", cx)

        elif buffer[i:i + 2] == "cl":
            cl, i, zeroFlag, signFlag, parityFlag = XOR.Xor(ecx[24:32], i, buffer, eax, ebx, ecx, edx)
            ecx = ecx[:24] + cl
            print("Xor instruction ,cl: ", cl)


        elif buffer[i:i + 3] == "edx":
            edx, i, zeroFlag, signFlag, parityFlag = XOR.Xor(edx, i, buffer, eax, ebx, ecx, edx)
            print("Xor instruction ,edx:", edx)

        elif buffer[i:i + 2] == "dh":
            dh, i, zeroFlag, signFlag, parityFlag = XOR.Xor(edx[16:24], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dh + edx[24:32]
            print("Xor instruction ,dh: ", dh)

        elif buffer[i:i + 2] == "dx":
            dx, i, zeroFlag, signFlag, parityFlag = XOR.Xor(edx[16:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:16] + dx
            print("Xor instruction ,dx: ", dx)

        elif buffer[i:i + 2] == "dl":
            dl, i, zeroFlag, signFlag, parityFlag = XOR.Xor(edx[24:32], i, buffer, eax, ebx, ecx, edx)
            edx = edx[:24] + dl
            print("Xor instruction ,dl: ", dl)

print(
    "ZeroFlag = " + str(zeroFlag) + "   SignFlag = " + str(signFlag) + "    CarryFlag = " + str(
        carryFlag) + "  OverflowFlag = " + str(overflowFlag) + "    ParityFlag = " + str(parityFlag))
