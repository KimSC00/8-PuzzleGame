import random

start = [1,2,3,4,5,6,7,0,8]

goal = (1,2,3,4,5,6,7,8,0)

def is_solvable(puzzle):
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i+1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

def randomize_state():
    while True:
        puzzle = start.copy()
        random.shuffle(puzzle)
        if is_solvable(puzzle):
            return puzzle

def up(puzzle):
    index = puzzle.index(0)
    
    if index == 0 or index == 1 or index == 2:
        return puzzle
    else:
        puzzle[index] = puzzle[index - 3]
        puzzle[index - 3] = 0
        return puzzle

def down(puzzle):
    index = puzzle.index(0)
    
    if index == 6 or index == 7 or index == 8:
        return puzzle
    else:
        puzzle[index] = puzzle[index + 3]
        puzzle[index + 3] = 0
        return puzzle

def right(puzzle):
    index = puzzle.index(0)
    
    if index == 2 or index == 5 or index == 8:
        return puzzle
    else:
        puzzle[index] = puzzle[index + 1]
        puzzle[index + 1] = 0
        return puzzle

def left(puzzle):
    index = puzzle.index(0)
    
    if index == 0 or index == 3 or index == 6:
        return puzzle
    else:
        puzzle[index] = puzzle[index - 1]
        puzzle[index - 1] = 0
        return puzzle

def draw_puzzle(puzzle, count):
    print("거쳐간 노드 수 : ", count)
    print("-------------")
    print("|", puzzle[0], "|", puzzle[1], "|", puzzle[2],"|")
    print("-------------")
    print("|", puzzle[3], "|", puzzle[4], "|", puzzle[5],"|")
    print("-------------")
    print("|", puzzle[6], "|", puzzle[7], "|", puzzle[8], "|")
    print("-------------\n")

def breadth_first_search():
    print(" ======== 너비 우선 탐색 =========")
    open = [start]
    closed = set()
  
    print("시작노드 : ", open)
    count = 1
    while open != []:
        puzzle = open.pop(0)
        
        count += 1
        
        if puzzle == goal:
            draw_puzzle(puzzle, count)
            print(" Success ")
            return True
        else :
                closed.add(puzzle)        
                draw_puzzle(puzzle, count)

                change = []
                tmp = puzzle
                
                change.append(up(list(tmp)))
                change.append(down(list(tmp)))
                change.append(left(list(tmp)))
                change.append(right(list(tmp)))

        for i in range(len(change)):
            if tuple(change[i]) not in closed: 
                open.append(tuple(change[i]))
         
    print("Fail")
    return False


start = tuple(randomize_state())
breadth_first_search()