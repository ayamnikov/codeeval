

test_cases = [
    '6D 7H AH 7S QC 6H 2D TD JD AS',
    'JH 5D 7H TC JS JD JC TS 5S 7S',
    '2H 8C AD TH 6H QD KD 9H 6S 6C',
    'JS JH 4H 2C 9H QH KC 9D 4D 3S',
    'TC 7H KH 4H JC 7D 9S 3H QS 7S'
]

ranklist = '23456789TJQKA'

def eval_hand(hand):
    ranks, suits = zip(*hand.split())
    a, b, c, d, e = ranks = tuple(reversed(sorted(map(ranklist.index, ranks))))
    flush = len(set(suits)) == 1
    straight = len(set(ranks)) == 5 and a-e == 4
    if flush and straight: return 10, ranks
    if flush: return 9, ranks
    if straight: return 8, ranks
    if len(set(ranks)) == 2:
        if a!=b or d!=e: return 7, ranks
        else: return 6, ranks
    if len(set(ranks)) == 3:
        if a==c or b==d or c==e: return 5, ranks
        else: return 4, ranks
    if len(set(ranks)) == 4: return 3, ranks
    return 2, ranks


for test in test_cases:
    a = eval_hand(test[:len(test)//2].strip())
    b = eval_hand(test[len(test)//2:].strip())
    print ['left', 'none', 'right'][1+(a<b)-(a>b)]
