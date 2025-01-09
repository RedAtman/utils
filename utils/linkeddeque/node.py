class _Node:
    """链表结点"""
    # __slots__ = [
    #     '_item',
    #     '_next',
    #     # '__dict__',
    # ]

    def __init__(self, item=None, prev=None, next=None):
        self._item = item  # 对象元素
        self._prev = prev  # 前驱结点引用
        self._next = next  # 后继结点引用

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, item):
        self._prev = item

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, item):
        self._next = item
