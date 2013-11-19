from translateRna import translate
import itertools

###seqs = itertools.product(['A','U','G','C'], repeat=30)
##total = 0
##for i in seqs:
##    if translate(''.join(i)) == 'VKLFPWFNQY':
##        total += 1
##print total


def untranslate(peptide):
    results = []
    possibilities = 1
    for base in peptide:
        if base == 'V':
            results.append(('GUU','GUC','GUA','GUG'))
        elif base == 'K':
            results.append(('AAA','AAG'))
        elif base == 'L':
            results.append(('UUA','UUG','CUU','CUC','CUA','CUG'))
        elif base == 'F':
            results.append(('UUU','UUC'))
        elif base == 'P':
            results.append(('CCU','CCC','CCA','CCG'))
        elif base == 'W':
            results.append(('UGG',))
        elif base == 'N':
            results.append(('AAU','AAC'))
        elif base == 'Q':
            results.append(('CAA','CAG'))
        elif base == 'Y':
            results.append(('UAU','UAC'))
    for i in range(len(results)):
        possibilities *= len(results[i])
        print len(results[i])
    return possibilities
        
    
    
            
