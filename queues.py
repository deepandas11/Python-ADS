class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def dequeue(self):
        return self.items.pop()

    def enqueue(self, item):
        self.items.insert(0, item)

    def show(self):
        s = ""
        for i in range(len(self.items)):
            if i == len(self.items) - 1:
                s = s + str(self.items[i])
            else:
                s = s + str(self.items[i]) + ", "
        print("Queue is: " + s)


q = Queue()
q.enqueue(3)
q.show()
q.enqueue(5)
q.enqueue(9)
q.show()
q.dequeue()
q.enqueue(4)
q.show()

#Question1 for Queues

def hotPotato(names, num= 5):
    '''
    Simulate the game hot potato
    :param num: number of times the ball is passed around
    :param names: list of people playinh
    :return: winner name
    '''
    q = Queue()
    for i in names:
        q.enqueue(i)

    while(q.size()>1):
        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q

playerslist = ['A','B','C','D','E']
winner = hotPotato(playerslist,9)
winner.show()