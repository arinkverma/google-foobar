
import collections

def answer(s):
    lens = len(s)
    if lens == 1:
        return 1
    letters = collections.defaultdict(int)
    for letter in s:
        letters[letter] += 1

    letters = sorted(letters.items(), key=lambda i: i[1])
    MAX = letters[0][1]
    L   = letters[0][0]

    for i in xrange(MAX,1,-1):
        kl = lens/i
        k   = s[:kl]
        f = len(s.replace(k, ''))
        if f == 0:
            return i
    return 1
