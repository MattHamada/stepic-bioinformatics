#from medianPattern import medianPattern
def medianPattern(dnas):
    pattern = []
    for i in range(len(dnas[0])):
        temp = [0,0,0,0]
        for j in range(len(dnas)):
            #print dnas, i, j
            if dnas[j][i] == 'A':
                temp[0] += 1
            elif dnas[j][i] == 'T':
                temp[1] += 1
            elif dnas[j][i] == 'G':
                temp[2] += 1
            elif dnas[j][i] == 'C':
                temp[3] += 1
        highestnum = max(temp)
        if temp.index(highestnum) == 0:
            pattern.append('A')
        elif temp.index(highestnum) == 1:
            pattern.append('T')
        elif temp.index(highestnum) == 2:
            pattern.append('G')
        elif temp.index(highestnum) == 3:
            pattern.append('C')
        
    return ''.join(pattern)
#adjust to go of seqs not profile
        
            

def hammingDistance(kmers, motif):
    score = 0
    #print kmers, motif
    for kmer in kmers:
        for i in range(len(kmer)):
            if not kmer[i] == motif[i]:
                score += 1
    return score

def makeProfile(kmers):
      #ATGC order
    counts = [[],[],[],[]]
    for i in range(len(kmers[0])):
        A = 0.0
        T = 0.0
        G = 0.0
        C = 0.0
        for j in range(len(kmers)):
            if kmers[j][i] == 'A':
                 A += 1.0
            if kmers[j][i] == 'T':
                 T += 1.0
            if kmers[j][i] == 'G':
                 G += 1.0
            if kmers[j][i] == 'C':
                 C += 1.0
        counts[0].append(A)
        counts[1].append(T)
        counts[2].append(G)
        counts[3].append(C)
    profile = [[],[],[],[]]
    for i in range(len(counts[0])):
        sum = 0
        for j in range(len(counts)):
            sum += counts[j][i]
        profile[0].append(counts[0][i] / sum)
        profile[1].append(counts[1][i] / sum)
        profile[2].append(counts[2][i] / sum)
        profile[3].append(counts[3][i] / sum)
    
    return profile

def makePseudoProfile(kmers):
    counts = [[],[],[],[]]
    for i in range(len(kmers[0])):
        A = 1.0
        T = 1.0
        G = 1.0
        C = 1.0
        for j in range(len(kmers)):
            if kmers[j][i] == 'A':
                 A += 1.0
            if kmers[j][i] == 'T':
                 T += 1.0
            if kmers[j][i] == 'G':
                 G += 1.0
            if kmers[j][i] == 'C':
                 C += 1.0
        counts[0].append(A)
        counts[1].append(T)
        counts[2].append(G)
        counts[3].append(C)
    profile = [[],[],[],[]]
    for i in range(len(counts[0])):
        sum = 0
        for j in range(len(counts)):
            sum += counts[j][i]
        profile[0].append(counts[0][i] / sum)
        profile[1].append(counts[1][i] / sum)
        profile[2].append(counts[2][i] / sum)
        profile[3].append(counts[3][i] / sum)
    
    return profile
    
        
        
def profileMostProb(seq, k, profile):
    bestSeq = ''
    bestProb = -1
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        #print kmer
        prob = 1
        for j in range(k):
            #print profile
            if kmer[j] == 'A':
                prob *= profile[0][j]
            if kmer[j] == 'T':
                prob *= profile[1][j]
            if kmer[j] == 'G':
                prob *= profile[2][j]
            if kmer[j] == 'C':
                prob *= profile[3][j]

        if prob > bestProb:
            bestProb = prob
            bestSeq = kmer
    return bestSeq

def greedyMotif(dnas, k, t):
    baselineKmers = []
    for dna in dnas:
        baselineKmers.append(dna[0:k])
    #print baselineKmers
    consensusKmer = medianPattern(baselineKmers)
    
    baselineScore = hammingDistance(baselineKmers, consensusKmer)
    #print baselineScore

    
    bestcol = baselineKmers
    bestscore = baselineScore
    for i in range(len(dnas[0])-k+1):
        collection = []
        kmers = []
        kmers.append(dnas[0][i:i+k])
        collection.append(dnas[0][i:i+k])
        for j in range(1,len(dnas)):    
             #print kmers

            #change here from pseudo/nonpseudo
             profile = makePseudoProfile(collection)
             mostProb = profileMostProb(dnas[j] , k, profile)
             collection.append(mostProb)
        
        colconsensus = medianPattern(collection)
        colscore = hammingDistance(collection, colconsensus)
        #print collection, colscore, colconsensus
        if colscore < bestscore:
            bestscore = colscore
            bestcol = collection
    return bestcol
             
             
         


##dnas = ['GGCGTTCAGGCA',
##              'AAGAATCAGTCA',
##              'CAAGGAGTTCGC',
##              'CACGTCAATCAC',
##              'CAATAATATTCG',]

f = open('greedyinput.txt', 'r')
line = f.readline().strip().split(' ')
k = int(line[0])
t  = int(line[1])

dnas = f.read().splitlines()

a = greedyMotif(dnas,k,t)

for i in a:
    print i

f.close()

