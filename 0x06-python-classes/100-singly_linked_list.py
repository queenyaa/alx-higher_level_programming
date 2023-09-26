#!/usr/bin/python3

"""
this module defines the Node and SinglyLinkedList classes
"""


class Node:
    """
    this class represents a node in singly linked list

    Attributes:
        __data (int): the data stored in the node
        __next_node (Node): the next node in the linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the node class

        Args:
            data (int): the data to be stored in the node
            next_node (Node, optional): the next node in the linked list,
                defaults to None

        Raises:
            TypeError: if data is not an integer or if next_node is not a
                node object
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data stored in the node

        Returns:
            int: the data stored in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        sets the data stored in the node

        Args:
            value (int): the new data to be stored in the node

        Raises:
            TypeError: if the valuew is not integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list

        Returns:
            Node: the next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        sets the next node in the linked list

        Args:
            value (Node): the new next node in the linked list

        Raises:
            TypeError: if value is not a node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    This class represents a singly linked list

    Attributes:
        head: the head (first node) of the linke list
    """

    def __init__(self):
        """
        Initialize a new instance of the SinglyLinkedList class
            with an empty linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked
        list (increasing order).

        Args:
            value (int): the value to be inserted into the linked list

        Raises:
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        new_node = Node(value)

        if self.head is None:
            # if the list is empty, set the new node as the head
            self.head = new_node
        elif value < self.head.data:
            """
            if the new value is smaller than the head's data insert it at
                the beginning
            """
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list

        Returns:
            str: a string representation of the linked list
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
