

test_cases = [
    '6D 7H AH 7S QC 6H 2D TD JD AS',
    'JH 5D 7H TC JS JD JC TS 5S 7S',
    '2H 8C AD TH 6H QD KD 9H 6S 6C',
    'JS JH 4H 2C 9H QH KC 9D 4D 3S',
    'TC 7H KH 4H JC 7D 9S 3H QS 7S'
]

def eval_hand(hand):
    r, s=zip(*hand.split())
    a, b, c, d, e=r=tuple(reversed(sorted(map('23456789TJQKA'.index, r))))
    k, l=lambda n: tuple(x for x in r if r.count(x)==n), len(set(r))
    kk=lambda n, m: tuple(chain(k(n), k(m)))
    f=len(set(s))==1
    a5=l==5 and a==12 and b-e==3
    st=l==5 and a-e==4
    if f and st: return 11, r
    if f and a5: return 10
    if l==2 and k(4): return 9, kk(4, 1)
    if l==2: return 8, kk(3, 2)
    if f: return 7, r
    if st: return 6, r
    if a5: return 5
    if l==3 and k(3): return 4, kk(3, 1)
    if l==3: return 3, kk(2, 1)
    if l==4: return 2, kk(2, 1)
    return 1, r
    
for test in test_cases:
    a = eval_hand(test[:len(test)//2].strip())
    b = eval_hand(test[len(test)//2:].strip())
    print ['left', 'none', 'right'][1+(a<b)-(a>b)]
