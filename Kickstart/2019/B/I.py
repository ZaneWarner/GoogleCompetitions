class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.leftSide = 0
        self.rightSide = 0
        self.h = {}

def insert(node, nodeString, left, right):
    node.leftSide = left
    node.rightSide = right
    if len(nodeString)==1:
        node.h[nodeString] = 1
    else:
        half = len(nodeString)//2
        node.left = Node()
        insert(node.left, nodeString[:half], left, left+half-1)
        node.right = Node()
        insert(node.right, nodeString[half:], left+half, right)
        for elem in node.left.h:
            if elem in node.h:
                node.h[elem] += node.left.h[elem]
            else:
                node.h[elem] = node.left.h[elem]
        for elem in node.right.h:
            if elem in node.h:
                node.h[elem] += node.right.h[elem]
            else:
                node.h[elem] = node.right.h[elem]
                
class Tree:
    def __init__(self, head):
        self.head = head
        self.h = {}
        
    def range(self, left, right):
        self.h = {}
        self.traverse(self.head, left, right)
        palindrome = True
        if (right-left) % 2 == 0: #odd num elements in interval
            center = True
        else:
            center = False
        for elem in self.h:
            if self.h[elem] % 2 != 0 and center:
                center = False
            elif self.h[elem] % 2 != 0:
                palindrome = False
        return palindrome
        
    def traverse(self, node, left, right):
        if node.leftSide == left and node.rightSide == right:
            for elem in node.h:
                if elem in self.h:
                    self.h[elem] += node.h[elem]
                else:
                    self.h[elem] = node.h[elem]
        else:
            if left < node.right.leftSide:
                self.traverse(node.left, left, min(right, node.left.rightSide))
            if right > node.left.rightSide:
                self.traverse(node.right, max(left, node.right.leftSide), right)

cases = int(input())
for case in range(1, cases+1):
    N, Q = [int(s) for s in input().split()]
    fullString = input()
    x = Tree(Node())
    insert(x.head, fullString, 0, len(fullString)-1)
    validPalindromes = 0
    for _ in range(Q):
        L, R =  [int(s) for s in input().split()]
        found = x.range(L-1, R-1)
        if found:
            validPalindromes += 1
    print("Case #{}: {}".format(case, validPalindromes))
    
    
# x = Tree(Node())
# insert(x.head, "ABAACCA", 0, 6)
# print(x.range(3, ))

    