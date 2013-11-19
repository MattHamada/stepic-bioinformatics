weights = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

count = 0

def countPeptides(weights, mass):
    countRecurs(weights, mass, [])

def countRecurs(weights, mass, partial):
    global count
    s = sum(partial)
    
    #check if sum equals target
    if s == mass:
        count += 1
    
    if s >= mass:
        return

    for i in range(len(weights)):
        n = weights[i]
        remaining = weights[i+1:]
        countRecurs(remaining, mass, partial + [n])


    
