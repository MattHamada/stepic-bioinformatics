#from cyclospectrum import *
aa = [[57],[71],[87],[97],[99],[101],[103],[113],[114],[115],[128],[129],[131],[137],[147],[156],[163],[186]]


def expand(peptides):
    aa = [[57],[71],[87],[97],[99],[101],[103],[113],[114],[115],[128],[129],[131],[137],[147],[156],[163],[186]]
    returnPeptides = []
    for peptide in peptides:
        for residue in aa:
            temp = peptide[:]
            temp.append(residue[0])
            returnPeptides.append(temp)
    return returnPeptides

def theospec_rec(peptide, length, peptides):
    if length == 1:
        for base in peptide:
            peptides.append(base)
        return peptides
    elif length == len(peptide):
        peptides.append(peptide)
        return theospec_rec(peptide, len(peptide)-1, peptides)
    else:
        count = 0
        while count != len(peptide):
            if count+length <= len(peptide): 
                peptides.append(peptide[count:count+length])
                count += 1
            else:
                temp = peptide[count:] + peptide[0:length-len(peptide[count:])]
                peptides.append(temp)
                count+= 1
        return theospec_rec(peptide, length - 1, peptides)


def submasses_linear(peptide):
    returnl = []
    for i in range(len(peptide)):
        for j in range(len(peptide)+1):
            if i < j:
                returnl.append(sum(peptide[i:j]))
    return returnl




def submasses_circular(peptide):
    theospec = theospec_rec(peptide, len(peptide), [])
    returnList = [0]
    for item in theospec:
        if type(item) == int:
            returnList.append(item)
        else:
            returnList.append(sum(item))
        
    return returnList




def compareSpectra(theoretical, experimental):
    count = 0
    goal = len(theoretical)
    for mass in theoretical:
        if experimental.count(mass) >= theoretical.count(mass):
            count += 1
    if count == goal:
        return True
    return False



def leaderExpand(leaderboard):
    aa =  [(57,),(71,),(87,),(97,),(99,),(101,),(103,),(113,),(114,),(115,),(128,),(129,),(131,),(137,),(147,),(156,),(163,),(186,)]
    returnboard = {}
    for peptide in leaderboard.keys():
        for residue in aa:
            #print 'peptide:', type(peptide), 'residue:', type(residue)
            if returnboard.keys().count(peptide+residue) == 0:
                returnboard[peptide+residue] = 0
    return returnboard

def leaderscore_circular(peptide, spectrum):
    theospec = submasses_circular(peptide)
    

    hits = 0
    unique_weights = list(set(spectrum))
    for weight in unique_weights:
        #if weight in spectrum:
        if spectrum.count(weight) >= theospec.count(weight):
            hits += theospec.count(weight)
        elif spectrum.count(weight) < theospec.count(weight):
            hits += spectrum.count(weight)   
    return hits

def leaderscore_linear(peptide, spectrum):
    theospec = submasses_linear(peptide)
    

    hits = 0
    unique_weights = list(set(spectrum))
    for weight in unique_weights:
        #if weight in spectrum:
        if spectrum.count(weight) >= theospec.count(weight):
            hits += theospec.count(weight)
        elif spectrum.count(weight) < theospec.count(weight):
            hits += spectrum.count(weight)   
    return hits

#print leaderscore((0,113,114,128,128,227,242,242,257,355,356,370,371,484),(0,99,113,114,128,227,257,299,355,356,370,371,484))  
#print leaderscore((129, 71, 147, 113),(0,71,113,129,147,200,218,260,313,331,347,389,460))

def cut(leaderboard, N):
    #print leaderboard
    full_scores = leaderboard.values()
    scores = list(set(full_scores))
    full_scores.sort()
    #print 's',full_scores
    topNscores = scores[len(scores)-N:len(scores)+1]
    topNscores.sort()
    topNscores = topNscores[::-1]
    #print 'top', topNscores
    #print topNscores
    returnboard = {}
    keepscores = []
    counter  = 0
    for score in topNscores:
        counter += full_scores.count(score)
        #print counter
        keepscores.append(score)
        if counter >= 10:
            break
    #print keepscores
    for peptide in leaderboard.keys():
        if leaderboard[peptide] in keepscores:
            returnboard[peptide] = leaderboard[peptide]

    
    #print returnboard
    return returnboard
    
        
    
    
    

def leaderboardCyclosequencing(spectrum, N):
    #print spectrum
    peptides =  [(57,),(71,),(87,),(97,),(99,),(101,),(103,),(113,),(114,),(115,),(128,),(129,),(131,),(137,),(147,),(156,),(163,),(186,)]
    leaderboard = {}
    bestPeptide = (0,)
    realMass = max(spectrum)
    for peptide in peptides:
        leaderboard[peptide] = 0
    tempboard = {}
    while len(leaderboard) != 0:
        leaderboard = leaderExpand(leaderboard)
        #get scores
        tempboard = leaderboard.copy()
        for peptide in leaderboard.keys():
            #print peptide

            #FIX FILTERING
            #if not compareSpectra(submasses(peptide), spectrum):
            peptideMass = max(submasses_linear(peptide))
            score_linear = leaderscore_linear(peptide, spectrum)
            tempboard[peptide] = score_linear
            if peptideMass == max(spectrum):
                
                if leaderscore_circular(peptide, spectrum) > leaderscore_circular(bestPeptide, spectrum):
                    bestPeptide = peptide
            elif peptideMass > max(spectrum):
                del tempboard[peptide]
                
                
##            if peptideMass in spectrum:
##                score = leaderscore(peptide,spectrum)
##                tempboard[peptide] = score
##                if score > leaderscore(bestPeptide,spectrum):
##                    bestPeptide = peptide
##            elif peptideMass > realMass:
##                del tempboard[peptide]
                    
##            if  max(submasses(peptide)) >  max(spectrum):
##                #print 'deleted'
##                del tempboard[peptide]
##            else:
##                score = leaderscore(peptide,spectrum)
##                #print score
##                tempboard[peptide] = score
##                if score > leaderscore(bestPeptide, spectrum):
##                    bestPeptide = peptide
        #print max(tempboard.values())
        leaderboard = cut(tempboard, N)
        #print len(leaderboard)
        #print ''
        #print tempboard
##
##        if (128,99,163,128,114,147,186,97,147,113) in leaderboard.keys():
##            score = leaderboard[(128,99,163,128,114,147,186,97,147,113)]
##            print '\n\n'
##            print score
##            
##            for peptide in leaderboard:
##                if leaderboard[peptide] == score:
##                    print '-'.join(map(str, peptide))
            #print leaderboard
        #print max(set(leaderboard.values()))
    #print bestPeptide
    #print leaderscore_circular(bestPeptide, spectrum)
    return '-'.join(map(str,bestPeptide))


#sample = [71,113,129,147,200,218,260,313,331,347,389,460]
#print leaderboardCyclosequencing(sample, 10)
        
                
       
        
    
    

def cyclosequencing(spectrum):
    peptides =  [[57],[71],[87],[97],[99],[101],[103],[113],[114],[115],[128],[129],[131],[137],[147],[156],[163],[186]]
    #print 'spectrum', spectrum
    length = len(peptides)
    while length != 0:
        peptides = expand(peptides)
        keepPeptides = peptides[:]
        #up to here matches
        for peptide in peptides:
            #print peptide
            peptideTheospec = submasses(peptide)
            totalCount = len(peptideTheospec)
            if compareSpectra(peptideTheospec, spectrum):
                print '-'.join(map(str, peptide))
            else:
                keepPeptides.remove(peptide)
        peptides = keepPeptides[:]
        length = len(peptides)
    
 
            
       
a = [97,97,99,101,103,196,198,198,200,202,295,297,299,299,301,394,396,398,400,400,497]

#cyclosequencing(a)
#cyclosequencing([0,113,128,186,241,299,314,427])

#f = open('spectrum.txt', 'r')

#print expand([[0],[113],[128],[186],[241],[299],[314],[427]],[[113],[128],[186]])




#N = int(f.readline())
#lines =  '0 97 99 114 128 147 147 163 186 227 241 242 244 260 261 262 283 291 333 340 357 385 389 390 390 405 430 430 447 485 487 503 504 518 543 544 552 575 577 584 632 650 651 671 672 690 691 738 745 747 770 778 779 804 818 819 820 835 837 875 892 917 932 932 933 934 965 982 989 1030 1039 1060 1061 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1225 1322'.strip('\n').split(' ')
lines =  '0 71 87 99 101 113 114 115 128 129 129 129 137 137 137 137 163 163 163 186 186 200 200 202 215 229 236 236 250 252 265 266 266 276 292 292 299 300 300 300 329 337 339 343 363 363 364 365 365 366 372 373 401 415 429 429 429 429 436 462 465 466 478 480 485 486 492 500 501 502 502 502 529 544 549 558 565 566 573 579 587 592 599 602 615 629 629 629 630 631 648 664 665 666 681 700 701 702 715 716 721 728 729 731 735 758 762 765 766 768 778 792 794 801 802 828 830 844 845 849 850 852 858 863 865 865 895 902 907 916 921 929 931 931 931 950 951 964 964 965 973 987 991 993 994 1002 1031 1044 1044 1045 1058 1058 1060 1064 1065 1078 1088 1093 1094 1094 1101 1102 1128 1130 1131 1131 1150 1157 1173 1193 1195 1201 1202 1207 1208 1215 1217 1223 1227 1230 1231 1231 1259 1260 1264 1279 1288 1294 1294 1294 1310 1314 1330 1330 1330 1336 1345 1360 1364 1365 1393 1393 1394 1397 1401 1407 1409 1416 1417 1422 1423 1429 1431 1451 1467 1474 1493 1493 1494 1496 1522 1523 1530 1530 1531 1536 1546 1559 1560 1564 1566 1566 1579 1580 1580 1593 1622 1630 1631 1633 1637 1651 1659 1660 1660 1673 1674 1693 1693 1693 1695 1703 1708 1717 1722 1729 1759 1759 1761 1766 1772 1774 1775 1779 1780 1794 1796 1822 1823 1830 1832 1846 1856 1858 1859 1862 1866 1889 1893 1895 1896 1903 1908 1909 1922 1923 1924 1943 1958 1959 1960 1976 1993 1994 1995 1995 1995 2009 2022 2025 2032 2037 2045 2051 2058 2059 2066 2075 2080 2095 2122 2122 2122 2123 2124 2132 2138 2139 2144 2146 2158 2159 2162 2188 2195 2195 2195 2195 2209 2223 2251 2252 2258 2259 2259 2260 2261 2261 2281 2285 2287 2295 2324 2324 2324 2325 2332 2332 2348 2358 2358 2359 2372 2374 2388 2388 2409 2422 2424 2424 2438 2438 2461 2461 2461 2487 2487 2487 2487 2495 2495 2495 2496 2509 2510 2511 2523 2525 2537 2553 2624'.strip('\n').split(' ')
#lines =  '0 71 113 129 147 200 218 260 313 331 347 389 460'.strip('\n').split(' ')
ints = []
for item in lines:
    ints.append(int(item))

print leaderboardCyclosequencing(ints, 29)

##out = open('output.txt', 'w')
##out.write(cyclosequencing(ints))
#f.close()
##out.close()
