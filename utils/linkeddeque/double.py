# class _Node:
#     """用于封装双向链表结点的类"""

#     def __init__(self, item=None, prev=None, next=None):
#         self.item = item  # 对象元素
#         self.prev = prev  # 前驱结点引用
#         self.next = next  # 后继结点引用

from .node import _Node


class _DoublyLinkedBase:
    """双向链表的基类"""

    def __init__(self):
        """创建一个空的双向链表"""
        self._header = _Node(item=None, prev=None, next=None)
        self._trailer = _Node(item=None, prev=None, next=None)
        self._header.next = self._trailer  # 尾哨兵结点在头哨兵结点之后
        self._trailer.prev = self._header  # 头哨兵结点在尾哨兵结点之前
        self._size = 0  # 元素数量

    def __len__(self):
        """返回链表元素数量"""
        return self._size

    def is_empty(self):
        """如果链表为空则返回True"""
        return self._size == 0

    def _insert_between(self, item, predecessor, successor):
        """
        在两个已有结点之间插入封装了元素item的新结点，并将该结点返回
        :param item: 新结点中的对象元素
        :param predecessor: 前驱结点
        :param successor: 后继结点
        :return: 封装了item的新结点
        """
        new_node = _Node(item, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """删除非哨兵结点并将结点返回"""
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        item = node.item
        node.prev = node.next = node.item = None
        return item


class Empty(Exception):
    """尝试对空队列进行删除操作时抛出的异常"""
    pass


class LinkedDeque(_DoublyLinkedBase):
    """使用双向链表实现的双端队列"""

    def __iter__(self):
        """
        正序迭代生成队列中的元素
        """
        cursor = self._header.next
        while cursor.item is not None:
            yield cursor.item
            cursor = cursor.next

    def _iter(self):
        """
        正序迭代生成队列中的node
        """
        cursor = self._header.next
        while cursor is not None:
            yield cursor
            cursor = cursor.next

    def iter_reverse(self):
        """
        反序迭代生成队列中的元素
        """
        cursor = self._trailer.prev
        while cursor.item is not None:
            yield cursor.item
            cursor = cursor.prev

    @property
    def first(self):
        """返回但不删除队头元素"""
        if self.is_empty():
            raise Empty('队列为空！')
        return self._header.next.item

    @property
    def last(self):
        """返回但不删除队尾元素"""
        if self.is_empty():
            raise Empty('队列为空！')
        return self._trailer.prev.item

    @property
    def _first(self):
        """返回但不删除队头元素"""
        if self.is_empty():
            raise Empty('队列为空！')
        return self._header.next

    @property
    def _last(self):
        """返回但不删除队尾元素"""
        if self.is_empty():
            raise Empty('队列为空！')
        return self._trailer.prev

    def insert_first(self, item):
        """在队列头部插入元素"""
        self._insert_between(item, self._header, self._header.next)

    def add(self, item):
        """在队列尾部插入元素"""
        self._insert_between(item, self._trailer.prev, self._trailer)

    # def extend(self, items):
    #     """在队列尾部插入多个元素"""
    #     for item in items:
    #         self._insert_between(item, self._trailer.prev, self._trailer)

    def delete_first(self):
        """删除队头结点，并返回结点元素域"""
        if self.is_empty():
            raise Empty('队列为空！')
        return self._delete_node(self._header.next)

    def delete_last(self):
        """删除尾结点，并返回结点元素域"""
        if self.is_empty():
            raise Empty('队列为空！')
        return self._delete_node(self._trailer.prev)

    def search(self, item, item_attr=None):
        current = self._header
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.item == item:
                found = True
            else:
                current = current.next
        if found:
            return current
        else:
            return

    def _index(self, item, item_attr=None):
        current = self._header
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if item_attr is None:
                if current.item == item:
                    found = True
                else:
                    current = current.item
            else:
                if current.item is None:
                    current = current.next
                    continue

                _ = getattr(current.item, item_attr, None)
                if _ is None:
                    return
                    raise ValueError(f'{current.item} has not {item_attr}')
                if _ == item:
                    found = True
                else:
                    current = current.next
        if found:
            return count
        else:
            return
            raise ValueError('%s is not in linkedlist' % item)


if __name__ == '__main__':
    lnk_deque = LinkedDeque()
    lnk_deque.add(9)
    lnk_deque.insert_first(5)
    print(len(lnk_deque))  # 2
    lnk_deque.add(3)
    lnk_deque.insert_first(8)
    print(list(lnk_deque))  # [3, 9, 5, 8]
    print(lnk_deque.delete_first())  # 3
    print(list(lnk_deque))  # [9, 5, 8]
    print(lnk_deque.delete_last())  # 8
    print(len(lnk_deque))  # 2
    print(list(lnk_deque))  # [9, 5]
    print(list(lnk_deque.iter_reverse()))  # [5, 9]
