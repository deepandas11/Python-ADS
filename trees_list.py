
"""
:Accessing subtrees and tree elements using standard indexing:
:Repository of functions to help formalize this definition
"""
myTree = ['a', ['b',['d',[],[]],['e',[],[]]], ['c',['f',[],[]],[]]]
print(myTree)
print("Left Subtree: ", myTree[1])
print("Right Subtree: ", myTree[2])


def binaryTree(r):
    """
    Returns a binary tree with r at root and two empty branches
    :param r: root value
    :return: tree with two children
    """
    return [r, [], []]

def insertLeft(root, newBranch):
    """
    Insert a subtree at second position but move down existing subtree
    If existing tree is present in root, should look like [root, [newbranch,t,[]],[rst]]
    :param root: root node
    :param newBranch: new subtree
    :return: Modified tree
    """
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    """
    Insert a subtree at third position but move down existing subtree
    If existing tree is present in root, should look like [root, [newBranch,[],t],[rst]]
    :param root: root node
    :param newBranch: new subtree
    :return: Modified tree
    """
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, item):
    root[0] = item

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]




r = binaryTree('a')
insertLeft(r,'b')
insertLeft(r,'d')
insertRight(r,'c')
insertRight(r,'e')
l = getLeftChild(r)
print(l)

setRootVal(l,'A')
print(r)
insertLeft(l,'Z')
print(r)
print(getRightChild(getRightChild(r)))