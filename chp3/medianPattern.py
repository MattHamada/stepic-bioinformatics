import itertools
def medianPattern(dnas, k):
    bestScore = 10000
    bestPattern = ''
    patterns = itertools.permutations('ATGC', k)
    for pattern in patterns:
        score = 0
        for dna in dnas:
            for i in range(len(dna)-k):
                kmer = dna[i:i+k]
                for i in range(len(pattern)):
                    #print 'i:', i
                    #print 'k:', k
                    #print 'kmer:', kmer
                    #print 'pattern:', pattern
                    if kmer[i] != pattern[i]:
                        score += 1
        if pattern == ('G','A','C'):
            print score
        if score < bestScore:
            bestScore = score
            bestPattern = pattern
            print pattern
    return pattern

dnas = ['AAATTGACGCAT',
              'GACGACCACGTT',
              'CGTCAGCGCCTG',
              'GCTGAGCACCGG',
              'AGTACGGGACAG']
a = medianPattern(dnas, 3)
print a
    
                
    
