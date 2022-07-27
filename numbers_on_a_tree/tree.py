import sys

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0

class perfectBinaryTree:
    def __init__(self, H):
        self.H = H
        self.root = Node()
        self.root.val = 2**(H+1) - 1
        self.counter = self.root.val
        self.constructTree()

    def insert_two(self, node, val):
        if val > 2**self.H:
            node.left = Node()
            node.right = Node()
            const = 2**(self.H+1) - val
            lft = val - const
            rght = lft - 1
            node.left.val = lft
            node.right.val = rght
            self.insert_two(node.left, lft)
            self.insert_two(node.right, rght)
        
    def constructTree(self):
        self.insert_two(self.root, self.root.val)            


def main():
    lines = [line.strip() for line in sys.stdin]
    line = lines[0].split()

    H = int(line[0])
    path = line[1]
    
    tree = perfectBinaryTree(H)
    node = tree.root

    for i in path:
        if i == 'L':
            node = node.left
        elif i == 'R':
            node = node.right
    
    print(node.val)


main()