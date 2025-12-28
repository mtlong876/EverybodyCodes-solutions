p1 = open('part1.txt','r')
p2 = open('part2.txt','r')
p3 = open('part3.txt','r')


def part1(input):
    lines = input.readlines()
    grid = []
    for line in lines:
        grid.append(line.strip())
    width = len(grid[0])
    height = len(grid)
    y = 0
    x = 0
    found = False
    for line in grid:
        x = 0
        for char in line:
            if found: break
            if char == "D":
                found = True
                break
            x+= 1
        if found: break
        y+= 1
    locations = [(x,y)]
    seen = set()
    possibleMoves = [(1,-2),(-1,-2),(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1)]
    moves = 4
    for i in range(moves+1):
        newLocations = []
        for location in locations:
            if location not in seen:
                for move in possibleMoves:
                    newX = location[0] + move[0]
                    newY = location[1] + move[1]
                    if 0 <= newX < width and 0<= newY < height:
                        newLocations.append((newX,newY))
                seen.add(location)
        locations = newLocations
    total = 0
    for location in seen:
        if grid[location[1]][location[0]] == "S":
            total += 1
    return total

def part2(input):
    lines = input.readlines()
    grid = []
    for line in lines:
        grid.append(line.strip())
    width = len(grid[0])
    height = len(grid)
    y = 0
    x = 0
    dragon = ()
    sheep = set()
    hiding = set()
    for line in grid:
        x = 0
        for char in line:
            if char == "D":
                dragon = (x,y)
            elif char == "#":
                hiding.add((x,y))
            elif char == "S":
                sheep.add((x,y))
            x+= 1
        y+= 1
    locations = set()
    locations.add(dragon)
    possibleMoves = [(1,-2),(-1,-2),(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1)]
    moves = 20
    total = 0
    for i in range(moves):
            newLocations = set()
            for location in locations:
                for move in possibleMoves:
                    newX = location[0] + move[0]
                    newY = location[1] + move[1]
                    if 0 <= newX < width and 0<= newY < height:
                        newLocations.add((newX,newY))
                        if (newX,newY) in sheep and grid[newY][newX] != "#":
                            total += 1
                            sheep.remove((newX,newY))
            locations = newLocations

            newSheep = set()
            for s in sheep:
                new = (s[0],s[1]+1)
                if not (0 <= new[0] < width and 0<= new[1] < height):
                    continue
                if (new[1],new[0]) in locations and grid[new[1]][new[0]] != "#":
                    total += 1
                    continue
                newSheep.add((s[0],s[1]+1))
            sheep = newSheep
    return total
       
print(part1(p1))
print(part2(p2))