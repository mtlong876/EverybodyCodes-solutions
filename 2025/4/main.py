p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')

import math 

def part1(input):
    numbers = list(map(int,input.readlines()))
    return int((numbers[0]/numbers[-1])* 2025)

def part2(input):
    numbers = list(map(int,input.readlines()))
    return math.ceil(10000000000000*(numbers[-1]/numbers[0]))

def part3(input):
    lines = input.readlines()
    numbers = []
    numbers.append([int(lines[0]),int(lines[0])])
    del lines[0]
    for i in range(len(lines)-1):
        splitNums = lines[i].split("|")
        numbers.append([int(splitNums[0]),int(splitNums[1])])
    numbers.append([int(lines[-1]),int(lines[-1])])
    ratios = []
    for i in range(len(numbers)-1):
        ratios.append(numbers[i][1]/numbers[i+1][0])
    sum = 1
    for ratio in ratios:
        sum = sum * ratio
    return int(sum* 100)

print(part1(p1))
print(part2(p2))
print(part3(p3))