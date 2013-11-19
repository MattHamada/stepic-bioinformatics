def peptideDa(peptide):
    total = 0
    for base in peptide:
        if   base == 'G':
            total += 57
        elif base == 'A':
            total +=  71
        elif base == 'S':
            total +=  87
        elif base == 'P':
            total +=  97
        elif base == 'V':
            total +=  99
        elif base == 'T':
            total +=  101
        elif base == 'C':
            total +=  103
        elif base == 'I' or base == 'L':
            total +=  113
        elif base == 'N':
            total +=  114
        elif base == 'D':
            total +=  115
        elif base == 'K' or base == 'Q':
            total +=  128
        elif base == 'E':
            total +=  129
        elif base == 'M':
            total +=  131
        elif base == 'H':
            total +=  137
        elif base == 'F':
            total +=  147
        elif base == 'R':
            total +=  156
        elif base == 'Y':
            total +=  163
        elif base == 'W':
            total +=  186
    return total


##def theospec(peptide):
##    spectrum = [0]
##    peptides = []
##    i = 0
##    while i < len(peptide):
##        if i+i < len(peptide):
##            spectrum.append(aminoDa(peptide[i:i+i]))
##        i+= 1
##    return spectrum
##print theospec('LEQN')

def theospec_rec(peptide, length, peptides):
    if length == 1:
        for base in peptide:
            peptides.append(base)
        return peptides
    elif length == len(peptide):
        peptides.append(peptide)
        return theospec_rec(peptide, len(peptide)-1, peptides)
    else:
        count = 0
        while count != len(peptide):
            if count+length <= len(peptide): 
                peptides.append(peptide[count:count+length])
                count += 1
            else:
                temp = peptide[count:] + peptide[0:length-len(peptide[count:])]
                peptides.append(temp)
                count+= 1
        return theospec_rec(peptide, length - 1, peptides)

def theospec_values(theospec):
    spectrum = [0]
    for fragment in theospec:
        spectrum.append(peptideDa(fragment))
    return spectrum

def massSpectrum(peptide):
    theospec = theospec_rec(peptide, len(peptide), [])
    values = sorted(theospec_values(theospec))
    return values
    #return sorted(theospec)

print  massSpectrum('NQEL')

#print spectrum('HSIMDVMRPGTDPA')
    
##
##theospec = theospec_rec('HSIMDVMRPGTDPA', len('HSIMDVMRPGTDPA'), [])
##
##
##b = sorted(theospec_values(theospec))
##s = ''
##for  num in b:
##    s += str(num) + ' '
##print s
##        
    
    
