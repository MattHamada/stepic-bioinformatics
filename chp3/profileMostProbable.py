##profile = [[0.2,0.4,0.3,0.1],
##                 [0.2,0.3,0.3,0.2],
##                 [0.3,0.1,0.5,0.1],
##                 [0.2,0.5,0.2,0.1],
##                 [0.3,0.1,0.4,0.2]]

def profileMostProb(seq, k, profile):
    bestSeq = ''
    bestProb = 0
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        prob = 1
        for j in range(k):
            prob *= profile[j][kmer[j]]
        if prob > bestProb:
            bestProb = prob
            bestSeq = kmer
    return bestSeq
            
            



profile = []
f = open('probPattern.txt', 'r')
seq = f.readline().strip()
k = int(f.readline())
f.readline()
lines = f.read().splitlines()
for line in lines:
    lArray = line.split()
    temp = {}
    temp['A'] = float(lArray[0])
    temp['C'] = float(lArray[1])
    temp['G'] = float(lArray[2])
    temp['T'] = float(lArray[3])
    profile.append(temp)
#print profile

a = profileMostProb(seq, k, profile)
print a
        
