import random
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, value, top = None, right = None, bottom = None, left = None):
        self.value = value
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
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
    rows = len(maze)
    for row in range(rows):
        print(maze[row])
    vals = [[node.value for node in row] for row in maze]
    plt.imshow(vals)
    plt.colorbar()
    plt.show()

def createMaze(rows, cols) -> list[list[Node]]: 
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


def main():
    rows = int(input("how many rows do you want in the maze?:"))
    cols = int(input("how many rows do you want in the maze?:"))
    maze = createMaze(rows,cols)
    printMaze(maze)
    #Make all 
    
    


if __name__ == "__main__":
    main()