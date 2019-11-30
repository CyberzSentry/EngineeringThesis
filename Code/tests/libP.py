def pesel(snip):
    checksum = (int(snip[0]) * 9) + (int(snip[1]) * 7) + (int(snip[2]) * 3) + int(snip[3]) + (int(snip[4]) * 9) + \
        (int(snip[5]) * 7) + (int(snip[6]) * 3) + int(snip[7]) + (int(snip[8]) * 9 ) + (int(snip[9]) * 7)

    if checksum%10 == int(snip[-1]):
        return True
    else:
        return False