from linked_list.linked_list import LinkedList


def testing_linked_list():
    ll = LinkedList()
    ll.add_last("Alice")
    ll.add_last("Bob")
    ll.add_last("Alex")
    # ll.remove_first()
    print(f'Size: {ll.size}')
    print(ll.get_previous(ll.last))
    print(ll)
    print(ll.index_of("Alice"))
    print(ll.contains("Alex"))
    print(ll.as_list)


if __name__ == '__main__':
    testing_linked_list()
