class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def postorder(root):
    lst = []

    def postorderRec(root):
        lst.append(root.val)
        if (root.children != None):
            root.children.reverse()
            for child in root.children:
                postorderRec(child)
    postorderRec(root)
    print(lst)


n20 = Node(4)
n21 = Node(5)
n22 = Node(6)
n10 = Node(2, [n20, n21])
n11 = Node(3, [n22])
n00 = Node(1, [n10, n11])

postorder(n00)
