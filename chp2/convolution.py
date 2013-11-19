def makeIntArray(peptidestr):
    peptide = peptidestr.split(' ')
    temp = []
    for item in peptide:
        temp.append(int(item))
    return temp

def convolution(peptidestr):
    peptideX = makeIntArray(peptidestr)
    peptideY = peptideX[:]

    diffs = []
    for i in peptideX:
        for j in peptideY:
            if i-j > 0:
                diffs.append(i-j)
    diffs.sort()
    strReturn = " ".join(map(str, diffs))
    return strReturn
    
a = convolution('658 639 996 868 358 581 826 954 115 638 396 754 1069 128 210 0 1054 256 356 57 729 524 952 656 1182 601 753 1010 313 314 230 771 1067 428 543 371 857 824 97 128 1067 287 1125 113 543 926 243 754 939 767 415 228 639 484 283 899 115 300 115 411 429 185 972 243 869 511 415 428 767 671 939 453 1054 997 172 1085 1067 698 786 543 895 639 641 526 128 811 882 325 544 1054 186 541')
print a
