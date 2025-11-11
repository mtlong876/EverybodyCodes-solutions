p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')

def part1(input):
    letters = list(input.readlines()[0])
    swords = []
    archery = []
    magic = []
    for letter in letters:
        match letter.lower():
            case "a":
                swords.append(letter)
            case "b":
                archery.append(letter)
            case "c":
                magic.append(letter)
    mentors = 0
    combos = 0
    for sword in swords:
        if sword == "A":
            mentors += 1
        else:
            combos += mentors
    return combos

def part2(input):
    letters = list(input.readlines()[0])
    swords = []
    archery = []
    magic = []
    for letter in letters:
        match letter.lower():
            case "a":
                swords.append(letter)
            case "b":
                archery.append(letter)
            case "c":
                magic.append(letter)
    total = 0
    mentors = 0
    combos = 0
    for sword in swords:
        if sword == "A":
            mentors += 1
        else:
            combos += mentors
    total += combos
    mentors = 0
    combos = 0
    for archer in archery:
        if archer == "B":
            mentors += 1
        else:
            combos += mentors
    total += combos
    mentors = 0
    combos = 0
    for mage in magic:
        if mage == "C":
            mentors += 1
        else:
            combos += mentors
    total += combos
    return total

def part3(input):
    line = input.readlines()[0]
    letters = list(line+line)
    mentors = {
        "s":[],
        "a":[],
        "m":[]
    }
    apprentices = {
        "s":[],
        "a":[],
        "m":[]
    }
    for i in range(len(letters)):
        match letters[i]:
            case "a":
                apprentices["s"].append(i)
            case "b":
                apprentices["a"].append(i)
            case "c":
                apprentices["m"].append(i)
            case "A":
                mentors["s"].append(i)
            case "B":
                mentors["a"].append(i)
            case "C":
                mentors["m"].append(i)
    total1 = 0
    total2 = 0
    for group in apprentices:
        for apprentice in apprentices[group]:
            for master in mentors[group]:
                if master<apprentice-1000:
                    continue
                if master>apprentice+1000:
                    break
                if apprentice< len(letters)/2 and master< len(letters)/2:
                    total1+=1
                else:
                    total2+=1
    return total1 + (total2*999)

print(part1(p1))
print(part2(p2))
print(part3(p3))