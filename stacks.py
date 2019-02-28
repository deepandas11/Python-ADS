class Stack:
    '''
    Class to define a Stack class
    Last in First out (LIFO)
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def push(self, item):
        self.items.append(item)

    def show(self):
        s = ""
        for i in range(len(self.items)):
            if i == len(self.items)-1:
                s = s+str(self.items[i])
            else:
                s = s+str(self.items[i])+", "
        print("Stack is: " +s)

stack = Stack()
stack.push(1)
stack.push(34)
stack.push('e')
stack.show()
stack.pop()
stack.push(344)
stack.show()



'''
Question 1 using Stacks
'''

def parantheses_checker(symbolString):
    '''
    Checks whether the list of parantheses in symbolString is balanced or not
    :param symbolString: list of parantheses
    :return: true or false
    '''

    s = Stack()
    flag = True
    newSymbolString = symbolString.strip()
    i = 0
    while(flag == True and i<len(newSymbolString)):
        item = newSymbolString[i]
        if item == '(':
            s.push(item)
        else:
            if(s.isEmpty()):
                flag = False
            else:
                s.pop()
        i+=1

    return flag and s.isEmpty()

string1 = "(())()()(((())))"
string2 = "(((())))))"

print(parantheses_checker(string1))
print(parantheses_checker(string2))


'''
Question 2 using stacks
'''

def convert_dec2base(number, base=2):
    '''
    Converts any decimal number to any given base upto 16
    :param number: decimal number
    :param base: to which it is to be converted
    :return: converted number as integer
    '''

    digits = "0123456789ABCDEF"

    s = Stack()

    while number>0:
        rem = number%base
        s.push(rem)
        number = number//base

    new_number = Stack()
    while not s.isEmpty():
        new_number.push(digits[s.pop()])

    return new_number


convert_dec2base(15,16).show()


