
def deBruijn(text, k):
    k = k-1
    kmers = []
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    graph(kmers)
    return

def deBruijnFromKmers(kmers):
    length = len(kmers[0])
    sufprefixes = []
    for kmer in kmers:
        sufprefixes.append(kmer[0:length-1])
        sufprefixes.append(kmer[1:])
    graph(sufprefixes)
    return
        

def graph(kmers):
    kmers.sort()
    kmers = set(kmers)
    overlaps = {}
    for kmer in kmers:
        overlaps[kmer] = []
        suffix = kmer[1:len(kmer)]
        for kmerCandidate in kmers:
            if suffix == kmerCandidate[0:len(kmer)-1]:
                overlaps[kmer].append(kmerCandidate)

    fout = open('deBrujinGraphout.txt', 'w')

    foundmers = []
    for kmer in overlaps.keys():
        foundmers.append(kmer)
    foundmers.sort()
    for kmer in foundmers:
        if not len(overlaps[kmer]) == 0:
            values = ','.join(overlaps[kmer])
            fout.write(kmer + " -> " + values + '\n')
    fout.close()
    return


#deBruijn('TAATGCCATGGGATGTT', 4)

deBruijnFromKmers(['GAGG','GGGG','GGGA','CAGG','AGGG','GAGG'])

fin = open('deBrujinKmersIn.txt', 'r')
a = fin.read().splitlines()
fin.close()
deBruijnFromKmers(a)


