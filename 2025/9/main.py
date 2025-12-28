p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')

def part1(input):
    lines = input.readlines()
    parent1 = lines[0].strip().split(":")[1]
    parent2 = lines[1].strip().split(":")[1]
    child = lines[2].strip().split(":")[1]
    p1total = 0
    p2total = 0
    for i, letter in enumerate(parent1):
        if letter == child[i]:
            p1total+=1
    for i, letter in enumerate(parent2):
        if letter == child[i]:
            p2total+=1
    return p1total*p2total

def part2(input):
    lines = input.readlines()
    dna = {}
    for line in lines:
        id,letters = line.strip().split(":")
        dna[int(id)] = letters
    total = 0
    for cId , cLetters in dna.items():
        found = False
        for pId , pLetters in dna.items():
            if found: continue
            for p2Id , p2Letters in dna.items():
                if found: continue
                if pId == cId or p2Id == cId: continue
                if all(a == c or b == c for a,b,c in zip(pLetters,p2Letters,cLetters)):
                    p1total = 0
                    p2total = 0
                    for i, letter in enumerate(pLetters):
                        if letter == cLetters[i]:
                            p1total+=1
                    for i, letter in enumerate(p2Letters):
                        if letter == cLetters[i]:
                            p2total+=1
                    total += p1total*p2total
                    found = True
    return total
            
def part3(input):
    lines = input.readlines()
    dna = {}
    for line in lines:
        id,letters = line.strip().split(":")
        dna[int(id)] = letters
    tree = {}
    for cId , cLetters in dna.items():
        print("Checking child ",cId)
        found = False
        for pId , pLetters in dna.items():
            if found: continue
            for p2Id , p2Letters in dna.items():
                if found: continue
                if pId == cId or p2Id == cId: continue
                if all(a == c or b == c for a,b,c in zip(pLetters,p2Letters,cLetters)):
                    if cId in tree:
                        tree[cId].extend((pId,p2Id))
                    else:
                        tree[cId] = [pId,p2Id]
                    if pId in tree:
                        tree[pId].extend((cId,p2Id))
                    else:
                        tree[pId] = [cId,p2Id]
                    if p2Id in tree:
                        tree[p2Id].extend((cId,pId))
                    else:
                        tree[p2Id] = [cId,pId]
                    found = True
    maxSeen = set()
    print(tree)
    for child,parents in tree.items():
        seen = set()
        visit = set()
        seen.add(child)
        visit.add(child)
        while visit:
            for id in visit:
                toAdd = []
                if id in tree:
                    for id2 in tree[id]:
                        if id2 not in seen:
                            seen.add(id2)
                            toAdd.append(id2)
            visit.remove(id)
            visit.update(toAdd)
        if len(seen)>len(maxSeen):
            print("New max found with ",len(seen)," members, starting at ",child)
            maxSeen = seen
    total = 0
    for x in maxSeen:
        total += x
    return total

print(part1(p1))
print(part2(p2))
print(part3(p3))