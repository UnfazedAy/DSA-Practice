#!/usr/bin/python3

class Node:
    """
    Node class for linked list
    """

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    """
    Linked list class
    """

    def __init__(self, value) -> None:
        """
        Initialize the linked list With a head, tail, and length
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        """
        A method to print all values in the linked list
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value) -> bool:
        """
        Append a new node to the end of the linked list
        """
        new_node = Node(value)
        # If there is no head, then the new node is the head and the tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        #  If there is a head and a tail, then the new node is the tail
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self) -> Node:
        """
        A method to remove the last node in the linked list
        """
        if self.length == 0:
            return None

        # If there are nodes in the linked list
        # then set the tail to the node before the tail
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # If after popping, the length is 0, then there is no head or tail
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value) -> bool:
        """
        A method to add a new node to the beginning of the linked list
        """
        # If there is no head, then the new node is the head and the tail
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        # Add the new node to the beginning of the linked list
        # and set the head to the new node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node:
        """
        A method to remove the first node in the linked list
        """
        if self.length == 0:
            return None

        # Set the head to the next node
        # and remove the reference to the previous head
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index) -> Node:
        """
        A method to get a node at a given index
        """

        # Check if the index is valid and return the node at that index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value) -> bool:
        """
        Change the value of a node at a given index
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value) -> bool:
        """
        Set a new node at a given index
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        # Set the new node to the given value and get the node before the index
        new_node = Node(value)
        temp = self.get(index - 1)

        # Set the new node's next to the temp's next
        # and set temp's next to the new node
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
