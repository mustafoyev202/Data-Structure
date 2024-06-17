class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedListNode:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("None")
            return
        itr = self.head
        arr = ''
        while itr:
            arr += str(itr.data) + '-->'
            itr = itr.next
        arr += 'None'
        print(arr)

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def return_count(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.return_count():
            raise ValueError("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.return_count():
            raise ValueError("Index out of range")
        if index == 0:
            self.insert_at_beginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                new_node = Node(data_to_insert, itr.next)
                itr.next = new_node
                return
            itr = itr.next
        raise ValueError(f"Value {data_after} not found in the list")

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

        raise ValueError(f"Value {data} not found in the list")


ll = LinkedListNode()
ll.insert_values(['banana', 'mango', 'kiwi'])
ll.print_list()
ll.remove_at(1)
ll.print_list()
ll.insert_at(1, 'apple')
ll.print_list()
ll.insert_after_value('banana', 'orange')
ll.print_list()
ll.remove_by_value('banana')
ll.print_list()
