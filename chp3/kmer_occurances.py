#occurances of a kmer occuring in N sequences of length L
#assume all nucleotides have 0.25 chance of occuring
def occurances(ksize, N, L):
    return N*(L-ksize+1)*(0.25**ksize)

#if nucleotides have different probabilities
#numX: number of nucleotide X in kmer
#probX: probability of X occuring in sequence
def occurances_differentprob(ksize, N, L, numA, probA, numT, probT, numC, probC, numG, probG):
    return N*(L-ksize+1)*((probA**numA)*(probT**numT)*(probC**numC)*(probG**numG))
