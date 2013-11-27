import random
from greedyMotifSearch import makePseudoProfile, hammingDistance, profileMostProb
from medianPattern import medianPattern


def getMotifs(profile, dnas, k):
    motifs = []
    for dna in dnas:
        motifs.append(profileMostProb(dna, k, profile))
    return motifs
            

def randomMotifs(dnas, k, t):
    finalBestMotifs = []
    for i in range(1000):
        bestMotifs = []
        for dna in dnas:        
            length = len(dna)
            startBase = random.randint(0, length-k)
            bestMotifs.append(dna[startBase:startBase+k])
        bestconsensus = medianPattern(bestMotifs, k)
        bestScore = hammingDistance(bestMotifs, bestconsensus)
        while True:
            profile = makePseudoProfile(bestMotifs)
            motifs = getMotifs(profile, dnas, k)
            consensus = medianPattern(motifs, k)
            score = hammingDistance(motifs, consensus)
            if score < bestScore:
                bestMotifs = motifs
                bestconsensus = consensus
                bestScore = score
            else:
                if bestScore < hammingDistance(finalBestMotifs, medianPattern(finalBestMotifs, k)):
                    finalBestMotifs = bestMotifs
                break
    print bestMotifs

dnas = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
              'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
              'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
              'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
              'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

randomMotifs(dnas, 8, 5)
        



        
        
        
