def skew(sequence):
    skew = [0]
    for char in sequence:
        if char == 'C':
            skew.append(skew[-1]-1)
        elif char == 'G':
            skew.append(skew[-1]+1)
        else:
            skew.append(skew[-1])
    return skew


    
    
    
def minimum_skew(sequence):
    skewArray = skew(sequence)
    indecies = [i for i, x in enumerate(skewArray) if x == min(skewArray)]
    return ' '.join(map(str, indecies))

f = open('stepic_dataset.txt', 'r')

#print minimum_skew(f.readline())
skew = [0]
while True:
    c = f.read(1)
    if not c:
        break
    if c == 'C':
        skew.append(skew[-1]-1)
    elif c == 'G':
        skew.append(skew[-1]+1)
    else:
        skew.append(skew[-1])
minimum = min(skew)
indecies = [i for i, x in enumerate(skew) if x == minimum]
print ' '.join(map(str, indecies))
    
    
