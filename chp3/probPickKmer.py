import random
chars = ['A','G','T','C']

strings = []
for i in range(10):
    string = ''
    for j in range(600):
        string += chars[random.randint(0,3)]
    strings.append(string)

motif = 'A'*15

total = 0
for i in range(1000000):
    found = []
    for j in range(10):
        start = random.randint(0,584)
        found.append(strings[j][start:start+15])
    for substring in found:
        if substring == motif:
            total += 1
print total / 1000.0
