import random
from greedyMotifSearch import makePseudoProfile, hammingDistance, profileMostProb, medianPattern
#from medianPattern import medianPattern


def getMotifs(profile, dnas, k):
    motifs = []
    for dna in dnas:
        motifs.append(profileMostProb(dna, k, profile))
    return motifs
            

def randomMotifs(dnas, k, t):
    bestMotifs = []
    for i in range(2000):
        for dna in dnas:        
            length = len(dna)
            startBase = random.randint(0, length-k)
            bestMotifs.append(dna[startBase:startBase+k])
        bestconsensus = medianPattern(bestMotifs)
        bestScore = hammingDistance(bestMotifs, bestconsensus)
        while True:
            profile = makePseudoProfile(bestMotifs)
            motifs = getMotifs(profile, dnas, k)
            consensus = medianPattern(motifs)
            score = hammingDistance(motifs, consensus)
            if score < bestScore:
                bestMotifs = motifs
                bestconsensus = consensus
                bestScore = score
            else:
                break
    print bestMotifs

dnas = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
              'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
              'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
              'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
              'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

f = open('randomMotifInput.txt', 'r')
line = f.readline().strip().split(' ')
k = int(line[0])
t  = int(line[1])

dnas = f.read().splitlines()


randomMotifs(dnas, k, t)
        



        
        
        
