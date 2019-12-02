from pyzt import inputi,inputs
def n82(san):
    sum = 0
    for i in range(len(san)):
        en = int(san[i])
        res = en * (8 ** (len(san) - i - 1))
        sum += res
    l1 = []
    while True:
        c = sum % 2
        l1.append(c)
        b = sum // 2
        sum = b
        if b == 0:
            break
    for i in range(1, len(l1) + 1):
        s = l1[-i]
        print(s, end='')

def n810(san):
    sum = 0
    for i in range(len(san)):
        en = int(san[i])
        res = en * (8 ** (len(san) - i - 1))
        sum += res
    print(sum,end='')

def n816(san):
    sum = 0
    for i in range(len(san)):
        en = int(san[i])
        res = en * (8 ** (len(san) - i - 1))
        sum += res
    n1016(sum)


def n210(san):
    l2 = []
    a = 1
    sum = 0
    for i in san:
        l2.append(int(i))
    a1 = len(l2)
    for it in l2:
        sd = it * (2 ** (a1 - a))
        a1 -= 1
        if a == -1:
            break
        sum += sd
    print(sum,end='')
def n28(san):
    l2 = []
    l88 = []
    a = 1
    sum = 0
    for i in san:
        l2.append(int(i))
    a1 = len(l2)
    sum = 0
    for it in l2:
        sd = it * (2 ** (a1 - a))
        sum += sd
        a1 -= 1
        if a == -1:
            break
    if sum == 0 or sum == 1 or sum == 2 or sum == 3 or sum == 4 or sum == 5 or sum == 6 or sum == 7:
        print(sum,end='')
    else:
        while True:
            bytin = sum // 8
            if sum < 8:
                l88.append(sum)
                for elem in range(len(l88)):
                    print(l88[-elem - 1], end='')
                break
            kaldyk = sum % 8
            sum = bytin
            l88.append(kaldyk)
def n216(san):
    l2 = []
    a = 1
    for i in san:
        l2.append(int(i))
    a1 = len(l2)
    sum = 0
    for it in l2:
        sd = it * (2 ** (a1 - a))
        sum += sd
        a1 -= 1
        if a == -1:
            break
    n1016(sum)

def n102(san):
    l1 = []
    san_int=int(san)
    while True:
        c = san_int % 2
        l1.append(c)
        b = san_int// 2
        san_int = b
        if b == 0:
            break
    for i in range(1, len(l1) + 1):
        s = l1[-i]
        print(s, end='')

def n108(san):
    l8 = []
    en = int(san)
    if en == 0 or en == 1 or en == 2 or en == 3 or en == 4 or en == 5 or en == 6 or en == 7:
        print( en)
    else:
        while True:
            butin = en // 8
            if en <= 7:
                l8.append(en)
                for i in range(len(l8)):
                    print(l8[-i - 1], end='')
                break
            mod = en % 8
            en = butin
            l8.append(mod)

def n1016(num1):
    num=int(num1)
    l1 = []
    if num == 0 or num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9:
        print('10>>16: ', '0x' + str(num),end='')
    else:
        while True:
            butin = num // 16
            if num <= 15:
                l1.append(num)
                for i in range(len(l1)):
                    if l1[i] == 10:
                        l1[i] = 'A'
                    if l1[i] == 11:
                        l1[i] = 'B'
                    if l1[i] == 12:
                        l1[i] = 'C'
                    if l1[i] == 13:
                        l1[i] = 'D'
                    if l1[i] == 14:
                        l1[i] = 'E'
                    if l1[i] == 15:
                        l1[i] = 'F'
                l1.append('0x')
                for i in range(len(l1)):
                    print(l1[-i - 1], end='')
                break
            mod = num % 16
            num = butin
            l1.append(mod)
def do8(san):
    san_set8 = set('01234567')
    engiz_set = set(san)
    if len(engiz_set - san_set8) == 0 and san != '':
        print('''Таңда!!! 
        1- 8>>10
        2- 8>>2
        3- 8>>16
        0-quit''''')
        while True:
            tandau=inputs('\nТаңдауыңды енгіз:')
            if tandau=='1':
                n810(san)
            elif tandau=='2':
                n82(san)
            elif tandau=='3':
                n816(san)
            elif tandau=='0':
                break
def do2(san):
    byn_set = set('10')
    engiz_set = set(san)
    if len(engiz_set - byn_set) == 0 and san != '':
        print('''Таңда!!! 
                1- 2>>10
                2- 2>>8
                3- 2>>16
                0-quit''''')
        while True:
            tandau = inputs('\nТаңдауыңды енгіз:')
            if tandau=='1':
                n210(san)
            elif tandau=='2':
                n28(san)
            elif tandau=='3':
                n216(san)
            elif tandau=='0':
                break

def do10(san):
    on_set = set('0123456789')
    engiz_set = set(san)
    if len(engiz_set - on_set) == 0 and san != '':
        print('''Таңда!!! 
                        1- 10>>2
                        2- 10>>8
                        3- 10>>16
                        0-quit''''')
        while True:
            tandau = inputs('\nТаңдауыңды енгіз:')
            if tandau == '1':
                n102(san)
            elif tandau == '2':
                n108(san)
            elif tandau == '3':
                n1016(san)
            elif tandau=='0':
                break
def n1610(san):
    l = []
    for i in san:
        l.append(i)
    # l.remove(l[0])
    # l.remove(l[0])
    for i in range(2,len(l)):
        if l[i] == 'A':
            l[i] = 10
        if l[i] == 'B':
            l[i] = 11
        if l[i] == 'C':
            l[i] = 12
        if l[i] == 'D':
            l[i] = 13
        if l[i] == 'E':
            l[i] = 14
        if l[i] == 'F':
            l[i] = 15
    for i in range(2,len(l)):
        l[i] = int(l[i])
    sum = 0
    for i in range(2,len(l)):
        sum += l[len(l) - i - 3] * 16 ** (i-2)
    return sum
def n162(san):
    a=n1610(san)
    n102(a)
def n168(san):
    a=n1610(san)
    n108(a)

def do16(san):
    hex_set = set('0xABCDEF123456789')
    engiz_set = set(san)
    if len(engiz_set - hex_set) == 0 and san != '':
        print('''Таңда!!! 
                                1- 16>>2
                                2- 16>>8
                                3- 16>>10
                                0-quit''''')
        while True:
            tandau = inputs('\nТаңдауыңды енгіз:')
            if tandau == '1':
                n162(san)
            elif tandau == '2':
                n168(san)
            elif tandau == '3':
                print(n1610(san),end='')
            elif tandau == '0':
                break
def tanu():
    while True:
        byn_set = set('10')
        san_set8 = set('01234567')
        on_set=set('0123456789')
        hex_set=set('0xABCDEF123456789')
        san=inputs('Сан енгізіңіз:')
        engiz_set = set(san)
        if len(engiz_set - byn_set) == 0 and san != '':
            do2(san)
        elif len(engiz_set - on_set) == 0 and san != '':
            do10(san)
        elif len(engiz_set - san_set8) == 0 and san != '':
            do8(san)


        elif len(engiz_set-hex_set)==0 and san!='':
            do16(san)


tanu()