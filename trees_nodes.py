class BinaryTree():
    """
    Functions defined so as to help build a binary tree based on nodes and references
    The attributes left and right will become references to other instances of the BinaryTree class.
    Also describes traversal methods
    """

    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None

    def insert_left(self, item):
        if self.left is None:
            self.left = BinaryTree(item)
        else:
            new_left = BinaryTree(item)
            new_left.left = self.left
            self.left = new_left

    def insert_right(self, item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            new_right = BinaryTree(item)
            new_right.right = self.right
            self.right = new_right

    def get_root_val(self):
        return self.key

    def set_root_val(self, item):
        self.key = item

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def preorder_traversal(self):
        """
        Node -> Left -> Right
        :return: Prints tree
        """
        print(self.key)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def inorder_traversal(self):
        """
        Left -> Node -> Right
        :return: Prints tree
        """
        if self.left:
            self.left.inorder_traversal()
        print(self.key)
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        """
        Left -> Right -> Node
        :return: Prints tree
        """
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.key)




r = BinaryTree(10)
print(r.get_root_val())

r.insert_left(5)
r.left.insert_left(51)
r.left.insert_right(52)
r.insert_right(6)
r.right.insert_left(61)
r.right.insert_right(62)

#print(r.get_left_child())
print('----------------------------------\nPostorder : ')
r.postorder_traversal()
print('----------------------------------\nPreorder: ')

r.preorder_traversal()
print('----------------------------------\nInorder: ')
r.inorder_traversal()