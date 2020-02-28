from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Check if the length of the storage is less than the total capacity
        if self.storage.length < self.capacity:
            # If this is true, then adding the value to the tail
            self.storage.add_to_tail(item)
        # If the storage length has met capacity
        # elif self.storage.length == self.capacity:
            # Then, we will want to remove the last value
            # And we will want to add the new value to to the front
        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

       # Setting current value to the head
        current = self.storage.head
       # while loop to append values to given [] as long as there is some value in the head
        while current is not None:
            list_buffer_contents.append(current)
            current = current.next
        return list_buffer_contents


# Testing if functionality is working
buffer = RingBuffer(1)
print("Blank Buffer: ", buffer.get())
buffer.append('a')
print("New Buffer: ", buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
