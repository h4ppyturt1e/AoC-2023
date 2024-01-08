from time import time
import re

def solvePart1(data):
    data = data.split("\n")
    bodyLen = len(data[0])
    joinedData = "".join(data)
    
    symbolIndices = set()
    numIndices = []
    curNum = ""
    curNumIndices = set()
    
    for i in range(len(joinedData)):
        c = joinedData[i]
        
        if i % bodyLen == 0 and i != 0 and curNum and curNumIndices:
            numIndices.append((int(curNum), curNumIndices))
            curNum = ""
            curNumIndices = set()
        
        if c.isdigit():
            curNum += c
            curNumIndices.add(i)
        
        elif c != ".":
            symbolIndices.add(i)
            if curNum and curNumIndices:
                numIndices.append((int(curNum), curNumIndices))
                curNum = ""
                curNumIndices = set()
            
        elif curNum and curNumIndices: 
            numIndices.append((int(curNum), curNumIndices))
            curNum = ""
            curNumIndices = set()
    
    # print(symbolIndices)
    
    # for i in symbolIndices:
    #     print(i, joinedData[i])
    # print(numIndices)
    
    withAround = []
    
    for num, indices in numIndices:
        # print()
        # print(num)
        left, right = min(indices), max(indices)
        # get ranges
        
        # check if on left edge (eg. 456.....)
        midLeft = left-1 if (left-1) % bodyLen != bodyLen-1 else left
        midRight = right+1 if (right+1) % bodyLen != 0 else right
        
        # get ranges
        topRange = set(range(midLeft-bodyLen, midRight+1-bodyLen))
        midRange = set(range(midLeft, midRight+1))
        botRange = set(range(midLeft+bodyLen, midRight+1+bodyLen))

        # print()
        allRanges = set()
        allRanges.update(topRange)
        allRanges.update(midRange)
        allRanges.update(botRange)
        
        # check if num has symbol around it
        intersectionSymbols = allRanges.intersection(symbolIndices)
        if len(intersectionSymbols) > 0:
            symbolTuples = [(i, joinedData[i]) for i in intersectionSymbols]
            withAround.append((num, symbolTuples))
    
    # print(withAround)
    return sum([x[0] for x in withAround]), withAround

def solvePart2(data):
    _, withAround = solvePart1(data)
    
    # reverse withAround from Tuple(num, symbolTuples) to Dict(symbolTuple: loNums)
    
    symbolDict = {}
    for num, symbolTuples in withAround:
        for symbolTuple in symbolTuples:
            if symbolTuple not in symbolDict:
                symbolDict[symbolTuple] = []
            symbolDict[symbolTuple].append(num)
    
    # print(symbolDict)
    
    res = 0
    
    for i, symbol in symbolDict.keys():
        loNums = symbolDict[(i, symbol)]
        if len(loNums) == 2:
            res += (loNums[0] * loNums[1])
    
    return res

if __name__ == '__main__':
    # read test file
    with open('test.txt', 'r') as f:
        test = f.read()
    
    start = time()
    
    part1 = solvePart1(test)[0]
    p1Time = time() - start
    
    part2 = solvePart2(test)
    p2Time = time() - p1Time - start
    
    print()
    
    # print solutions and show time elapsed
    print(f'Part 1 ({p1Time:.4f}s):\n{part1}\n')
    print(f'Part 2 ({p2Time:.4f}s):\n{part2}\n')