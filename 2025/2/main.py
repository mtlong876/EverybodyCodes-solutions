p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')
def complexAdd(a,b):
    return [(a[0]+b[0]),(a[1]+b[1])]

def complexMult(a,b):
    return [((a[0]*b[0])-(a[1]*b[1])),((a[0]*b[1])+(b[0]*a[1]))]

def complexDiv(a,b):
    num1 = int(a[0] / b[0])
    num2 = int(a[1] / b[1])
    
    return [num1, num2]

def part1(input):
    lines = input.readlines()
    numbers = list(map(int,lines[0].split("=")[1].replace("[","").replace("]","").split(",")))
    start = [0,0]
    def cycle(result, A):
        R = complexMult(result,result)
        R = complexDiv(R,[10,10])
        R = complexAdd(R,A)
        return R
    return cycle(cycle(cycle(start,numbers),numbers),numbers)

def part2(input):
    lines = input.readlines()
    start = list(map(int,lines[0].split("=")[1].replace("[","").replace("]","").split(",")))
    end = complexAdd(start,[1000,1000])
    def cycle(result,A):
        R = complexMult(result,result)
        R = complexDiv(R,[100000,100000])
        R = complexAdd(R,A)
        return R
    pointer = list(start)
    total = 0
    while pointer[1]<end[1]+1:
        valid = True
        temp = [0,0]
        for _ in range(100):
            temp = cycle(temp,pointer)
            if temp[0] < -1000000 or temp[0] >1000000 or temp[1] < -1000000 or temp[1] >1000000:
                valid = False
                break
        if valid:
            total+= 1
        pointer[0] += 10
        if pointer[0]> end[0]:
            pointer[0] = start[0]
            pointer[1] +=10
    return total


def part3(input):
    lines = input.readlines()
    start = list(map(int,lines[0].split("=")[1].replace("[","").replace("]","").split(",")))
    end = complexAdd(start,[1000,1000])
    def cycle(result,A):
        R = complexMult(result,result)
        R = complexDiv(R,[100000,100000])
        R = complexAdd(R,A)
        return R
    pointer = list(start)
    total = 0
    while pointer[1]<end[1]+1:
        valid = True
        temp = [0,0]
        for _ in range(100):
            temp = cycle(temp,pointer)
            if temp[0] < -1000000 or temp[0] >1000000 or temp[1] < -1000000 or temp[1] >1000000:
                valid = False
                break
        if valid:
            total+= 1
        pointer[0] += 1
        if pointer[0]> end[0]:
            pointer[0] = start[0]
            pointer[1] +=1
    return total

print(part1(p1))
print(part2(p2))
print(part3(p3))
    