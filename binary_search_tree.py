class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def set_val(self, item):
        self.val = item

    def get_val(self):
        return self.val

    def get_children(self):
        children = []
        if self.leftChild is not None:
            children.append(self.leftChild)

        if self.rightChild is not None:
            children.append(self.rightChild)

        return children


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, item):
        self.root = Node(item)

    def insert_node(self, current_node, item):
        if(item <= current_node.val):
            if(current_node.leftChild):
                self.insert_node(current_node.left_child, item)
            else:
                current_node.left_child = Node(item)
        elif(item>current_node.val):
            if(current_node.rightChild):
                self.insert_node(current_node.rightChild, item)
            else:
                current_node.rightChild = Node(item)

    def insert(self, item):
        if self.root is None:
            self.set_root(item)
        else:
            self.insert_node(self.root, item)

    def find_node(self, currentNode, item):
        if currentNode is None:
            return False
        elif item is currentNode.val:
            return True
        elif item < currentNode.val:
            return self.find_node(currentNode.leftChild, item)
        else:
            return self.find_node(currentNode.rightChild, item)

    def find(self, item):
        return self.find_node(self.root, item)


b1 = BinarySearchTree()
b1.insert(3)
b1.insert(5)
b1.insert(90)
b1.insert(10)
b1.insert(13)


print(b1.find_node(b1.root, 932))