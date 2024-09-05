
import unittest
import sys

sys.path.append('/home/bstrang/repos/blind-python/problems/twopointers/')
sys.path.append('/home/bstrang/repos/blind-python/problems/shared/')

import linked_list_node
import remove_nth_node_from_end_of_list


class TestRemoveNthNodeFromEndOfList(unittest.TestCase):
    def test_example1(self):
        input_linked_list = linked_list_node.LinkedListNode(
            1, linked_list_node.LinkedListNode(2))
        expected_output = linked_list_node.LinkedListNode(1)
        self.assertEqual(remove_nth_node_from_end_of_list.remove_nth_last_node
                         (input_linked_list, 1).data, expected_output.data)
