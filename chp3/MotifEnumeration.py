#dnas: array of dna strings
#k: length of motif
#d: number of mutations allowed
import itertools
def MotifEnumeration(dnas, k, d):
    motifs = []
    for dna in dnas:
        dna_length = len(dna)
        for i in range(dna_length-k):
            baseMotif = dna[i:i+k]
            candidateMotifs = set(mutations(baseMotif, d))
            for candidate in candidateMotifs:
                candidate_candidates = mutations(candidate, d)
                sequences = dnas[:]
                for candidateMut in candidate_candidates:
                    for seq in dnas:
                        if candidateMut in seq and seq in sequences:
                            sequences.remove(seq)
                if len(sequences) == 0:
                    motifs.append(candidate)
    motifs = set(motifs)
    return ' '.join(motifs)
               
            

def mutations(motif, d, charset='ATCG'):
    all = []
    for indices in itertools.combinations(range(len(motif)), d):
        for replacements in itertools.product(charset, repeat=d):
            mutation = list(motif)
            for index, replacement in zip(indices, replacements):
                mutation[index] = replacement
            all.append("".join(mutation))
    return all

f = open('motifEnumInput.txt',  'r')
nums = f.readline()
nums = list(nums.strip().replace(' ', ''))
k = int(nums[0])
d = int(nums[1])
dnas = f.read().splitlines()
f.close()

print MotifEnumeration(dnas, k, d) 

