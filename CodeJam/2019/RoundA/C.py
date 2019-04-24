class Node:
    def __init__(self, letter):
        self.letter = letter
        self.wordsContaining = 0
        self.children = []
        
def insert(node, word):
    if len(word) != 0:
        letter = word[-1]
        node.wordsContaining += 1
        found = False
        for child in node.children:
            if child.letter == letter:
                insert(child, word[:-1])
                found = True
        if found == False:
            newChild = Node(letter)
            node.children.append(newChild)
            insert(newChild, word[:-1])
    else:
        node.wordsContaining += 1
        
def traverse(node):
    if node.wordsContaining < 2:
        return 0
    if node.wordsContaining == 2:
        return 2
    foundRhymes = 0
    for child in node.children:
        foundRhymes += traverse(child)
    if foundRhymes <= (node.wordsContaining-2):
        foundRhymes += 2 
    return foundRhymes
    
cases = int(input())
for case in range(1, cases+1):
    numWords = int(input())
    words = []
    head = Node("1")
    for _ in range(numWords):
        word = input()
        insert(head, word)
    foundRhymes = 0
    for child in head.children:
        foundRhymes += traverse(child)
    print("Case #{}: {}".format(case, foundRhymes))
        

        


        