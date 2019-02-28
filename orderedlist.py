class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, item):
        self.next = item

    def setData(self, item):
        self.data = item


class OrderedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def search(self, item):
        current = self.head
        flag = False
        stop = False
        while current is not None and not flag and not stop:
            if current.getData() is item:
                flag = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return flag

    def add(self, item):
        temp = Node(item)
        current = self.head
        flag = False
        previous = None
        while current is not None and not flag:
            if current.getData() > item:
                flag = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

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


l = OrderedList()
l.add(5)
l.add(9)
print(l.show())
l.add(1)
l.add(13)
l.add(34)
l.add(12)
print(l.show())
l.remove(12)
print(l.show())



