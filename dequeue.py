class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def show(self):
        s = ""
        for i in range(len(self.items)):
            if i == len(self.items)-1:
                s = s+str(self.items[i])
            else:
                s = s+str(self.items[i])+", "
        print("Dequeue is: " +s)


d = Dequeue()
d.add_front(3)
d.add_front(5)
d.add_front(9)
d.show()
d.add_rear(4)
d.add_rear(6)
d.add_rear(8)
d.show()
d.remove_front()
d.show()
d.remove_rear()
d.show()


def PalindromeCheck(s):
    '''
    Checks if the string s is a palindrome
    :param s: string
    :return: true or false
    '''
    d = Dequeue()
    for i in s:
        d.add_front(i)
    d.show()
    flag = True
    while(flag and d.size()>1):
        first_element = str(d.remove_rear())
        last_element = d.remove_front()
        if(first_element!= last_element):
            flag = False
        return flag

list1 = 'lkjjkl'
list2 = 'fjk'

print(PalindromeCheck(list1))


