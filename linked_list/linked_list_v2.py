# @author Parham Modirniya
class LinkedList:
    class _Node():
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next: LinkedList._Node = next
            self.prev: LinkedList._Node = prev

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.head: LinkedList._Node | None = None
        self.tail: LinkedList._Node | None = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __str__(self):
        elements = [str(node) for node in self]
        return ('None <- ' + ' <-> '.join(elements) + ' -> None'
                + f'\nsize: {self.size}')

    def prepend(self, data):
        nd = self._new_node(data)
        if self.head:
            self.head.prev = nd
            nd.next = self.head
            self.head = nd
        else:
            self.head = self.tail = nd
        self._increase_size()

    def append(self, data):
        nd = self._new_node(data)
        if self.tail:
            self.tail.next = nd
            nd.prev = self.tail
            self.tail = nd
        else:
            self.head = self.tail = nd
        self._increase_size()

    def insert(self, index, data):
        next = self._get_node(index)
        if not next.prev:
            self.prepend(data)
        else:
            nd = self._new_node(data)
            prev = next.prev
            nd.next = next
            nd.prev = prev
            prev.next = nd
            next.prev = nd
            self._increase_size()

    def pop_front(self):
        res = self.head
        if res and res.next:
            next = res.next
            self.head = next
            self.head.prev = None
            res.next = None
        else:
            self.clear()
        self._decrease_size()
        return res

    def pop_back(self):
        res = self.tail
        if res and res.prev:
            prev = res.prev
            self.tail = prev
            self.tail.next = None
            res.prev = None
        else:
            self.clear()
        self._decrease_size()
        return res

    def remove_at(self, index):
        nd = self._get_node(index)
        if nd:
            self._remove_node(nd)

    def find(self, data):
        for i, nd in enumerate(self):
            if nd.data == data:
                return i
        return -1

    def contains(self, data):
        return self.find(data) != -1

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _new_node(self, data) -> _Node:
        if data is None:
            raise Exception("Data cannot be None")
        return self._Node(data)

    def _get_node(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Out of range index")
        for i, nd in enumerate(self):
            if i == index:
                return nd
        return None

    def _remove_node(self, targ: _Node):
        if targ is None:
            raise Exception("Invalid parameter")

        if targ.next is None:
            self.pop_back()
        elif targ.prev is None:
            self.pop_front()
        else:
            prev = targ.prev
            next = targ.next
            prev.next = next
            next.prev = prev
            self._decrease_size()

    def _increase_size(self):
        self.size += 1

    def _decrease_size(self):
        self.size -= 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.prepend("B")
    ll.prepend("A")
    ll.append("D")
    ll.append("E")
    ll.insert(2,"C")
    print(ll)
    ll.remove_at(4)
    print(ll.find("D"))
    print(ll.contains("C"))
    # ll.insert(2, "C")
    # print(ll.pop_head())
    # print(ll.pop_head())
    # print(ll.pop_head())
    print(ll)
    pass

#
#     def _prev_node_by_index(self, index: int):
#         if index < 1 or index > self.size - 1:
#             raise Exception("Out of range")
#         for i, node in enumerate(self):
#             if i == index - 1:
#                 return node
#         return None
#
#     def _prev_node_by_value(self, data: str):
#         if type(data) is not str:
#             raise Exception("Invalid parameter")
#         prev_node = None
#         for node in self:
#             if node.data == data:
#                 break
#             prev_node = node
#         if prev_node is self.tail:
#             return None
#         else:
#             return prev_node
#
#     def prepend(self, data):
#         nd = self._new_node(data)
#         if self.head is None:
#             self.head = self.tail = nd
#         else:
#             nd.next = self.head
#             self.head = nd
#         self.size += 1
#
#     def append(self, data):
#         nd = self._new_node(data)
#         if self.tail is None:
#             self.head = self.tail = nd
#         else:
#             self.tail.next = nd
#             self.tail = nd
#         self.size += 1
#
#     def insert(self, index, data):
#         nd = self._new_node(data)
#         prev = self._prev_node_by_index(index)
#         if prev:
#             nd.next = prev.next
#             prev.next = nd
#             self.size += 1
#
#     def pop_head(self):
#         res = self.head
#         if res and res.next:
#             self.head = res.next
#             res.next = None
#         else:
#             self.clear()
#         return res
#
#     def pop_tail(self):
#         pass
#
#     def clear(self):
#         self.head = None
#         self.tail = None
#
#     # def remove(self, data):
#     #     if (self.head.data == data):
#     #         self.
#     #         prev_node = self._prev_node_by_value(data)
#     #     if prev_node:
#     #         cur_node = prev_node.next
#
#     def find(self, data):
#         for i, node in enumerate(self):
#             if node.data == data:
#                 return i
#         return -1
#
#
