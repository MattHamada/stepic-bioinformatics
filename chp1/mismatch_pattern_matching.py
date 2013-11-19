import itertools
def mismatch_pattern(pattern, sequence, limit):
    indecies = []
    patternSize = len(pattern)
    for i in range(len(sequence)-patternSize):
        count = 0
        substring = sequence[i:i+patternSize]
        for j in range(patternSize):
            if pattern[j] == substring[j]:
                count += 1
        if abs(count-patternSize) <= limit:
            indecies.append(i)
    return ' '.join(map(str,indecies))

def mismatch_pattern_kmer(pattern, sequence, limit):
    indecies = []
    patternSize = len(pattern)
    for i in range(len(sequence)-patternSize):
        count = 0
        substring = sequence[i:i+patternSize]
        for j in range(patternSize):
            if pattern[j] == substring[j]:
                count += 1
        if abs(count-patternSize) <= limit:
            indecies.append(i)
    return len(indecies)

#f = open('stepic_dataset.txt', 'r')

def reverseComplement(sequence):
    rcomp = []
    
    for base in sequence:
        if base == 'A':
            rcomp.append('T')
        elif base == 'C':
            rcomp.append('G')
            
        elif base == 'T':
            rcomp.append('A')
        elif base == 'G':
            rcomp.append('C')
    return ''.join(rcomp)
    

def frequentKmerMismatch(sequence, size, limit):
    output = {}
    biggest = 0
    combos = itertools.product(['A','T','G','C'], repeat=size)
    for combo in combos:
        matches = mismatch_pattern_kmer(combo, sequence, limit)
        if matches == biggest:
            output[combo] = matches
        elif matches > biggest:
            output = {}
            output[combo] = matches
            biggest = matches
    answers = []
    for answer in output:
        temp = ''.join(answer)
        answers.append(temp)
    return ' '.join(answers)

def mismatchRevcompPatterns(sequence, size, limit):
    output = {}
    biggest = 0
    combos = itertools.product(['A','T','G','C'], repeat=size)
    for combo in combos:
        strCombo = ''.join(combo)
        if reverseComplement(strCombo) not in output:
            matches = mismatch_pattern_kmer(strCombo, sequence, limit) + mismatch_pattern_kmer(reverseComplement(strCombo), sequence, limit)
            if matches == biggest:
                output[strCombo] = matches
            elif matches > biggest:
                output = {}
                output[strCombo] = matches
                biggest = matches
    answers = []
    for answer in output:
        answers.append(answer)
    return ' '.join(answers)
f = open('problem.txt', 'r')
print mismatchRevcompPatterns(f.readline(), 9, 2)
    
    
 
        
