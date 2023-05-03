def gradient(lengh:int, startingColor:str, endingColor:str):
    if len(startingColor) > 6 or len(startingColor) < 6 or len(endingColor) > 6 or len(endingColor) < 6:
        return 'ERROR: Invalid hexadecimal expression.'

    lengh = lengh - 1
    result, toadd = [], []
        
    dr, dg, db = int(startingColor[:2], 16), int(startingColor[2:4], 16), int(startingColor[4:], 16)
    ar, ag, ab = int(endingColor[:2], 16), int(endingColor[2:4], 16), int(endingColor[4:], 16)

    increm = [(ar-dr)/lengh, (ag-dg)/lengh, (ab-db)/lengh]

    for i in range(3):
        tl = []
        for j in range(0, lengh):
            tl.append(j*increm[i])
        toadd.append(tl)
    
    for l in range(lengh):
        fr = dr + int(round(toadd[0][l]))
        fg = dg + int(round(toadd[1][l]))
        fb = db + int(round(toadd[2][l]))

        fr, fg, fb = str(hex(fr))[2:], str(hex(fg))[2:], str(hex(fb))[2:]
        
        if len(fr) < 2:
            fr = '0' + fr
        if len(fg) < 2:
            fg = '0' + fg
        if len(fb) < 2:
            fb = '0' + fb
        
        color = fr + fg + fb
        result.append(color)

    result.append(endingColor)
    return result
