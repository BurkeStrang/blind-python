import unittest
from problems.shared.linked_list_node import LinkedListNode
from problems.twopointers.remove_nth_last_node import remove_nth_last_node


class TestRemoveNthNodeFromEndOfList(unittest.TestCase):

    def test_example1(self):
        input_linked_list = LinkedListNode(
            1, LinkedListNode(2))
        expected_output = LinkedListNode(1)
        self.assertTrue(remove_nth_last_node(
            input_linked_list, 1).__eq__(expected_output))

    def test_example2(self):
        input_linked_list = LinkedListNode(
            1, LinkedListNode(2, LinkedListNode(
                3, LinkedListNode(4, LinkedListNode(5)))))
        expected_output = LinkedListNode(1, LinkedListNode(
            2, LinkedListNode(3, LinkedListNode(5))))
        self.assertTrue(remove_nth_last_node(
            input_linked_list, 2).__eq__(expected_output))
