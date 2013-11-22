import math
motifs = (('T','C','G','G','G','G','G','T','T','T','T','T'),
                 ('C','C','G','G','T','G','A','C','T','T','A','C'),
                 ('A','C','G','G','G','G','A','T','T','T','T','C'),
                 ('T','T','G','G','G','G','A','C','T','T','T','T'),
                 ('A','A','G','G','G','G','A','C','T','T','C','C'),
                 ('T','T','G','G','G','G','A','C','T','T','C','C'),
                 ('T','C','G','G','G','G','A','T','T','C','A','T'),
                 ('T','C','G','G','G','G','A','T','T','C','C','T'),
                 ('T','A','G','G','G','G','A','A','C','T','A','C'),
                 ('T','C','G','G','G','T','A','T','A','A','C','C'))


countMatrix = [{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},
                          {'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},
                          {'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},
                          {'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0}]
for i in range(len(motifs[0])):
    for j in range(len(motifs)):
        countMatrix[i][motifs[j][i]] += 1 
    
profileMatrix =  [{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},
                          {'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},
                          {'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},
                          {'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0},{'A': 0, 'T': 0, 'C': 0, 'G': 0}]

for i in range(len(profileMatrix)):
    for hash in countMatrix:
        for key in hash:
            profileMatrix[i][key] = countMatrix[i][key] / 10.0

entropies = []
for hash in profileMatrix:
    entropy = 0
    for key in hash:
        if not hash[key]  == 0:
            entropy += hash[key] * math.log(hash[key],2)
    entropies.append(entropy)

print sum(entropies)
                
