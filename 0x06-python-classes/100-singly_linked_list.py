#!/usr/bin/python3
class Node:
    """Node class representing a single element in a singly linked list.

    Attributes:
        data (int): The integer data stored in the node.
        next_node (Node, optional): Reference to the next node in the list. Defaults to None.

    Raises:
        TypeError: If `data` is not an integer.
        TypeError: If `next_node` is not a Node object or None.

    """

    def __init__(self, data, next_node=None):
        """
        Initialize a Node object with data and optional next_node.

        Args:
            data (int): The integer data stored in the node.
            next_node (Node, optional): Reference to the next node in the list. Defaults to None.

        Raises:
            TypeError: If `data` is not an integer.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node."""
        return self._data

    @data.setter
    def data(self, value):
        """Set the data stored in the node to a new integer value.

        Args:
            value (int): The new integer data to store.

        Raises:
            TypeError: If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Get the reference to the next node in the list."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Set the reference to the next node in the list.

        Args:
            value (Node, optional): The new next node object.

        Raises:
            TypeError: If `value` is not a Node object or None.
        """
        if value is None or isinstance(value, Node):
            self._next_node = value
        else:
            raise TypeError("next_node must be a Node object")
class SinglyLinkedList:
    """Class representing a singly linked list containing integer data.

    Attributes:
        _head (Node): Reference to the head node of the list. Private attribute with no getter or setter.

    """

    def __init__(self):
        """Initialize an empty SinglyLinkedList object."""
        self._head = None

    def __str__(self):
        """
        Returns a string representation of the linked list, printing each node's data on a new line.

        Returns:
            str: String representation of the linked list.

        """
        current = self._head
        string = ""
        while current:
            string += f"{current.data}\n"
            current = current.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """
        Inserts a new Node with the given value into the correct sorted position (increasing order) of the list.

        Args:
            value (int): The integer value to insert.

        Raises:
            ValueError: If the value already exists in the list.

        """
        new_node = Node(value)
        if not self._head or value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
            return

        current = self._head
        previous = None
        while current and value >= current.data:
            previous = current
            current = current.next_node

        if previous:
            previous.next_node = new_node
        else:
            raise ValueError("Value already exists in the list")
        new_node.next_node = current

