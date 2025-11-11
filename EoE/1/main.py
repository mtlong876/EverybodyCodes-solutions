p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')
def eni(N,EXP,Mod):
    score = 1
    remainders = []
    for _ in range(EXP):
       score = (score * N)%Mod
       remainders.append(score)
    remainders.reverse()
    return int("".join(map(str,remainders)))

def eniTwo(N,EXP,Mod):
    remainders = []
    for i in range(5):
        remainders.append(pow(N,EXP-i,Mod))
    return int("".join(map(str,remainders)))

def eniThree(N,EXP,Mod):
    score = 1
    loop = [score]
    seen = set()
    while score not in seen:
        seen.add(score)
        score = (score * N)%Mod
        loop.append(score)
    loopStart = loop.index(score)
    loopEnd = len(loop)-1
    loopSum = sum(loop[loopStart+1:])
    loopSize = loopEnd-loopStart
    dmod = divmod(EXP-loopStart,loopSize)

    return sum(loop[1:loopStart+1]) + dmod[0] * loopSum + sum(loop[loopStart+1:loopStart+1+dmod[1]])

def part1(input):
    lines = input.readlines()
    maximum = 0
    for line in lines:
        initialSplit = line.strip().split("=")
        initialSplit.pop(0)
        splitLine = []
        for split in initialSplit:
            num = split.split(" ")[0]
            splitLine.append(int(num))
        eni1 = eni(splitLine[0],splitLine[3],splitLine[6])
        eni2 = eni(splitLine[1],splitLine[4],splitLine[6])
        eni3 = eni(splitLine[2],splitLine[5],splitLine[6])
        maximum = max(maximum,(eni1+eni2+eni3))
    return(maximum)


def part2(input):
    lines = input.readlines()
    maximum = 0
    for line in lines:
        initialSplit = line.strip().split("=")
        initialSplit.pop(0)
        splitLine = []
        for split in initialSplit:
            num = split.split(" ")[0]
            splitLine.append(int(num))
        eni1 = eniTwo(splitLine[0],splitLine[3],splitLine[6])
        eni2 = eniTwo(splitLine[1],splitLine[4],splitLine[6])
        eni3 = eniTwo(splitLine[2],splitLine[5],splitLine[6])
        maximum = max(maximum,(eni1+eni2+eni3))
    return(maximum)


def part3(input):
    lines = input.readlines()
    maximum = 0
    for line in lines:
        initialSplit = line.strip().split("=")
        initialSplit.pop(0)
        splitLine = []
        for split in initialSplit:
            num = split.split(" ")[0]
            splitLine.append(int(num))
        eni1 = eniThree(splitLine[0],splitLine[3],splitLine[6])
        eni2 = eniThree(splitLine[1],splitLine[4],splitLine[6])
        eni3 = eniThree(splitLine[2],splitLine[5],splitLine[6])
        maximum = max(maximum,(eni1+eni2+eni3))
    return(maximum)
print(part1(p1))
print(part2(p2))
print(part3(p3))