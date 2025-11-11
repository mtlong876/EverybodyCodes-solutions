p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')
p4 = open('part3.txt','r')

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
    letters = list(line+line+line)
    distance = 1000
    mentors = {"A":[],"B":[],"C":[]}
    apprentices = {"A":[],"B":[],"C":[]}
    start,middle,final= 0,0,0
    for i in range(len(letters)):
        if letters[i].isupper():
            if apprentices[letters[i]]:
                while i - apprentices[letters[i]][0] >distance:
                    apprentices[letters[i]].pop(0)
                if i<len(letters)/3:
                    start += len(apprentices[letters[i]])
                elif i<2*(len(letters)/3):
                    middle += len(apprentices[letters[i]])
                else:
                    final += len(apprentices[letters[i]])
            mentors[letters[i]].append(i)
        else:
            if mentors[letters[i].upper()]:
                while i - mentors[letters[i].upper()][0] >distance:
                    mentors[letters[i].upper()].pop(0)
                if i<len(letters)/3:
                    start += len(mentors[letters[i].upper()])
                elif i<2*(len(letters)/3):
                    middle += len(mentors[letters[i].upper()])
                else:
                    final += len(mentors[letters[i].upper()])
            apprentices[letters[i].upper()].append(i)
    return start+(middle*998)+final

print(part1(p1))
print(part2(p2))
print(part3(p3))