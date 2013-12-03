def overlapGraph(kmers):
    kmers.sort()
    overlaps = {}
    for kmer in kmers:
        overlaps[kmer] = []
        suffix = kmer[1:len(kmer)]
        for kmerCandidate in kmers:
            if suffix == kmerCandidate[0:len(kmer)-1]:
                overlaps[kmer].append(kmerCandidate)

    fout = open('overlapGraphout.txt', 'w')
    
    for kmer in overlaps.keys():
        if not len(overlaps[kmer]) == 0:
            values = ' '.join(overlaps[kmer])
            fout.write(kmer + " -> " + values + '\n')
    fout.close()
    return

#fin  = open('overlapGraphInput.txt', 'r')

#kmers = fin.read().splitlines()
#fin.close()


#verlapGraph(kmers)
