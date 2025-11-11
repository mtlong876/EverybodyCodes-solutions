p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')

class Bone:
    def __init__(self,middle):
        self.left = -1
        self.right = -1
        self.middle = middle
    def __repr__(self):
        return str(self)
    def __str__(self):
        return f"({self.left},{self.middle},{self.right})"
    
def part1(input):
    numbers = list(map(int,input.readlines()[0].split(":")[1].split(",")))
    fishbone = []
    fishbone.append(Bone(numbers[0]))
    del numbers[0]
    for number in numbers:
        newbone = True
        for bone in fishbone:
            if number < bone.middle:
                if bone.left>0:
                    continue
                else:
                    newbone = False
                    bone.left = number
                    break
            if number > bone.middle:
                if bone.right>0:
                    continue
                else:
                    newbone = False
                    bone.right = number
                    break
        if newbone:
            fishbone.append(Bone(number))
    ret = ""
    for bone in fishbone:
        ret += str(bone.middle)
    return ret

def part2(input):
    lines = input.readlines()
    numbersList = []
    for line in lines:
        numbersList.append([int(line.split(":")[0]),list(map(int,line.split(":")[1].split(",")))])
    fishbones = []
    for l in numbersList:
        numbers = l[1]
        fishbone = []
        fishbone.append(Bone(numbers[0]))
        del numbers[0]
        for number in numbers:
            newbone = True
            for bone in fishbone:
                if number < bone.middle:
                    if bone.left>0:
                        continue
                    else:
                        newbone = False
                        bone.left = number
                        break
                if number > bone.middle:
                    if bone.right>0:
                        continue
                    else:
                        newbone = False
                        bone.right = number
                        break
            if newbone:
                fishbone.append(Bone(number))
        ret = ""
        for bone in fishbone:
            ret += str(bone.middle)
        fishbones.append(int(ret))
    return max(fishbones)-min(fishbones)

def part3(input):
    lines = input.readlines()
    numbersList = []
    for line in lines:
        numbersList.append([int(line.split(":")[0]),list(map(int,line.split(":")[1].split(",")))])
    scores = []
    for l in numbersList:
        numbers = l[1]
        fishbone = []
        fishbone.append(Bone(numbers[0]))
        del numbers[0]
        for number in numbers:
            newbone = True
            for bone in fishbone:
                if number < bone.middle:
                    if bone.left>0:
                        continue
                    else:
                        newbone = False
                        bone.left = number
                        break
                if number > bone.middle:
                    if bone.right>0:
                        continue
                    else:
                        newbone = False
                        bone.right = number
                        break
            if newbone:
                fishbone.append(Bone(number))
        score = ""
        boneScores = []
        for bone in fishbone:
            boneScore = ""
            if bone.left != -1:
                boneScore += str(bone.left)
            if bone.middle != -1:
                boneScore += str(bone.middle)
            if bone.right != -1:
                boneScore += str(bone.right)
            boneScores.append(int(boneScore))        
            score += str(bone.middle)
        scores.append([l[0],int(score),boneScores])
    sortedScores = sorted(scores,key =lambda x:(x[1],x[2],x[0]),reverse = True)
    ret = 0
    for i in range(len(sortedScores)):
        ret+= (i+1) * sortedScores[i][0]
    return ret

print(part1(p1))
print(part2(p2))
print(part3(p3))