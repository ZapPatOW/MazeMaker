import random
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import colormap 

class Node:
    top = None
    right = None
    bottom = None
    left = None
    def __init__(self, value, ):
        self.value = value
    def __str__(self):
        return f"{self.value:<2}"
    def __repr__(self):
        return f"{self.value:<2}"
    def addTop(self, top: 'Node'):
        self.top = top
    def addRight(self, right: 'Node'):
        self.right = right
    def addBottom(self, bottom: 'Node'):
        self.bottom = bottom
    def addLeft(self, left: 'Node'):
        self.left = left


def printMaze(maze: list[list[Node]]):
    rows, cols = len(maze), len(maze[0])
    fig, ax = plt.subplots()
    for row in range(rows):
        for col in range(cols):
            x, y = col, rows - row - 1
            node = maze[row][col]
            if node.top is not None:
                ax.plot([x, x+1], [y+1, y+1], color='black')        
            if node.bottom is not None:
                ax.plot([x, x+1], [y, y], color='black')
            if node.left is not None:
                ax.plot([x, x], [y, y+1], color='black')    
            if node.right is not None:
                ax.plot([x+1, x+1], [y, y+1], color='black')
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

def createBlankMaze(rows, cols) -> list[list[Node]]: 
    maze = [[None for _ in range(cols)]for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            node = Node(random.randint(0,99)) 
            maze[row][col] = node
            if row > 0:
                leftNode = maze[row-1][col]
                node.addLeft(leftNode)
                leftNode.addRight(node)
            if col > 0:
                topNode = maze[row][col-1]
                node.addTop(topNode)
                topNode.addBottom(node)
    return maze

def dfsMazeGen(maze, row, col, visited):
    rows = len(maze)
    cols = len(maze[0]) 
    visited.add((row,col))
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    random.shuffle(directions)
    for dr, dc in directions:
        currRow = row+dr
        currCol = col+dc
        if currRow < rows and currRow >= 0 and currCol < cols and currCol >= 0 and (currRow,currCol) not in visited:
            if dr == -1:
                maze[row][col].top = None
                maze[currRow][currCol].bottom = None
            if dr == 1:
                maze[row][col].bottom = None
                maze[currRow][currCol].top = None
            if dc == -1:
                maze[row][col].left = None
                maze[currRow][currCol].right = None
            if dc == 1:
                maze[row][col].right = None
                maze[currRow][currCol].left = None
            dfsMazeGen(maze,currRow,currCol,visited)

def bfsSolver(maze, row, col):
    visited = set()
    pass

def printSolution():
    pass

def main():
    rows = int(input("how many rows do you want in the maze?:"))
    cols = int(input("how many rows do you want in the maze?:"))

    #rows = 40 #for quick testing
    #cols = 40
    maze = createBlankMaze(rows,cols)
    visited = set()
    dfsMazeGen(maze, 0, 0, visited)
    printMaze(maze)
    #bfsSolver(maze)
    
    


if __name__ == "__main__":
    main()