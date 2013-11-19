import random
import itertools
def pr(N, A, pattern, t):
        count = 0
        pattern = list(pattern)
        for i in range(len(pattern)):
                pattern[i] = int(pattern[i])
        possible = itertools.product(range(A), repeat=N)
        possibilities = 0 #amount of random strings lenN generated
        for choice in possible:
                possibilities += 1
                tcount = 0
                #print choice                
                for i in range(len(choice)):
                        
                        if not i == len(choice)-A+1:
                                for j in range(len(pattern)):
                                        if not j == len(pattern)-A+1:
                                                #print "j= ", j
                                                if choice[i] == pattern[j] and choice[i+1] == pattern[j+1]:
                                                        tcount += 1
                                                        #print "found"
                
                if tcount >= t:
                        count += 1
        return count / float(possibilities)


print pr(4,2,'11',2)

#po = itertools.product(range(2), repeat=4)



        




