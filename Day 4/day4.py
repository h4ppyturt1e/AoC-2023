from time import time
import re
from math import floor

def solvePart1(data):
    data = [line.split(": ")[1].split(" | ") for line in data.split("\n")]
    
    lineData = []
    
    for true, owned in data:
        true = {int(x) for x in true.split(" ") if x}
        owned = {int(x) for x in owned.split(" ") if x}
        lineData.append((true, owned))
    
    # print(lineData)
    
    totalPoints = 0
    countList = []
    for true, owned in lineData:
        count = sum([1 for x in owned if x in true])
        points = floor(2 ** (count - 1))
        # print(points)
        totalPoints += points
        countList.append(count)
        
    return totalPoints, countList

def solvePart2(data):
    cardDict = {i: 1 for i in range(len(data))}

    for i, count in zip(range(len(data)), data):
        for _ in range(cardDict[i]):
            for j in range(count):
                cardDict[i + j + 1] += 1
                
    return sum(cardDict.values())

if __name__ == '__main__':
    # read test file
    with open('test.txt', 'r') as f:
        test = f.read()
    
    start = time()
    
    part1, lineData = solvePart1(test)
    p1Time = time() - start
    
    part2 = solvePart2(lineData)
    p2Time = time() - p1Time - start
    
    # print solutions and show time elapsed
    print(f'Part 1 ({p1Time:.4f}s):\n{part1}\n')
    print(f'Part 2 ({p2Time:.4f}s):\n{part2}\n')