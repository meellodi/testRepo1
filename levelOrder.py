from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class customQueue:
    lst = []
    l = 0

    def __init__(self, lst=None) -> None:
        self.lst = lst
        self.l = len(lst)

    def popleft(self):
        popped = self.lst[0]
        self.lst = self.lst[1:]
        self.l -= 1
        return popped

    def append(self, x):
        self.lst.append(x)
        self.l += 1

    def len(self):
        return self.l

    def show(self):
        print(self.lst)


def levelOrder(root):
    if root == None:
        return []
    levelBranches = []
    level = 0
    myQueue = customQueue([[root, level]])
    while myQueue.len() > 0:
        rawPopped = myQueue.popleft()
        popped = rawPopped[0]
        level = rawPopped[1]
        if level >= len(levelBranches):
            levelBranches.append([popped.val])
        else:
            levelBranches[level].append(popped.val)
        print(popped.val, level)
        if popped.children != None:
            for i in popped.children:
                myQueue.append([i, level+1])
    print(levelBranches)
    return levelBranches


node20 = Node(5)
node21 = Node(6)
node10 = Node(3, [node20, node21])
node11 = Node(2)
node12 = Node(4)
node00 = Node(1, [node10, node11, node12])

levelOrder(node00)
levelOrder(None)
