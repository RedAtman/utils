class Node():
    __slots__ = [
        '_item',
        '_next',
        # '__dict__',
    ]

    def __init__(self, item):
        self._item = item
        self._next = None

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setItem(self, newitem):
        self._item = newitem

    def setNext(self, newnext):
        self._next = newnext


class SingleLinkedDeque():
    def __init__(self):
        self._head = None  # 初始化为空链表

    def is_empty(self):
        return self._head == None

    def size(self):
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def __iter__(self):
        return self

    def __next__(self):
        current = self._head
        while current != None:
            # print(current, current.getItem())
            yield current
            current = current.getNext()
        # raise StopIteration()

    def reverse(self):
        prev = None
        current = self._head
        while(current is not None):
            next = current._next
            current._next = prev
            prev = current
            current = next
        self._head = prev

    def travel(self):
        current = self._head
        while current != None:
            # print(current.getItem())
            current = current.getNext()

    def add(self, item):
        temp = Node(item)
        temp.setNext(self._head)
        self._head = temp

    def extend(self, items: list):
        for item in items:
            self.add(item)

    def append(self, item):
        temp = Node(item)
        if self.is_empty():
            self._head = temp  # 若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()  # 遍历链表
            current.setNext(temp)  # 此时current为链表最后的元素

    def search(self, item):
        current = self._head
        founditem = False
        while current != None and not founditem:
            if current.getItem() == item:
                founditem = True
            else:
                current = current.getNext()
        return founditem

    def index(self, item):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getItem() == item:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            raise ValueError('%s is not in linkedlist' % item)

    def slice(self, index):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            if count == index:
                found = True
            else:
                current = current.getNext()
            count += 1
        if found:
            return current
        else:
            raise ValueError('%s is not in linkedlist' % item)

    def remove(self, item):
        current = self._head
        pre = None
        while current != None:
            if current.getItem() == item:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    def insert(self, pos, item):
        if pos <= 1:
            self.add(item)
        elif pos > self.size():
            self.append(item)
        else:
            temp = Node(item)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)


if __name__ == '__main__':
    a = SingleLinkedDeque()
    for i in range(1, 10):
        # print(i)
        a.append(i)
    # print(list(range(1, 10)))
    # print(a.size())
    # a.reverse()
    # a.add(18)
    # a.add(18)
    a.add(18)
    # a.travel()
    # print(a.search(6))
    # print(a.index(5))
    # print(a.slice(0)._item)
    # a.remove(4)
    # a.travel()
    # a.insert(4, 100)
    # a.travel()
    # print(a.__next__())
    # print(a._head)
    for i in a.__next__():
        print(i._item)
