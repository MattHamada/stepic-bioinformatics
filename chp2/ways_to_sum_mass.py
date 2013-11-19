
peptides = (57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186)

def numberOfWays(target):
    ways = [1]
    for i in range(len(peptides)):
        start = peptides[i]
        while start<= target:
            ways.append(ways[start-peptides[i]])
            start+= 1
    return sum(ways)
        
target = 1024
ways = 0
a = target
while a >= 0:
    b = a
    a -= target
    while b >= 0:
        c = b
        b -= 186
        while c >= 0:
            d = c
            c -= 163
            while d >= 0:
                e = d
                d -= 156
                while e >= 0:
                    f = e
                    e -= 147
                    while f >= 0:
                        g = f
                        f -= 137
                        while g >= 0:
                            h = g
                            g -= 131
                            while h >= 0:
                                i = h
                                h -= 129
                                while  i >= 0:
                                    j = i
                                    i -= 128
                                    while j >= 0:
                                        k =j
                                        j -= 115
                                        while k >= 0:
                                            l = k
                                            k -= 114
                                            while l >= 0:
                                                m = l
                                                l -= 113
                                                while m >= 0:
                                                    n = m
                                                    m -= 103
                                                    while n >= 0:
                                                        o =n
                                                        n -= 101
                                                        while o >= 0:
                                                            p = o
                                                            o -= 99
                                                            while p >= 0:
                                                                q = p
                                                                p -= 97
                                                                while q >= 0:
                                                                    r = q
                                                                    q -= 87
                                                                    while r >= 0:
                                                                        s = r
                                                                        r -= 71
                                                                        while s >= 0:
                                                                            t = s
                                                                            ways += 1
                                                                            s -= 57

print ways
peptides = (57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186)
            
        
