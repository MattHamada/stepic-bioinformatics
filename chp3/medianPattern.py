import itertools


def seqScore(dna, pattern):
    bestScore = 10000
    for i in range(len(dna)-len(pattern)+1):
        kmer = dna[i:i+len(pattern)]
        kmerScore = 0
        for j in range(len(kmer)):
            if kmer[j] != pattern[j]:
                kmerScore += 1
        if kmerScore < bestScore:
            bestScore = kmerScore
    return bestScore


    

def medianPatternOld(dnas, k):
    bestScore = 10000
    bestPattern = ''
    patterns = itertools.product('ATGC', repeat=k)
    for pattern in patterns:
        #print 'pattern:', pattern
        score = 0
        for dna in dnas:
          score += seqScore(dna, pattern)
        if score < bestScore:
            bestScore = score
            bestPattern = pattern
        #print bestScore
    return bestPattern
dnas = ['GATGGACCGGGC',
             'TAAAAAGGTATA',
             'AACCACGAGTAC',
             'TGTCATGTGCGG',
             'AACCTAAACCCT',
             'GTGCCCGATATG',
             'TAGTCTTCGAGG',
             'AGGAGACGTGTT',
             'TGTGGGGATCGT',
             'CGCAGTGCACTA',
             'TACTCGTAACTT',
             'GCTCTAGTACGC',
             'GAGACGGTCGTA',
             'GATCGGTGGCAG',
             'GTAGGTATCACC',
             'GTGGCTATCGCT',
             'TGAGCAGACCCG',
             'AGTGATCTGAGC',
             'CAAAATGGGAGT',
             'GTTGGTATCACC',
             'CCTCGGAAAACG',
             'GGCGGCTCCATC',
             'TACTAGTATAAG',
             'GTGGTTATCACC',
             'CATCACGCAATG']
##dnas = ['ttaccttaac',
##'gatatctgtc',
##'acggcgttcg',
##'ccctaaagag',
##'cgtcagaggt',]
#print medianPattern(dnas, 12)
