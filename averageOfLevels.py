import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
    def calculateAverage(branches):
        sum = 0
        for branch in branches:
            sum += branch.val
        return sum/len(branches)

    levelBranches = []
    queue = collections.deque([[root, 0]])
    while len(queue) > 0:
        popped = queue.popleft()
        current = popped[0]
        level = popped[1]
        if len(levelBranches) <= level:
            levelBranches.append([current])
        else:
            levelBranches[level].append(current)
        if current.left != None:
            queue.append([current.left, level+1])
        if current.right != None:
            queue.append([current.right, level+1])
        print(current.val, "level", level)

    result = []
    for branches in levelBranches:
        result.append(calculateAverage(branches))
    return result


# node2L = TreeNode(15)
# node2R = TreeNode(7)
# node1L = TreeNode(9)
# node1R = TreeNode(20, node2L, node2R)
# root = TreeNode(3, node1L, node1R)

node2L = TreeNode(15)
node2R = TreeNode(7)
node1L = TreeNode(9, node2L, node2R)
node1R = TreeNode(20)
root = TreeNode(3, node1L, node1R)

averageOfLevels(root)
