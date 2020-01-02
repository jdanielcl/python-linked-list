from unittest import TestCase
from main import LinkedList, Node

class NodeTest(TestCase):

    def setUp(self):
        self.value_a = 10
        self.node_a = Node(self.value_a)
        self.value_b = 20
        self.node_b = Node(self.value_b)

    def test_get_data(self):
        self.assertEqual(self.value_a, self.node_a.get_data())
        self.assertEqual(self.value_b, self.node_b.get_data())
    
    def test_set_next(self):
        self.node_a.set_next(self.node_b)
        self.assertEqual(self.node_a._Node__next, self.node_b)
    
    def test_set_previous(self):
        self.node_b.set_previous(self.node_a)
        self.assertEqual(self.node_b._Node__previous, self.node_a)
    
    def test_get_next(self):
        self.node_a.set_next(self.node_b)
        self.assertEqual(self.node_a.get_next(), self.node_a._Node__next)
    
    def test_get_previous(self):
        self.node_b.set_previous(self.node_a)
        self.assertEqual(self.node_b.get_previous(), self.node_b._Node__previous)

    def test_get_str(self):
        self.assertEqual(str(self.value_a), str(self.node_a))

    def test_repr(self):
        self.assertEqual(repr(self.node_a), "<Node: 10>")


class LinkedListTest(TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.append(1)

    def test_append(self):
        # first element
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__count, 1)
        self.linked_list.append(2)
        # second element
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        # chained elements
        self.assertEqual(self.linked_list._LinkedList__first._Node__next.get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__last._Node__previous.get_data(), 1)

    def test_find(self):
        self.assertEqual(self.linked_list.find(1), 0)

    def test_not_find(self):
        self.assertIsNone(self.linked_list.find(10))
    
    def test_pop_unique_element(self):
        self.assertIsNone(self.linked_list.pop())
        self.assertIsNone(self.linked_list._LinkedList__first)
        self.assertIsNone(self.linked_list._LinkedList__last)

    def test_lpop_unique_element(self):
        self.assertIsNone(self.linked_list.lpop())
        self.assertIsNone(self.linked_list._LinkedList__first)
        self.assertIsNone(self.linked_list._LinkedList__last)

    def test_pop_in_empty_list(self):
        self.assertIsNone(self.linked_list.pop())
        self.assertIsNone(self.linked_list.pop())

    def test_lpop_in_empty_list(self):
        self.assertIsNone(self.linked_list.lpop())
        self.assertIsNone(self.linked_list.lpop())

    def test_pop_element(self):
        self.linked_list.append(2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        self.linked_list.pop()
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__count, 1)
    
    def test_lpop_element(self):
        self.linked_list.append(2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        self.linked_list.lpop()
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__count, 1)
    
    def test_show_elements(self):
        self.assertEqual(self.linked_list.show_elements(), '[1]')
        self.linked_list.append(2)
        self.assertEqual(self.linked_list.show_elements(), '[1, 2]')

    def test_show_empty_list(self):
        self.linked_list.pop()
        self.assertEqual(self.linked_list.show_elements(), '[]')
    
    def test_len_method(self):
        self.assertEqual(self.linked_list._LinkedList__count, 1)
        self.assertEqual(len(self.linked_list), 1)
        self.linked_list.append(2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        self.assertEqual(len(self.linked_list), 2)
    
    def test_cero_len_method(self):
        self.linked_list.pop()
        self.assertEqual(self.linked_list._LinkedList__count, 0)
        self.assertEqual(len(self.linked_list), 0)

    def test_contains(self):
        self.assertTrue(1 in self.linked_list)

    def test_not_contains(self):
        self.assertFalse(2 in self.linked_list)
    
    def test_iterator(self):
        self.linked_list.append(2)
        my_iterator = iter(self.linked_list)
        self.assertEqual(str(next(my_iterator)), "1")
        self.assertEqual(str(next(my_iterator)), "2")
        self.assertRaises(StopIteration, next, my_iterator)
        my_iterator = iter(self.linked_list)
        self.assertEqual(str(next(my_iterator)), "1")