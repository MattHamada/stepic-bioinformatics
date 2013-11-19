import time
def frequent_words(seq, size):
        #get all k-mers of size size
    words = {}
    seqArray = list(seq)
    #print seqArray
    for i in range(0, len(seqArray)-1):
        if (i <= len(seqArray)-size):
            word = ''.join(seqArray[i:i+size])
            #print word
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    
    #find most frequent words
    most_frequent = []
    mostTimes = 0
    #print words
    for word in words:
        #print word
        if words[word] > mostTimes:
            #print word, words[word], mostTimes
            most_frequent = []
            most_frequent.append(word)
            mostTimes = words[word]
        elif words[word] == mostTimes:
            most_frequent.append(word)
    return most_frequent

def frequent_words2(seq, size):
    words = {}
    for i in range(len(seq)-size):
        word = seq[i:i+size]
        if word in words
        
	
#start = time.time()
print frequent_words('GGTACAGAACATAATATGACAGGGGGCTTTTAAGGCTTTTAGGTACAGAACATAATATGACAGGGAGGCTTTTAAGGCTTTTAGGTACAGAAGGCTTTTAGACAGGGGACAGGGGGCTTTTAACATAATATACATAATATGACAGGGGGTACAGAAGGCTTTTAAGGCTTTTAGGTACAGAGGCTTTTAACATAATATGGCTTTTAGGTACAGAACATAATATGACAGGGGGTACAGAGACAGGGACATAATATGGTACAGAGACAGGGACATAATATGACAGGGACATAATATACATAATATGGTACAGAACATAATATGACAGGGGACAGGGGGTACAGAAGGCTTTTAACATAATATGGCTTTTAACATAATATACATAATATAGGCTTTTAAGGCTTTTAGGTACAGAGACAGGGGGTACAGAAGGCTTTTAGGTACAGAGACAGGGACATAATATGACAGGGAGGCTTTTAACATAATATGACAGGGGGTACAGAGGCTTTTAACATAATATAGGCTTTTAGGCTTTTAACATAATATAGGCTTTTAACATAATATACATAATATACATAATATAGGCTTTTAAGGCTTTTAAGGCTTTTAGGCTTTTAGACAGGGGACAGGGGGTACAGAAGGCTTTTAGGTACAGAACATAATATGACAGGGGGCTTTTAACATAATATAGGCTTTTAAGGCTTTTAGGTACAGAACATAATATAGGCTTTTAAGGCTTTTAGGCTTTTAAGGCTTTTAAGGCTTTTAACATAATATGGCTTTTAGACAGGGGGCTTTTAAGGCTTTTAGACAGGGGGTACAGAGGCTTTTAACATAATATGGCTTTTAACATAATAT', 11)
#end = time.time()
#print end-start



