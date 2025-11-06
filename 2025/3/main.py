p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')

def part1(input):
    lines = input.readlines()
    numbers = list(map(int,lines[0].split(",")))
    pointer = max(numbers)
    end = min(numbers)
    total = pointer
    while pointer != end:
        nextNum = end
        for number in numbers:
            if number > nextNum and number < pointer:
                nextNum = number
        total+= nextNum
        pointer = nextNum
    return total

def part2(input):
    lines = input.readlines()
    numbers = list(map(int,lines[0].split(",")))
    pointer = 0
    end = max(numbers)
    total = pointer
    for _ in range(20):
        nextNum = end
        for number in numbers:
            if number < nextNum and number > pointer:
                nextNum = number
        total+= nextNum
        pointer = nextNum
    return total

def part3(input):
    lines = input.readlines()
    numbers = list(map(int,lines[0].split(",")))
    numberDict = {}
    for number in numbers:
        if number not in numberDict:
            numberDict[number] = 1
        else:
            numberDict[number] += 1
    return max(numberDict.values())
print(part1(p1))
print(part2(p2))
print(part3(p3))