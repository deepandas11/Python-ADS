class BinaryTree():
    """
    Functions defined so as to help build a binary tree based on nodes and references
    The attributes left and right will become references to other instances of the BinaryTree class.
    """

    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, item):
        if self.left is None:
            self.left = BinaryTree(item)
        else:
            new_left = BinaryTree(item)
            new_left.left = self.left
            self.left = new_left

    def insertRight(self, item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            new_right = BinaryTree(item)
            new_right.right = self.right
            self.right = new_right

    def getRootVal(self):
        return self.key

    def setRootVal(self, item):
        self.key = item

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
