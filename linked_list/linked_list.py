class LinkedList:
    class _Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __repr__(self):
            return f'{self.value} | {str(id(self))[-4:]}'

    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def add_first(self, value):
        node = self._Node(value)
        if self.is_empty:
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node
        self._size += 1

    def remove_first(self):
        if self.is_empty:
            raise Exception("No such element")
        if self.first == self.last:
            self.first = self.last = None
        else:
            temp = self.first.next
            self.first.next = None
            self.first = temp
        self._size -= 1

    def add_last(self, value):
        node = self._Node(value)
        if self.is_empty:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self._size += 1

    def remove_last(self):
        if self.is_empty:
            raise Exception("No such element")
        if self.first == self.last:
            self.first = self.last = None
        else:
            prev = self.get_previous(self.last)
            prev.next = None
            self.last = prev
        self._size -= 1

    def get_previous(self, target):
        for node in self.iter_nodes():
            if node.next is target:
                return node
        return None

    def iter_nodes(self):
        ptr = self.first
        while ptr:
            yield ptr
            ptr = ptr.next

    def index_of(self, value):
        for idx, node in enumerate(self.iter_nodes()):
            if node.value == value:
                return idx
        return -1

    def contains(self, value):
        return self.index_of(value) != -1

    @property
    def as_list(self):
        list = []
        for node in self.iter_nodes():
            list.append(node)
        return list

    @property
    def is_empty(self):
        return self.first is None

    @property
    def size(self):
        return self._size

    def __str__(self):
        elements = [str(node.value) for node in self.iter_nodes()]
        return ' --> '.join(elements) + ' --> None'
