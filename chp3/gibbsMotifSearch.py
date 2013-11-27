import random
from greedyMotifSearch import makePseudoProfile, profileMostProb, medianPattern, hammingDistance

def gibbsrandom(motifs):
    scores = []
    for motif in motifs:
        score = hammingDistance(motifs, motif)
        scores.append(score)
    total = sum(scores)
    probs = []
    for score in scores:
        probs.append(score/float(total))
    sumprobs = sum(probs)
    normalizedProbs = []
    for prob in probs:
        normalizedProbs.append(prob/sumprobs)
    r = random.random()
    distprobs = []
    for i in range(1,len(normalizedProbs)):
        distprobs.append(sum(probs[0:i]))
    #print distprobs
    for prob in distprobs:
        if r < prob:
            return distprobs.index(prob)
        else:
            return len(probs)-1

def gibsMotifSearch(dnas, k, t, n):
    startMotifs = []
    for dna in dnas:
        i = random.randint(0,len(dna)-k)
        startMotifs.append(dna[i:i+k])
    bestMotifs = startMotifs
    bestProfile = makePseudoProfile(bestMotifs)
    bestConsensus = medianPattern(bestMotifs)
    bestScore = hammingDistance(bestMotifs, bestConsensus)
    motifs = bestMotifs
    for i in range(n):
        exclude = random.randint(0,len(bestMotifs)-1)
        if not exclude == len(bestMotifs):
            motifs = motifs[0:exclude] + motifs[exclude+1:]
        else:
            motifs = motifs[0:exclude]
        profile = makePseudoProfile(motifs)
        consensus = medianPattern(motifs)
        newMotif = profileMostProb(consensus, k, profile)
        #print profile, consensus, newMotif
        motifs.insert(exclude, newMotif)
        score = hammingDistance(motifs, consensus)
        if score < bestScore:
            bestMotifs = motifs
            bestConsensus = consensus
            bestScore = score
        print bestScore
            
    for motif in bestMotifs:
        print motif
    return

def gibbsSearch2(dnas, k, t,n):
    startMotifs = []
    for dna in dnas:
        i = random.randint(0,len(dna)-k)
        startMotifs.append(dna[i:i+k])
    bestMotifs = startMotifs
    bestProfile = makePseudoProfile(bestMotifs)
    bestConsensus = medianPattern(bestMotifs)
    bestScore = hammingDistance(bestMotifs, bestConsensus)
    motifs = bestMotifs
 
    for j in range(n):
        i = gibbsrandom(motifs)
        tempMotifs = []
        for a in range(t):
            if not i == a:
                tempMotifs.append(motifs[a])
        profile = makePseudoProfile(tempMotifs)
        newmotif = profileMostProb(dnas[i], k, profile)
        tempMotifs.insert(i, newmotif)
        score = hammingDistance(tempMotifs, medianPattern(tempMotifs))
        #motifs = tempMotifs
        if score < bestScore:
           bestMotifs = tempMotifs
           bestScore = score
    for motif in bestMotifs:
        print motif
        
dnas = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
    'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
     'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
     'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
     'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

#gibsMotifSearch(dnas, 8, 5, 100)
gibbsSearch2(dnas, 8, 5, 100)
