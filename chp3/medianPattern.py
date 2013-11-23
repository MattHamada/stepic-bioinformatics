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


def medianPattern(dnas, k):
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
dnas = ['TTACCTTCTTGGGTCGCCCAGATTATAATCCGTGAGAGAAAC',
'TACAATCTTTTGCGCAGCTTACCTTTGTTTAGGCATCGACCC',
'TTAACTGCTAGTCCGCATAAGATTCCTTTAAGACTATGCCTA',
'TCTCTGCGCCGTGCCGACTTACCTGCGGCAGGCGCGTTAAAC',
'TTACCTTACTCTGGACCAGCATATAGCAAGCGAAAACGCGAC',
'TTATCTGTGTCGCGGGGACTGAAGCCTCCGTTCACCTAAATC',
'ATTAATTTAACTCCTATGAAATGAACCATCTCTTTCTAAGGT',
'GAAGGAATTAATAGTGGGAAGTCCCTCTTGTAAGACTTACCT',
'TGGGCACCTGGATAATGGCCAGACTTAGCTCCGTATCTAGAA',
'TCCTTGTTACAGACTGGGAAGCCAGGATAATTATCTGTAAAG']
##dnas = ['ttaccttaac',
##'gatatctgtc',
##'acggcgttcg',
##'ccctaaagag',
##'cgtcagaggt',]
a = medianPattern(dnas, 6)
print a
