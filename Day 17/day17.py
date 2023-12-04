from time import time


def solvePart1(data):
    return

def solvePart2(data):
    return

if __name__ == '__main__':
    # read test file
    with open('test.txt', 'r') as f:
        test = f.read()
    
    start = time()
    
    part1 = solvePart1(test)
    p1Time = time() - start
    
    part2 = solvePart2(test)
    p2Time = time() - p1Time
    
    # print solutions and show time elapsed
    print(f'Part 1 ({p1Time:.4f}s):\n{part1}\n')
    print(f'Part 2 ({p2Time:.4f}s):\n{part2}\n')