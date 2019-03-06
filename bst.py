class TreeNode:
    """
    Provides helper functions to get the work done in BST class
    """
    def __init__(self, key, val, left = None, right = None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and (self.parent.left_child is self)

    def is_right_child(self):
        return self.parent and (self.parent.right_child is self)

    def is_root(self):
        """
        Returns true only if the node has no parent, ie its the root
        :return: boolean
        """
        return not self.parent

    def is_leaf(self):
        """
        Returns true if the node doesn't have children
        :return: boolean
        """
        return not (self.right_child or self.left_child)

    def has_any_child(self):
        return (self.right_child or self.left_child)

    def has_both_children(self):
        return (self.right_child and self.left_child)

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        """
        Finds the next largest element in the tree with self as root node
        :return:
        """
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_child():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent

            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def put(self, key, val):
        """
        Enables to build the binary search tree.
        Uses private function _put() if root already exists
        :param key:
        :param val:
        :return:
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):
        """
        Puts in node at appropriate place based on BST property
        :param key: to be compared
        :param val:
        :param current_node: existing position
        :return:
        """
        if key<current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent = current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val,current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent = current_node)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        """
        Traverses from current node to retrieve matching key
        :param key:
        :param current_node:
        :return:
        """
        if not current_node:
            return None
        elif current_node.key is key:
            return current_node
        elif current_node.key<key:
            self._get(key, current_node.right_child)
        else:
            self._get(key, current_node.left_child)


    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -=1
            else:
                raise KeyError("Error, key not in tree")

        elif self.size == 1 and self.root.key is key:
            self.root = None
            self.size -=1

        else:
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node):

        #Leaf case - Node to be deleted is a leaf
        if current_node.is_leaf():
            if current_node.parent.right_child is current_node:
                current_node.parent.right_child = None
            else:
                current_node.parent.left_child = None

        #Bi-parent - Node to be deleted has two children
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload


        #Single child for current node
        else:
            #Current node has left child
            if current_node.has_left_child():
                #Node to be deleted is a right child
                if current_node.is_right_child():
                    current_node.parent.right_child = current_node.left_child
                    current_node.left_child.parent = current_node.parent
                #Node to be deleted is a left child
                elif current_node.is_left_child():
                    current_node.parent.left_child = current_node.left_child
                    current_node.left_child.parent = current_node.parent
                #Node to be deleted is root node
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.payload,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)

            #Current node has a right child
            else:
                #Node to be deleted is a right child
                if current_node.is_right_child():
                    current_node.parent.right_child = current_node.right_child
                    current_node.right_child.parent = current_node.parent
                #Node to be deleted is a left child
                elif current_node.is_left_child():
                    current_node.parent.left_child = current_node.right_child
                    current_node.right_child.parent = current_node.parent
                #Node to be deleted is root node
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.payload,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)






mytree = BinarySearchTree()
mytree.put(0,"red1")
mytree.put(1,"red2")


print(mytree[0])
#print(mytree[3])
#print(mytree[2])

