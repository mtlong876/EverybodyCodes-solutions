p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')

def part1(input):
    lines = input.readlines()
    numbers = list(map(int,lines[0].strip().split(",")))
    total = 0
    for i in range(len(numbers)-1):
        if abs(numbers[i]-numbers[i+1]) == 16:
            total+=1
    return total


def part2(input):
    lines = input.readlines()
    numbers = list(map(int,lines[0].strip().split(",")))
    total = 0
    strings = []
    for i in range(len(numbers)-1):
        for x,y in strings:
            if numbers[i] == x or numbers[i+1] == x or numbers[i] == y or numbers[i+1] == y:
                continue
            if (x<numbers[i]<y) != (x<numbers[i+1]<y):
                total+=1
        strings.append(sorted([numbers[i],numbers[i+1]]))
    return total

def part3(input):
    lines = input.readlines()
    numbers = list(map(int,lines[0].strip().split(",")))
    cuts = {}
    for i in range(len(numbers)-1):
        a,b = sorted([numbers[i],numbers[i+1]])
        for left in range(a+1,b):
            for right in [*range(b+1,256+1),*range(1,a)]:
                l,r = sorted([left,right])
                cuts[(l,r)] = cuts.get((l,r),0) + 1

    return (max(cuts.values()))

print(part1(p1))
print(part2(p2))
print(part3(p3))