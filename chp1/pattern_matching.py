import time
def match_pattern(pattern, sequence):
    indices = []
    for i in range(len(sequence)-len(pattern)):
        if pattern == sequence[i:i+len(pattern)]:
            indices.append(i)
    strindices = []
    for item in indices:
        strindices.append(str(item))
    return ' '.join(strindices)

#print match_pattern('ATAT', 'GATATATGCATATACTT')

f = open('Vibrio_cholerae.txt', 'r')
f2 = open('output.txt', 'w')
start = time.time()
f2.write(match_pattern('CTTGATCAT', f.readline()))
end = time.time()
print end-start
#print len(f.readline())
f.close()
f2.close()

        

