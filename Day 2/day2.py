from time import time
import re

def processData(rawData):
    cubeDict = {}
    maxCubeDict = {}
    minCubeDict = {}
    for line in re.split("\n", rawData):
        rawId, gameData = re.split(": ", line)
        gameId = int(re.split(" ", rawId)[1])
        
        cubeDict[gameId] = []
        maxCubeDict[gameId] = {}
        minCubeDict[gameId] = {}
        
        gameData = re.split("; ", gameData)
        
        for gameSet in gameData:
            splitSet = re.split(" |, ", gameSet)
            tupleSet = [(splitSet[i], splitSet[i+1]) for i in range(0, len(splitSet), 2)]
            cubeDict[gameId].append(tupleSet)
            for num, color in tupleSet:
                num = int(num)
                if color not in maxCubeDict[gameId] or num >= maxCubeDict[gameId][color]:
                    maxCubeDict[gameId][color] = num
                    
                if color not in minCubeDict[gameId] or num <= minCubeDict[gameId][color]:
                    minCubeDict[gameId][color] = num
    
    return cubeDict, maxCubeDict, minCubeDict

def solvePart1(data):
        
    # given values
    trueDict = {"red": 12, "green": 13, "blue": 14}
    
    _, maxCubeDict, _ = processData(data)
    
    tot = 0
    for game in maxCubeDict.keys():
        maxVals = maxCubeDict[game]
        if all([True if maxVals[color] <= trueDict[color] else False for color in maxVals.keys()]):
            tot += game
    
    return tot

def solvePart2(data):
    _, maxCubeDict, _ = processData(data)
    tot = 0
    
    for game in maxCubeDict.keys():
        maxVals = maxCubeDict[game]
        pwr = 1
        print(list(maxVals.values()))
        for n in list(maxVals.values()):
            pwr *= n
        tot += pwr
    
    return tot

if __name__ == '__main__':
    # read test file
    with open('test.txt', 'r') as f:
        test = f.read()

    
    start = time()
    
    part1 = solvePart1(test)
    p1Time = time() - start
    
    part2 = solvePart2(test)
    p2Time = time() - p1Time - start
    
    # print solutions and show time elapsed
    print(f'Part 1 ({p1Time:.4f}s):\n{part1}\n')
    print(f'Part 2 ({p2Time:.4f}s):\n{part2}\n')