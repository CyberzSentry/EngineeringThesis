
def pesel(snip, content):
    snip = snip[1:-1]
    weight = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
    checksum = (int(snip[0]) * weight[0]) + (int(snip[1]) * weight[1]) + (int(snip[2]) * weight[2]) + (int(snip[3]) * weight[3])+ (int(snip[4]) * weight[4]) + \
        (int(snip[5]) * weight[5]) + (int(snip[6]) * weight[6]) + (int(snip[7]) * weight[7]) + (int(snip[8]) * weight[8]) + (int(snip[9]) * weight[9])

    if checksum%10 == int(snip[-1]):
        return True
    else:
        return False

def idnum(snip, content):
    weight = [7, 3, 1, 0, 7, 3, 1, 7, 3]
    key = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, \
        "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}

    snip_ready = snip.replace(" ", "").upper()
    checksum = (key[snip_ready[0]] * weight[0]) + (key[snip_ready[1]] * weight[1]) + (key[snip_ready[2]] * weight[2]) + (int(snip_ready[3]) * weight[3]) + \
        (int(snip_ready[4]) * weight[4]) + (int(snip_ready[5]) * weight[5]) + (int(snip_ready[6]) * weight[6]) + (int(snip_ready[7]) * weight[7]) + (int(snip_ready[8]) * weight[8])

    if checksum%10 == int(snip_ready[3]):
        return True
    else:
        return False

def passwd(snip, content):
    specialChars = "!@#$%^&*()_+-={}[];:\"'\\|<>?,./"
    nums = "0123456789"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    containsSpecial = False
    containsNum = False
    containsChars = False
    containsLow = False
    containsUpper = False

    for num in nums:
        if num in snip:
            containsNum = True
            break

    if not containsNum:
        return False

    for char in specialChars:
        if char in snip:
            containsSpecial = True
            break
    
    if not containsSpecial:
        return False
    
    for low in lowers:
        if low in snip:
            containsLow = True
            break

    if not containsLow:
        return False

    for up in uppers:
        if up in snip:
            containsUpper = True
            break

    if not containsUpper:
        return False
    else:
        return True
    
