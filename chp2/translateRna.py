def translate(rna):
    protein = ''
    i = 0
    
    while i < len(rna)-2:
        codon = rna[i:i+3]
        
        if   codon == 'UUU' or codon == 'UUC':
            protein += 'F'
        elif codon == 'UUA' or codon == 'UUG' or \
             codon == 'CUU' or codon == 'CUC' or \
             codon == 'CUA' or codon == 'CUG':
            protein += 'L'
        elif codon == 'AUU' or codon == 'AUC' or \
             codon == 'AUA':
            protein += 'I'
        elif codon == 'AUG':
            protein += 'M'
        elif codon == 'GUU' or codon == 'GUC' or \
             codon == 'GUA' or codon == 'GUG':
            protein += 'V'
        elif codon == 'UCU' or codon == 'UCC' or \
             codon == 'UCA' or codon == 'UCG':
            protein += 'S'
        elif codon == 'CCU' or codon == 'CCC' or \
             codon == 'CCA' or codon == 'CCG':
            protein += 'P'
        elif codon == 'ACU' or codon == 'ACC' or \
             codon == 'ACA' or codon == 'ACG':
            protein += 'T'
        elif codon == 'GCU' or codon == 'GCC' or \
             codon == 'GCA' or codon == 'GCG':
            protein += 'A'
        elif codon == 'UAU' or codon == 'UAC':
            protein += 'Y'
        elif codon == 'CAU' or codon == 'CAC':
            protein += 'H'
        elif codon == 'CAA' or codon == 'CAG':
            protein += 'Q'
        elif codon == 'AAU' or codon == 'AAC':
            protein += 'N'
        elif codon == 'AAA' or codon == 'AAG':
            protein += 'K'
        elif codon == 'GAU' or codon == 'GAC':
            protein += 'D'
        elif codon == 'GAA' or codon == 'GAG':
            protein += 'E'
        elif codon == 'UGU' or codon == 'UGC':
            protein += 'C'
        elif codon == 'UGG':
            protein += 'W'
        elif codon == 'CGU' or codon == 'CGC' or \
             codon == 'CGA' or codon == 'CGG' or \
             codon == 'AGA' or codon == 'AGG':
            protein += 'R'
        elif codon == 'AGU' or codon == 'AGC':
            protein += 'S'
        elif codon == 'GGU' or codon == 'GGC' or \
             codon == 'GGA' or codon == 'GGG':
            protein += 'G'
            
        i+= 3
    return protein

f = open('output.txt', 'w')
a = translate('AUGAAGACCCUCGCUGGCGGUGGCGGGACGGUGGUAACUACCAGGAGAAUCAGGGCGAUCGUAGGUGGAUCAGAGACUCGUUUUAGCACCGAAUAUUCAGGAUGGAGCUGCCAAAGUUGGUGUCUGUUUCGUUUACUAAGGACCCUGAUAUAUCACCCUGGUUGUCUCCCAUCAUGUCAGGUCCCUGCACGACCAUCUACUAGUUCCUCACGUUCAAUAAUAGGUGCCCCCCCACUGUUUUUUAAGCGCCGAGUGAACACUGACUGCAUACGAAACGUCAAGCCCACCGUCUUCGAGCCAGCCUUUGCGCGGUCCUCCAGAAUUUCUCCACUGCGUCUGCGUCGGUGGACCGCUGCUGCUUCAUUAAUGCGUCAGCCCCCCGGACAGACGGUACUUCAUGGACUAGCUGUCGUAAGGGCUGCCAGGUCCUGGUCCCGCUGCUGUUGUGUCGUAUGUCGAAGGAAGAGUGUUUGUCUAGGUGCGGAAGGACGGGGUAAUCCCCUUCAGCAGGCAUCGACAAGCCAAUCCUACCUCGCACGAUGCGUUGGGGUCACCUGUAUUAAUGUACUGCAACUUGGGGCUGCUUUUUCGAAGGGUGAUGUCCUCCAGAUACUUAAAACUCUGGCGCUACUAAGCGGUCCUAACGCGUUACUAGCCGGUCAAUGCGUGAGCUCUAGUAACAGAGCUGGCCAGAAACGAUACGCGAUCGACGUCCAGAAUCGUACCUUGAGGCGUCAAAUCGUACCUCACGAGUGCUCGUCUAUCAUAGAUUGGCCCACAUGGAUUCUCUUACGAUCUGACGGACGGACUAUGACAGGUCCAUAUCUUCGGGGUUCAGGGGUUCCCGAUCGGCUGAUUAAUCCGAAGACCCUUGGAUGGAUAAGCCUGAACCAAAUGACAUUCAUCAAGUUCAAGUCACGACCCCCAUCUGGCGUAUCCCCGGACUUCAUUUGUGAUUGGAAUGCUACAAGAGCGGAGAGGUUUGGUAUAUCUAGAACCAGAGUGCUUAGGACUGGGUUAGGGAGCGUGAAGGCAAUAGUAAAGGCGAAUAUUAAAUUUACGGUCCGUCCGACGAUGGAAAUGUCUACACGAUGUCUGACGGUUUUCCGCAUGCCCACAGGCCAGCUACUGAUUUUUCCUCAAGGCGUCAUACGCGGCAUAACUAAGUGUGGUUUGGAUGCACAGCUGUUGAACUGGGAUUGGCUAAUAGCUCUUUCUAGAUCGGGACCCAAACCUCACCUUACCUGUAGGCCGCGAAAGCCCAGAAGUUCUUGUGGUAUUUGCACAGGAGCCCUAGGUCCGAAACAAGUUGCUAAUUCUUUGACGUUUACCUCCACCGCUCCUUUAAGUAGCAAAGAAAUACAUAGGACGGAUUCUUGGCCAAGAGUCGAGCUACCUGGCUACGAAGACAAGUCGACAUUCCCCGGGGCCGUACGUCUCCGCUCGUUCUUAUCGUUACCGAAUUUCGUUAUAUUCGGAACGGGCACCAAGCAACUGGUGGUGAUUAAACGAGAUGAGGUGAAUUUGUUGAGUACUCCGGUACCAAUAUGUGAGCCUCAUCUCAGAGGGCGAUUCUACUCUAGCAUUCAGGUUUAUGUGGCUAAUUCCGUCUUUUGUAUUCUUUGUUGCCUUCCUUGGAAUAUGAGUAUACUGUGUGUAUCACUAUAUGUCAUCCGUUGCGUGAUAAUUCUAUUUUCCAGAUCGUCGUUGGAUGAUGUCCGUGUCUACAUUGGUCGGGGUCGCAUAAAAAUAUCCCCCCGCCGGGCAGUACGUUCCACGCGGUUAUUGAAAGAAAGAAAGUCGAAUACGGCUAUAUAUGAGAGGGACACAUAUGGUUGGAGGCUUCGGACGUCAGUCGAUUACCCAGAUUCGGUGGAACCCCGUGUGGAUGUUGCUAGGGUUACUAUUUACGUAACCACGUUUUCUAAUAUAAUACCGACGAUUCUGGAUAUGUGUUUGACAAUUAGAGGGGGUAGAAGAUGCCCGUCUUUUAAUAGGCUCAGUACCAUCUCAAACCGUCGUGUUGAUGGUCUAGCAUACUACAGGUCGCAAUUUCGAGGAAUUCAACCUCGGGAUGCUGCGAUCCGUGUAGGAGUUACCUGCGGACAUCAAUUGGCUCAAAAAACAAUUUUGGGCCCUUCUGUUCUAACCACGGCCACACGAGGUCUGGGCCAGACGGAAAAGGACUCGAAAGUUUAUGAGGCUGACUGCGAGGAGAUUAACAAUACCAACGCAGGGUCUGAAAGUCACCUUACUGUUCUCCAAUCGUUCUUUGAUCGCUUCGAGAGUCGACAUAUGUUACUGAGGAUCUCCAUAUUUAGGCACAGUACUAGCUCGUUCCCAAGCAUGCGGGCGAAGGAGUCACAUGCCCAAAGUUCUUCAGACCUUAAGAUUCAUCUUAAAGUCGUGGCUCCCGUACACAUUCCAAGUGUGGGACAGAGGGCAGAUGCCACGGACGGGCACCCGCUGUUAUUAGGUAUAAGGGUAAGUGUUACCGCCGCCAUUCAGAGUGCCUCACUGUCGAAUCCAGCGAUUUGUUUAGAAGUAGGACUGAAGGAGCAGAAACAUGCUAAAGCCUGUAACCCUUUGUGCGUUCUCGCAUCCGCUUCUAAUACUAGAUCACAACGGCGAAAUCGCCACAGCUGGAACCGCUUACGCGUCAUAUUCCACGCCCUAAUUGCAGUCAUGGCCGACAGUGUAAGACGCCGUGUCAGAUGCUGCGGGCGUGCCUCGAGGCACGAACUGACGAUGCAUCAUGGACCAAGCGAACUCGCCCCCGGCAAGAAAGUGCGAUGGUUUACCAGACAUGUUCAUGCCGUAAUCCGGAUAGUACAGAAAGUGGACACCACUAAUGCGAGUUCCCAACACGGGUUCCUGUACCCCAUCCACCGGUACGCCCAGAGCAAUCGUCAGCAUUGGAUAUUCCGUCUGCCGACUCAGUGCCCAUCGUCCGUUACCUCUCUAUCCCGCCUAGCCGUCAGAGGAGGCCAAAAAGCCCAAUACCCGCAUACUGACUUCGAGUUCAAAUACUACAGGUUACUACGUGUUAUAAAAUCUAGCGUGAGGUUCAGAGCGCUUCUGGAAAGAGUUCAGAUGCUCCGUCGUAGCCCUGCCUUAUCGGGGCUUCGGAGCUCGGUCACGGCUCUCAGCCGGCUACCUGUCUGUCGCGACGGCCCACCCCUCUGCCCGCUGAAGGUUGAUAGUCCUGACACAUCCCAUACCAAAAAUGAACUUCAAUCGUUGGUCAUUGUCGCUAUGGUAAGCGGCGAUGCACAUGGUGUCCUACCACCCAAUAUCGCGAGUUCAGGAUGCCUCGAUCUGACUUGGUAUACAGCAUAUCGGGGUUAUCGACUUGUGCACAGGUCCAGACGCCCAUGCAAAACUUGUCCUCUACCACGAUUCCAUCGGAACCAGAGCGGCGUGAAGGCUACGAAUAAGCUGUCGUUCAAAUUUUUGCUACGGAGGAGAUUUAAUUCAAUGGCCUACCGUUAUCGUCUUUGGCAAAUUGCUCUAGGCUGGCAACGACAGAUGGGAAGAUUUAGAGCGGAGUUACAUGGAGAGAUAGCCCGAAUCGCAGUUAUAAAAGGGUGGUCCGAGCCUUGCGUCUCCGUACGUCUCCUAUGGGAUGAAAUUGCCUUAGUGCACUCUGGCGGGGAAAGGUCAGGACCUGUGCGAACAUGUGGUAUCUCCGAGCGGGGGAGAUCAAAAGGUCACUCACGGCACUUACGGGGGUCGGCCAUUGCUGUGGCGCGGCUUAUCCGAGACCCAUGUCAGGCGCAGAACCGCGAAUAUUGCGUUCCGGCGAGAUUGCUGGGGUAUCAUAAGCUAGUACUCCCCCAGCCGGAACCAUUCGCAGCUUGUGCCGCUCGCACCUCUUUGGCUAGCGAAAACACGUGUGUCAGUUACGGACUACUCUCAUUACUAGAGUUUGUGUGGACCAUCGAUGCAGCGCCGCUGGGGAAAAUAGGUGCGCAGGGCCCUAUCCUUAGCUGCAGAUCUAUGUAUUCCCCCAAGACCAUACACUCCCCUGGAUUAUUUAGCGACGAUCUUUUGGCCUACUUCCCUCUGCAGAGUGCACUGUUUAAGGCUUCGGAUUCCGUUAGUGGAGGUCCCAAGCCAUUCACAAUCACUAAUACAGUCUUGGCCGGCUCCGAACGCCAUACUUCUAAGCAUGCAAAGAAAGCUGGUACUAGAUCCGGUGAUGUCAUCGGCGCAAACGCGAAUCGAGCAGUGUUACGGUACAGGACGGUAUCGGACGAACUUCUCCAUGCUGUUCACAAUACCUACUGUAUUAAGUUAGCCACGUGGCCCGAAGCUUUAAAUCAUGAAGUUGUUCAAGGAGACGACCAUUACUACCGAAACGGUGGCGGGAAAGAUAACCCUCCUUUAAACACAAGGCCCCAUUUACGGAACCGUUCGUGUUGCCAUGACGCCUAUGCCAAAAACGGCACUCUAGGCGUGAAAUUCCGAAAGUCCGAGGAUUUCAUAAGCUUUGAUGGGUCGGCCGGUUGCACCUGCGUCGGCUGUACUCGGGCAUCCACAACACUAAGUACCCGACGCUGCGACAUGCGAGUGGUUUCAGCCCCGUUCUUUGUCGAUUCAAGAUCGCUAGAGGUAAGCCUGCAGCUAAAACAUCGGGUACGUCGCAGGCGGCGUCCCCGACGAGAGGCGGGCGUUACUCUUAAAAAACCUUCCCUGGGAUACAACUCAAGUUUACGUGGGAUGCUCCACAUAGGAAAAAGCUCGUCUAGGAUCCCUUCGGCGCCCUAUCGAUACAUACGGAUUCCAGUAAUGGCACUGACCACUAUCUGCUUGAGGAACCCAUGUGCCCGGGCCACAAAACUUUACAUUAAGUCCACCGAACGGUUUGAGCCUAAUGAUACUGGUUUCUUAAGCUUCGCUCGGGGGUUGGCGCGGCGUUAUUGGAGAUAUAGGGCCCUCCGUAGUGGCCGAGAGGAGGCCUUUCCAGUCAACCUAACUCUGAAAUCCGGCGACGCUCCCUACAGCCAAGACGCACAUAUCACGGGGCUAACUCGUUGCUCCACAACCUGUCCUCCUCCAACUAGACUAGAAGUGGGAAGAUCUAGUCAAUUUGGCCGCACUACAACAUAUAACCCCGCAAAGACUGCAAGCAUGGGUUCGGACAGCCGUCUAGUGGUUCAGGGAAUCCCUGGUCCAGUUGUAACCCUCAGGCCCCGGAGGAUUACUUGGGUCAGCGUUUUCCAAUCGUAUCGUGGGGUUGUGAGCGGCGUUGAUUGUCUACACAUUGGAGUGCUGCCCGAGGAGUGGAUGGGGGUAGGACCGAGGACAAAUACCACUUCACCAACUGCUAUGGUGGACCGAUGGAGGACUCGGACGAGGGACUGUGUGGGAUGUGGCCAGCCGUGUGUAGCGACUUCAUUGUGGCGUUCUUUACAUAUUCCCUCGCCGAAUAUGGGGGAAUCUCCGCAACCUAUGGUAUGGCUUUGUACUUGCAACACCGUUGACAGGUAUCUGGCUAGAAUGGGUGACUCGGUUCGUGCGCAGUUCUCGGGCCGUUCCGCCUAUAUACAGGAGCGACUGAAUCGGGGUACGCCCGUGGUAUCAAUACACGUGCGCUCUUUUGCCCGGAUGAUGUGCCCUCGGUGGAGUUUGCCUACUGGAUCAGGACAGACCGUUGAGACAAUGGCAUGCGACACGUCUAUGAAACCCUUAAGAGCAUUGUUGUGCGGGCACCCCUCGAAUUCGAGUGCAGCAAUAUGCAUUUAUGUAAUCAAGAAAUCCAACACAGGAUUAUGUCGUCUUUCCAGUCUAACAGCGCAUGCCAGGCUAUAUAAUUUUAUUACGAUGGUUGUGGGGACGCUGGUCCUGCAGGCUUUGGAUCCCACGAGACUCGGACCCCCCGAACAUUUGGCACAGGAUGCAGUCCAUUCCCCAGAGGGCGUAAAAUGGGACCUGCUGGUGGCUGGAAAUUACCUGCAACUUUCUUACCUCGUAAGACUUGCCAGCGUCCUGCGUUCAUGUGAGUUACCAAAAAAGACUCGUACCCUCUCAGGCAUUCUCCGGCCUGCACAUCACCUAGCCGUGCGAGCUAAACCUAUCGCACGGCCAAGUAACAGUCGUCAAGGUGUCGUAAAUCACUGUACGGAAGGCGUAUGCUGUCGCUGGCACUGCGAUCGCUUUAUAACUAGUUCCUUGAUGCGGAAUAAUUUCGCCACGAAUAGACUAAGCCAUGACGUUUCAGGGAACCGCUCACAGCACAACGUCUUGUCUUUACUGUUAUCUCGGAGCUUUCUGCCCAUAGUUAAGAGACAAGGUCUUGAUGGGCUCAUCCCCUAUAGCACUGAAUUUAGCGCCUCACCUACAGAGUGGGUACGCAAGGGCCUGAACCACCUACGGGGUGUUCUGCCGGGGUCGUGCAUCCUCGCAGGCAAAAAUUACCGCGAACAGAAGACCCUACACCUGUCGGCCUGUGUUACUCGAAGCCAUGGACCCUCUCAUAACCCGUCUACUGCACACACCGCAGGGAAUAGUAGAAAGAGACGCGUACUCGUCAGACACAUGAUUAGUGCCCCUCGUGCGCAGUCUUCUAGAUGCCCAAGCAAGAGCCGUCUAUCAACUCAGGUAUGUAAUGCUCGCCUGACCGCCCGACACAGUAAAAGAGCAUUCCCCGACAACGUUUGGUAUAGGAGGGCUGGUCUCCACACAGUCGUACAGACAACUGUAGCGAGAAACUAUAAGCACGCCGCACUCGGGUCCGGGGUUCGAACUUUUAGUCAUACCUAUCUUGUCUAUGGUCAAGAUUCAGAUAUACUCCAAAUAGGGUUACUAUGGGCCUCUCGCCUCUCACACGUUCGGACGCUCACCUUAGCUUAUUUAGUUUGGAGGUCCAAAGGCAACGGUCGUCCUCAAUUCGCUAUUUCAACCCCCCCGGUACGAAACUGCCCGGGGCAUCAAAAAUCAGAGGGCAGACUCGCACUUCGGGCGCCAAAAGGAGAUCGGCGACAGUUGGCAACUGGCCUCCGGCGCAUCGUGCCGGAUAGCCCCAUAUAUGUUACUUACAAAGAGAACGAAAUUACGACUCAUUUAAUGCUAAAAGGCUGUGUUAACAGGGCCCAGGACGCAAUGAACCAAGGCGGUCAGGGGAAUAGCCUAUUCCUCGCAGAGAUUCCGAAGAUGCUGGGCUACGGUGACACAUAUGCAACACCCAAUGCGUGUGCGAGGGCGGCGUUCGUUAAAGUCAAGCCUGUGACUAAAUUGGCGCUAGCUUCAGAGCGAUUCGAACUAUUGCCCUCCCUGACCAUCACCCAAGCUGAUGCACACUCUAAGAUCGGGAUUUCCCGAGCUGGAGCCCUCGGUUCUCAAGGCCCUUCCCAAACUGCGCGCUCCGCUACUACGCAGUAUGCGGAUCCUGGUGGGAAUUUUCGCAGGCAGCGGAGAACGACACCCUUGAUCGAAGGAGGUAAUAACGUGCACACGGGCCACUCGCGUCGUGCAUUAGGAGGCCAAGGCCCAUGUAUCGCUACCGCGCCUAGAAGAACCCCGGACAAAAGUCAACAAUUUUUCCCUGGAAUCAGCAGAUGGUUUGGGCUGCUCCAUGCAACAAUGCCCGGGCUAUGUUGGGCCGUACGACUGCCACGAUUGAAACCGCUUAGGCUUAGCACCCGUCAGGUAUCGUGUUCACUGAUACCUACGUACGCUGGUACGGGAACUAUUUACGCGUGGUUUCGAUCACCGCGUUCUAUGGCUUUACGCUCCCGUCGGGCCGACCAUCGGCGGAGGCGCCAGAGGCAGGUGAGGAGGGUAGUGCGCCCGGCGACUUCGCAUUACGUAGCGAAAGAACGCGUGACCGACUUUAAUAGCGAAGGGGCACCAUGCGUACUCUACGGCAGUACCAUGGCGGGGGAGUCACAGUUGCAGGUUAAUCAUUCCUAUCAAUCAUUUACUCCUGAAGCAAUCGCUUCUCCACUUUUUAAGCGUUAUCGCAACCCAAAUCAUCCGUGCGGCGACAUACUGUCGCAUGUGCCCAAAAGCUGGCAGUUAGCUUCGAUUUGUACUAGGCACAAGUGCCACACCUACGACGUCUAUUUGUGUAUAGCCAGCAAUGCGAUUUUCAAACUCGUAUGA')
f.write(a)
len(a)
f.close()
                 
        
