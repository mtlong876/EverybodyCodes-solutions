p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')
def part1(input):
    lines = input.readlines()
    names = lines[0].strip().split(',')
    instructions = lines[2].strip().split(',')
    pointer = 0
    max = len(names)-1
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1])
        if direction == "R":
            pointer += amount
            if pointer>max:
                pointer = max
        else:
            pointer -= amount
            if pointer<0:
                pointer = 0
    return names[pointer]

def part2(input):
    lines = input.readlines()
    names = lines[0].strip().split(',')
    instructions = lines[2].strip().split(',')
    pointer = 0
    max = len(names)-1
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1:])
        if direction == "R":
            pointer += amount
            if pointer>max:
                pointer = (pointer % max)-1
        else:
            pointer -= amount
            if pointer<0:
                pointer = pointer % max+1
    return names[pointer]

def part3(input):
    lines = input.readlines()
    names = lines[0].strip().split(',')
    instructions = lines[2].strip().split(',')
    max = len(names)-1
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1:]) % (max+1)
        temp = ""
        if direction == "R":
            temp = names[amount]
            names[amount] = names[0]
            names[0] = temp
        else:
            temp = names[-amount]
            names[-amount] = names[0]
            names[0] = temp
    return names[0]

print(part1(p1))
print(part2(p2))
print(part3(p3))