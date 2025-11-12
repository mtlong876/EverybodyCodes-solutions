p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')

def part1(input):
    lines = input.readlines()
    names = lines[0].strip().split(",")
    rules = {}
    for rule in lines[2:]:
        splits = rule.split(">")
        prefix = splits[0].strip()
        suffix = splits[1].strip().split(",")
        rules[prefix] = suffix
    for name in names:
        valid = True
        for i in range(len(name)-1):
            if name[i+1] not in rules[name[i]]:
                valid = False
        if valid:
            return name
    return False

def part2(input):
    lines = input.readlines()
    names = lines[0].strip().split(",")
    rules = {}
    total = 0
    for rule in lines[2:]:
        splits = rule.split(">")
        prefix = splits[0].strip()
        suffix = splits[1].strip().split(",")
        rules[prefix] = suffix
    for name in names:
        valid = True
        for i in range(len(name)-1):
            if name[i+1] not in rules[name[i]]:
                valid = False
        if valid:
            total += names.index(name)+1
    return total

def part3(input):
    lines = input.readlines()
    names = lines[0].strip().split(",")
    rules = {}
    for rule in lines[2:]:
        splits = rule.split(">")
        prefix = splits[0].strip()
        suffix = splits[1].strip().split(",")
        rules[prefix] = suffix
        
    validNames = []
    for name in names:
        valid = True
        for i in range(len(name)-1):
            if name[i] not in rules or name[i+1] not in rules[name[i]]:
                valid = False
        if valid:
            validNames.append(name)
    
    seen = set()
    def visit(rules, current):
        if 7 <= len(current) <= 11:
            seen.add(current)
        if len(current) > 11:
            return
        if current[-1] not in rules: 
            return
        for rule in rules[current[-1]]:
            visit(rules, current+rule)

    for name in validNames:
        visit(rules, name)
    return len(seen)

print(part1(p1))
print(part2(p2))
print(part3(p3))