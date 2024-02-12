from linked_list.linked_list import LinkedList


class HashTable:
    def __init__(self):
        self.entries: list[LinkedList] = \
            [LinkedList() for _ in range(5)]

    class _KeyValueEntry:

        def __init__(self, key, value):
            self._key = key
            self.value = value

        @property
        def key(self):
            return self._key

        def __repr__(self):
            return f'{self._key}:{self.value}'

    def put(self, key, value):
        index = self._hash(key)
        existing_entry = self.get_node(key)
        if (existing_entry is None):
            entry = HashTable._KeyValueEntry(key, value)
            self.entries[index].append(entry)
        else:
            existing_entry.content.value = value

    def get_node(self, key) :
        index = self._hash(key)
        for entry in self.entries[index].iter_nodes():
            if entry.content.key == key:
                return entry
        return None

    def get(self, key):
        res = self.get_node(key)
        if (res is None):
            return None
        else:
            return res.content.value

    def remove(self, key):
        index = self._hash(key)
        node = self.get_node(key)
        if (node is not None):
            self.entries[index].remove(node)

    def _hash(self, key: str) -> int:
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % len(self.entries)


if __name__ == '__main__':
    ht = HashTable()
    ht.put("aabb", "A")
    ht.put("abab", "B")
    ht.put("baba", "C")
    print(ht.get("aabb"))
    ht.remove("aabb")
    print(ht.get("aabb"))
    print(ht.get("abab"))
    print(ht.get("baba"))
