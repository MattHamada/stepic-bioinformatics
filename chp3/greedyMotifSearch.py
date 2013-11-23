from medianPattern import medianPattern
from profileMostProbable import profileMostProb
def hammingDistance(kmers, motif):
    score = 0
    for kmer in kmers:
        for i in range(len(kmer)):
            if not kmer[i] == motif[i]:
                score += 1
    return score

def makeProfile(kmers):
    counts = []
    for i in range(len(kmers[0])):
        counts.append({'A': 0, 'T': 0, 'G': 0, 'C': 0})
    for kmer in kmers:
        for i in range(len(kmer)):
            counts[i][kmer[i]] += 1
            #ATGC order
    profile = [[],[],[],[]]
    print counts
    for hash in counts:
        for key in hash:
            profile[0].append(hash['A'] / float(len(kmers)))
            profile[1].append(hash['T'] / float(len(kmers)))
            profile[2].append(hash['G'] / float(len(kmers)))
            profile[3].append(hash['C'] / float(len(kmers)))
    print profile
    return profile
        
        


def greedyMotif(dnas, k, t):
    baselineKmers = []
    for dna in dnas:
        baselineKmers.append(dna[0:k])
    consensusKmer = medianPattern(baselineKmers, k)
    baselineScore = hammingDistance(baselineKmers, consensusKmer)
    #print baselineScore

    kmers = []
    dnaUsed = 1
    for i in range(len(dnas[0])-k+1):
         kmers.append(dna[0][i:i+k])
         profile = makeProfile(kmers)
         print dnas[dnaUsed], k, profile
         mostProb = profileMostProb(dnas[dnaUsed] , k, profile)
         


dnas = ['GGCGTTCAGGCA',
              'AAGAATCAGTCA',
              'CAAGGAGTTCGC',
              'CACGTCAATCAC',
              'CAATAATATTCG',]

#a = makeProfile(dnas)
#print a
greedyMotif(dnas, 3, 5)

