class Node:
    '''
    Class to define a Node for the Unordered list.
    Each node has a next pointer and a data associated with it
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

class UnorderedList():

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        flag = False
        current = self.head
        while current is not None and not flag:
            if current.getData() == item:
                flag = True
            current = current.getNext()
        return flag

    def remove(self, item):
        flag = False
        current = self.head
        previous = None
        if not self.search(item):
            print(self.show())
            item = int(input("Item not in List as shown above. Enter another element from the list to remove: "))

        while not flag and current is not None:
            if current.getData() is item:
                flag = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def show(self):
        current = self.head
        string = ""
        while current is not None:
            if current.getNext() is None:
                string = string + str(current.getData())
            else:
                string = string + str(current.getData())+" --> "
            current = current.getNext()
        return string

    def append(self, item):
        temp = Node(item)
        if self.head is None:
            temp.setNext(None)
            self.head = temp
        else:
            current = self.head
            lastflag = False
            while not lastflag:
                if current.getNext() is None:
                    lastflag = True
                else:
                    current = current.getNext()
            temp.setNext(None)
            current.setNext(temp)

    def insert(self, existing_item, item):
        temp = Node(item)
        while not self.search(existing_item) and existing_item is not None:
            print(self.show())
            existing_item = int(input("Entered item doesn't exist. Enter new item after which you wish to enter new item: "))
        current = self.head
        flag = False
        if existing_item is None:
            self.add(item)
        else:
            while not flag and current is not None:
                if current.getData() is existing_item:
                    flag = True
                else:
                    current = current.getNext()
            temp.setNext(current.getNext())
            current.setNext(temp)

    def pop(self, existing_item):
        current = self.head
        flag = False

        if existing_item is None:
            self.remove(self.head)

        else:
            while not self.search(existing_item):
                print(self.show())
                existing_item = int(input("Entered item doesn't exist. Enter new item after which you wish to remove an item: "))

            while current.getNext().getNext() is not None and not flag:
                if current.getNext().getData() is existing_item:
                    flag = True
                else:
                    current = current.getNext()
            rem = current.getNext().getNext()
            self.remove(rem)






l = UnorderedList()
l.add(3)
l.add(4)
l.add(5)
l.add(10)
l.add(100)
print(l.show())
print(l.size())
print(l.search(4))
l.remove(10)
print(l.show())
l.append(45)
l.append(43)
print(l.show())
l.insert(None,1000)
print(l.show())
l.insert(5, 32)
print(l.show())
l.pop(5)
print(l.show())
#l.pop(None)
#print(l.show())
#l.pop()
#print(l.show())
