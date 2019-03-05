
class Heap_Max():
    """
    Puts biggest element on top of the heap
    """
    def __init__(self):
        self.__heap = []
        self.__last_index = -1

    def __len__(self):
        return self.__last_index + 1

    def __get_parent(self, index):
        """
        gets parent index and parent node value for a certain node
        :param index: position
        :return: parent index and parent node value
        """
        if index is 0:
            return None, None
        else:
            parent_index = index //2
            return parent_index, self.__heap[parent_index]

    def __get_left_child(self, index):
        """
        Returns left child details. If not accessible, return None.
        :param index: position
        :return: left child details
        """
        lc_index = 2*index+1
        if lc_index > self.__last_index:
            return None, None
        else:
            return lc_index, self.__heap[lc_index]

    def __get_right_child(self, index):
        """
        Returns right child details. If not accessible, return None
        :param index: position
        :return: right child details
        """
        rc_index = 2*index+2
        if rc_index > self.__last_index:
            return None, None
        else:
            return rc_index, self.__heap[rc_index]

    def __sift_up(self, index):
        """
        Ensures that an item finds its right place in the heap by moving up the heap
        :param index: position
        :return: Changes heap
        """
        while index>0:
            parent_index, parent_value = self.__get_parent(index)
            if parent_value >= self.__heap[index]:
                break

            self.__heap[parent_index], self.__heap[index] = self.__heap[index], self.__heap[parent_index]
            index = parent_index

    def __sift_down(self, index):
        """
        Ensures that an item finds its right place in the heap by moving down the heap
        :param index: position
        :return: changes heap
        """
        while True:
            index_value = self.__heap[index]
            left_index, left_index_value = self.__get_left_child(index)
            right_index, right_index_value = self.__get_right_child(index)
            #If position to be accessed is not available
            if left_index is None or right_index is None:
                break
            else:
                #If parent is already bigger than its children
                if index_value >= left_index_value and index_value >= right_index_value:
                    break
                #If at least one child is bigger and if that child is the left child
                elif left_index_value>=right_index_value:
                    new_index = left_index
                #If the right child is bigger
                else:
                    new_index = right_index
                #Swap elements
                self.__heap[new_index], self.__heap[index] = self.__heap[index], self.__heap[new_index]
                index =  new_index

    def push(self, item):
        """
        Add element at the end and use __sift_up()
        :param item: new item
        :return: changes heap
        """
        #Adds element, so increase index
        self.__last_index += 1
        #If empty element space available
        if self.__last_index < len(self.__heap):
            self.__heap[self.__last_index] = item
        #If heap is full
        else:
            self.__heap.append(item)
        self.__sift_up(self.__last_index)

    def pop(self):
        """
        Pops element at the top of the heap. Moves last element up to the top and sift down.
        :return: removed element
        """
        #Empty heap
        if self.__last_index == -1:
            raise IndexError('pop from empty heap')
        #Element on top
        max_value = self.__heap[0]
        #Assign last element to the top of heap
        self.__heap[0] = self.__heap[self.__last_index]
        self.__last_index -= 1
        self.__sift_down(0)

        return max_value


class Heap_Min:
    """
    Puts smallest element on the top
    """
    def __init__(self):
        self.__heap = []
        self.__last_index = -1

    def __len__(self):
        return self.__last_index + 1

    def __get_parent(self, index):
        if index is 0:
            return None, None
        parent_index = index//2
        return parent_index, self.__heap[parent_index]

    def __get_left_child(self, index):
        left_child_index = index*2 +1
        if left_child_index > self.__last_index:
            return None, None
        return left_child_index, self.__heap[left_child_index]

    def __get_right_child(self, index):
        right_child_index = index*2+2
        if right_child_index > self.__last_index:
            return None, None
        return right_child_index, self.__heap[right_child_index]


    def __sift_up(self, index):
        while(index>0):
            parent_index, parent_value = self.__get_parent(index)
            if parent_value <= self.__heap[index]:
                break

            self.__heap[parent_index], self.__heap[index] = self.__heap[index], self.__heap[parent_index]

            index = parent_index

    def __sift_down(self, index):
        while True:
            index_value = self.__heap[index]
            left_child_index, left_child_value = self.__get_left_child(index)
            right_child_index, right_child_value = self.__get_right_child(index)

            if right_child_index is None or left_child_index is None:
                break

            else:
                if index_value <= left_child_value and index_value<=right_child_value:
                    break

                if left_child_value<right_child_value:
                    new_index = left_child_index
                else:
                    new_index = right_child_index
                self.__heap[new_index], self.__heap[index] = self.__heap[index], self.__heap[new_index]
                index = new_index

    def push(self, item):
        self.__last_index+=1
        if self.__last_index < len(self.__heap):
            self.__heap[self.__last_index]=item
        else:
            self.__heap.append(item)
        self.__sift_up(self.__last_index)

    def pop(self):
        if self.__last_index == -1:
            raise IndexError('pop from empty heap')

        min_value = self.__heap[0]
        self.__heap[0] = self.__heap[self.__last_index]
        self.__last_index -= 1
        self.__sift_down(0)

        return min_value





import random
values = random.sample(range(100), 15)
print(values)

h = Heap_Min()
for v in values:
    h.push(v)

while(len(h)>0):
    print(h.pop(), end = ' , ')

print("\n------------------\n")


h1 = Heap_Max()
for v in values:
    h1.push(v)

while(len(h1)>0):
    print(h1.pop(), end = ' , ')
