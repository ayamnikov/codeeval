

def lev(s, t):
    if s == t: return 0
    if not s: return len(t)
    if not t: return len(s)

    v0 = [x for x in xrange(len(t)+1)]
    v1 = [0] * (len(t) + 1)

    for i in xrange(len(s)):
        v1[0] = i + 1

        for j in xrange(len(t)):
            cost = s[i] != t[j]
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)

        for j in xrange(len(v0)):
            v0[j] = v1[j]

    return v1[len(t)]

import sys
filename = 'lev_dis.txt'
file = open(filename, 'r')
test_cases = []
for line in file:
    line = line.rstrip('\n')
    if line == 'END OF INPUT':
        break
    if line:
        test_cases.append(line)

words = []
max_len = 0
for line in file:
    line = line.rstrip('\n')
    if line:
        if len(line) > max_len: max_len = len(line)
        words.append(line)

from itertools import chain
words_separated = [[] for _ in xrange(max_len+1)]
for word in words:
    words_separated[len(word)].append(word)

def get_friends(word):
    a = len(word) - 1
    b = a + 3
    a = max(0, a)
    pool = chain(*words_separated[a:b])
    res = []
    for word2 in pool:
        if lev(word, word2) == 1:
            res.append(word2)
    return res

def solve(word):
    network = set([word])
    friends = get_friends(word)
    while 1:
        next_friends = []
        for friend in friends:
            network.add(friend)
            next_friends.extend(x for x in get_friends(friend) if x not in network)
        if not next_friends:
            break
        friends = next_friends
    return network

for test in test_cases:
    print len(solve(test))

print len(solve('jelly'))
