class LinkedList:
    class _Node:
        def __init__(self, content, next=None):
            self.content = content
            self.next = next

        def __repr__(self):
            return f'{self.content} | {str(id(self))[-4:]}'

    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def get_by_index(self, index) -> _Node | None:
        for i, node in enumerate(self.iter_nodes()):
            if i == index: return node
        return None

    def append(self, value):
        node = self._Node(value)
        if self.is_empty:
            self._first = self._last = node
        else:
            self._last.next = node
            self._last = node
        self._size += 1

    def prepend(self, value):
        node = self._Node(value)
        if self.is_empty:
            self._first = self._last = node
        else:
            node.next = self._first
            self._first = node
        self._size += 1

    def pop(self):
        if self.is_empty:
            raise Exception("No such element")
        if self._first == self._last:
            self._first = self._last = None
        else:
            temp = self._first.next
            self._first.next = None
            self._first = temp
        self._size -= 1

    def pop_back(self):
        if self.is_empty:
            raise Exception("No such element")
        if self._first == self._last:
            self._first = self._last = None
        else:
            prev = self.get_previous_node(self._last)
            prev.next = None
            self._last = prev
        self._size -= 1

    def remove(self, target: _Node):
        if not self.contains(target.content):
            return
        prev_node = self.get_previous_node(target)
        if prev_node is None:
            self.pop()
        else:
            if target.next is None:
                self.pop_back()
            else:
                prev_node.next = target.next
                target.next = None
                self._size -= 1

    def get_previous_node(self, target: _Node):
        for node in self.iter_nodes():
            if node.next is target:
                return node
        return None

    def iter_nodes(self):
        ptr = self._first
        while ptr:
            yield ptr
            ptr = ptr.next

    def find_index(self, value):
        for idx, node in enumerate(self.iter_nodes()):
            if node.content == value:
                return idx
        return -1

    def contains(self, value):
        return self.find_index(value) != -1

    @property
    def as_list(self):
        list = []
        for node in self.iter_nodes():
            list.append(node)
        return list

    @property
    def is_empty(self):
        return self._first is None

    @property
    def size(self):
        return self._size

    def __str__(self):
        elements = [str(node.content) for node in self.iter_nodes()]
        return ' --> '.join(elements) + ' --> None'
