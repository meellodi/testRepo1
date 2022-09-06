class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pruneTree(root):

    originalRoot = root

    def checkBranch(node):
        if node == None:
            # print("kosong")
            return False
        elif node.val == 0:
            # print("nol")
            return False or (checkBranch(node.left) or checkBranch(node.right))
        else:
            # print("1")
            return True

    def pruneTreeRec(root):
        # print(root.val)
        if checkBranch(root.left):
            pruneTreeRec(root.left)
        else:
            root.left = None
        if checkBranch(root.right):
            pruneTreeRec(root.right)
        else:
            root.right = None
    if not checkBranch(root):
        return None
    pruneTreeRec(root)
    return originalRoot


a20 = TreeNode(0)
a21 = TreeNode(1)
a11 = TreeNode(0, a20, a21)
a00 = TreeNode(1, None, a11)


res1 = pruneTree(a00)


def tranverse(root):
    if root != None:
        print(root.val)
    else:
        print("kosong")
        return
    if root.left != None:
        tranverse(root.left)
    if root.right != None:
        tranverse(root.right)


tranverse(res1)
