class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def ruleA(num):
    total = 0
    for a in range(5):
        if num[a].rank == 'A':
            total += 5
    return total

def ruleB(num):
    total = 0
    for a in range(5):
        rank = num[a].rank
        for b in range(5):
            if num[b].rank == rank:
                total += 10
        total -= 10
    total = total / 2
    return total

def ruleC(num):
    total = 0
    for a in range(4):
        if num[a].suit == num[a + 1].suit:
            total += 1
    if total == 4:
        return True
    return False

def ruleD(num):
    total = 0
    dictlist = []
    for a in range(5):
        dictlist.append(rankdict[num[a].rank])
    dictlist.sort()
    for a in range(4):
        if dictlist[a] + 1 == dictlist[a + 1]:
            total += 1
        elif dictlist[0] == 1:
            if dictlist[4] == 13:
                total += 1
    if total == 4:
        return True
    return False

def ruleE(num):
    total1 = 0
    total2 = 0
    rank = num[0].rank
    true = 0
    rank2 = 0
    for a in range(5):
        if num[a].rank == rank:
            total1 += 1
        else:
            rank2 = num[a].rank
    if rank2 != 0:
        for a in range(5):
            if num[a].rank == rank2:
                total2 += 1
        if (total1 == 3 and total2 == 2) or (total1 == 2 and total2 == 3):
            return True
    return False
    

def ruleF(num):
    total = 0
    rank = num[0].rank
    rank3 = 0
    for a in range(5):
        if num[a].rank == rank:
            total += 1
        else:
            rank3 = num[a].rank
    if total == 4:
        return True
    else:
        if rank3 != 0:
            total = 0
            for a in range(5):
                if num[a].rank == rank3:
                    total += 1
        if total == 4:
            return 1
        elif total == 5:
            return 5
    return False

def ruleG(num):
    if ruleC(num) == True and ruleD(num) == True:
        return True
    return False

suit = input().split(',')
rank = input().split(',')
carddict = dict(zip(suit, rank))
rankdict = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}

c1 = Card(suit[0], rank[0])
c2 = Card(suit[1], rank[1])
c3 = Card(suit[2], rank[2])
c4 = Card(suit[3], rank[3])
c5 = Card(suit[4], rank[4])

num = [c1, c2, c3, c4, c5]

# print(ruleF(num))


total = ruleA(num) + ruleB(num) + 30 * ruleC(num) + 50 * ruleD(num) + 80 * ruleE(num) + 100 * ruleF(num)+ 300 * ruleG(num)
print(int(total))